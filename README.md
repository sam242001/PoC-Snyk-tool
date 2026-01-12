# PoC Snyk Installer & System-Wide Scanner - Supply Chain Security

Dit project is een Proof of Concept voor het automatisch installeren en gebruiken van de Snyk tool om kwetsbaarheden in de software supply chain van huisartsenpraktijken te detecteren.

De PoC richt zich op:

- Automatische installatie van de Snyk CLI
- Uitvoeren van security-scans op software componenten
- Inzicht geven in kwetsbaarheden binnen dependencies en code

Het doel is om huisartsenpraktijken te ondersteunen bij het verbeteren van hun digitale weerbaarheid.

## Wat het project doet

De PoC bestaat uit:

- De vereisten om de Snyk tool te kunnen gebruiken.
  -> zie Requirements.md
- Een Python-script dat Snyk automatisch installeert.
- Een overzicht van hoe de Snyk tool wordt uitgevoerd en toegepast.

De tool detecteert kwetsbaarheden in:

- Open Source dependencies
- Applicatiecode
- Docker en containeromgevingen

## Hoe Snyk werkt

Snyk scant alleen dependency-managed projecten.
Het werkt niet als een antivirus en scant geen willekeurige bestanden.

Ondersteunde projectbestanden:

- `package.json` (Node.js)
- `requirements.txt`, `Pipfile.lock`, `poetry.lock` (Python)
- `composer.json` (PHP)
- `pom.xml`, `build.gradle` (Java)
- `Dockerfile` (Docker)

## Waarom dit project nuttig is

Huisartsenpraktijken werken met gevoelige patiëntgegevens en zijn afhankelijk van verschillende softwarecomponenten. Kwetsbaarheden in deze software supply chain kunnen leiden tot datalekken of verstoringen van zorgprocessen. 

Dit project is nuttig omdat het kwetsbaarheden in eigen broncode detecteert, dependencies helpt detecteren en het eenvoudig te integreren is in bestaande ontwikkel- en beheerprocessen. Daarnaast maakt de geautomatiseerde installatie van Snyk het mogelijk om de tool ook in te zetten binnen organisaties met weinig tot geen IT-expertise. 

De PoC ondersteunt huisartsenpraktijken bij het verbeteren van hun digitale weerbaarheid.

## Compatibiliteit

Het script ondersteunt de volgende platforms:

- Windows
- Linux
- macOS

## Wat wordt gescand

De scanner doorzoekt deze locaties op bestanden die door Snyk worden ondersteund.

### Linux

- `/home`
- `/root`
- `/opt`
- `/var/www`

### macOS

- `/Users`

### Windows

- `C:\`

### Uitgesloten directories

Om fouten en performance issues te voorkomen:

- `/proc`
- `/sys`
- `/dev`
- `/run`
- `/tmp`
- `/snap`
- `/usr/lib`
- `/usr/share`

## Functionaliteit

- Automatische OS-detectie
- Installatie van de juiste Snyk CLI versie
- Werkt op Windows, Linux en macOS
- System-wide scan (niet alleen current directory)
- Detecteert alleen echte Snyk-projecten
- Voorkomt onnodige Snyk errors (`SNYK-CLI-0000`)
- Projecten verschijnen automatisch in het Snyk Dashboard

## Testen

Voorbeeldtest:

```bash
mkdir snyk-test
cd snyk-test
npm init -y
npm install lodash@4.17.15
```
Het project verschijnt vervolgens in het Snyk Dashboard.

## Troubleshooting

- **PermissionError bij installatie**

  Zorg dat Powershell als Administrator geopend is. Het script moet draaien in een map waar je schrijfrechten hebt.

- **Geen projecten gevonden**

  Controleer of je projectbestanden aanwezig zijn in de map die wordt gescand.

- **npm niet gevonden (Windows)**

  Voer uit volgende commando uit:
```bash
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Security

- Zet je Snyk token nooit in GitHub repositories.
- Gebruik environment variables of secrets.

## Aan de slag

Voordat je gaat beginnen heb je een paar dingen nodig:
0. Openen van terminal met administrator rechten
  Zorg ervoor dat je een terminal opent op je computer met administratie rechten.
  
1. Node.js
  Dit is een manier van code lezen voor jouw computer. Dit heb je dus ook nodig voor als je het script wilt gaan draaien.
2. Snyk account
  Dit is de tool die wij gebruiken. Hier heb je een account voor nodig. Wanneer je het account hebt krijg je een token die aan je account staat gelinkt.
3. Installeren van het script
  Hier ga je het script downloaden wat wij in de github hebben staan `snyk-installer.py`
4. Het script moet nu uitgevoerd worden
  Om het script uit te kunnen voeren gebruik je het 'pad' naar het script met `--token [hier jouw account token]`
5. Kiezen van optie
  Hier kies je een optie. Je kiest 1 als je snyk nog niet gebruikt heb. Je kiest 2 als je het al een keer gebruikt heb.
6. Open account
  Zoek online naar snyk dashboard. Hier moet je vervolgens inloggen. Wanneer dit gedaan is ga je naar projects en vervolgens kan je hier je vulnerabilities vinden en hoe je het moet oplossen.

## Disclaimer

- Wanneer je meer wilt weten wat er met je informatie wordt gedaan door Snyk kan je de documentatie bekijken en voor jezelf oordelen of je het vertrouwt of niet. <a href="https://docs.snyk.io/snyk-data-and-governance/how-snyk-handles-your-data">Link naar documentatie</a>

Download de Python Script:

`Zie snyk-installer.py`

Lees de vereisten:

`Zie Requirements.md`
  
Volg daarna het stappenplan:

`Zie docs/stappenplan_snyk_tool.md`

Screenshots en voorbeelden staan in:

`Zie docs/images/`

## Licentie

MIT License

## Credits
- https://snyk.io

