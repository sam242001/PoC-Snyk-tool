import os
import platform
import urllib.request
import subprocess
import sys
import argparse

# ----------------------------
# Argumenten
# ----------------------------
parser = argparse.ArgumentParser(
    description="Installeer Snyk en scan het hele systeem"
)
parser.add_argument("--token", required=True, help="Snyk authentication token")
args = parser.parse_args()

SNYK_TOKEN = args.token

print("\n🔐 Snyk installer & system-wide scanner\n")

# ----------------------------
# Menu
# ----------------------------
print("Kies een optie:")
print("1️  Installeer Snyk + scan alles")
print("2️  Scan alles (Snyk al geïnstalleerd)")

choice = input("\nVoer je keuze in (1 of 2): ").strip()
if choice not in ("1", "2"):
    print("❌ Ongeldige keuze.")
    sys.exit(1)

# ----------------------------
# OS detectie
# ----------------------------
os_name = platform.system().lower()

if os_name == "windows":
    snyk_path = os.path.join(os.getcwd(), "snyk.exe")
    snyk_url = "https://static.snyk.io/cli/latest/snyk-win.exe"
    scan_roots = [os.path.expandvars(r"C:\\")]
elif os_name == "linux":
    snyk_path = "/usr/local/bin/snyk"
    snyk_url = "https://static.snyk.io/cli/latest/snyk-linux"
    scan_roots = ["/home", "/root", "/opt", "/var/www"]
elif os_name == "darwin":
    snyk_path = "/usr/local/bin/snyk"
    snyk_url = "https://static.snyk.io/cli/latest/snyk-macos"
    scan_roots = ["/Users"]
else:
    print("❌ Besturingssysteem niet ondersteund.")
    sys.exit(1)

# ----------------------------
# Installatie
# ----------------------------
if choice == "1":
    print("\n⬇️  Snyk downloaden...")
    if os_name == "windows":
        urllib.request.urlretrieve(snyk_url, snyk_path)
    else:
        tmp_path = "/tmp/snyk"
        urllib.request.urlretrieve(snyk_url, tmp_path)
        subprocess.run(["chmod", "+x", tmp_path])
        subprocess.run(["mv", tmp_path, snyk_path])

if not os.path.exists(snyk_path):
    print("❌ Snyk niet gevonden.")
    sys.exit(1)

# ----------------------------
# Authenticatie
# ----------------------------
env = os.environ.copy()
env["SNYK_TOKEN"] = SNYK_TOKEN
subprocess.run([snyk_path, "auth", SNYK_TOKEN], env=env)

# ----------------------------
# Geldige Snyk-projecten detecteren
# ----------------------------
PROJECT_MARKERS = {
    "package.json",
    "requirements.txt",
    "Pipfile.lock",
    "poetry.lock",
    "composer.json",
    "pom.xml",
    "build.gradle",
    "Dockerfile"
}

EXCLUDED_DIRS = ("proc", "sys", "dev", "run", "tmp", "snap", "usr/lib", "usr/share")

def is_valid_project(path):
    try:
        files = set(os.listdir(path))
        return bool(PROJECT_MARKERS.intersection(files))
    except (PermissionError, FileNotFoundError):
        return False

def is_excluded(path):
    return any(ex.lower() in path.lower() for ex in EXCLUDED_DIRS)

projects = set()

for root_dir in scan_roots:
    for root, dirs, _ in os.walk(root_dir, topdown=True):
        if is_excluded(root):
            dirs[:] = []
            continue
        if is_valid_project(root):
            projects.add(root)
            dirs[:] = []

# ----------------------------
# Monitor scan
# ----------------------------
if not projects:
    print("⚠️  Geen ondersteunde projecten gevonden.")
    sys.exit(0)

print(f"\n📦 {len(projects)} project(en) gevonden:\n")
for project in sorted(projects):
    print(f"➡️  Scannen: {project}")
    subprocess.run([snyk_path, "monitor"], cwd=project, env=env)

print("\n🎉 Klaar! Alle projecten zijn geregistreerd in Snyk dashboard.")
input("\nDruk op Enter om af te sluiten...")
