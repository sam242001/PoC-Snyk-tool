Volg dit stappenplan nadat je eerst de vereisten in 'Requirements.md' hebt uitgevoerd.

Dit stappenplan beschrijft hoe het Python script de Snyk tool installeert, koppelt en hoe scans worden uitgevoerd.

## Stap 1: Snyk API token ophalen

1. Ga naar:

- https://app.snyk.io/login en log in op je Snyk account.

2. Ga naar:

- Account Settings -> Auth Token

3. Kopieer je token en bewaar deze tijdelijk (nodig voor authenticatie)

![Account Settings](docs/Images/Account Settings.png)

![Auth Token](docs/Images/Auth Token.png)


## Stap 2: Python Script uitvoeren

Open PowerShell in de map waar het script staat en voer uit met het volgende commando:

**python snyk_installer.py --token <JOUW_TOKEN>**

Het script geeft twee opties:

1. Het installeren van Snyk tool en scan uit voeren
2. Scan uitvoeren nadat Snyk al geïnstalleerd is
 
Het script voert automatisch uit:

- Installatie van Snyk tool
- Verifiëren van verbinding met je Snyk account
- Scannen van kwetsbaarheden

## Stap 3: Resultaten bekijken in Dashboard

1. Ga naar je Snyk account
2. Open het aangemaakte project
3. Hier zie je:
   - Kwetsbaarheden
   - Severity (Low / Medium / High / Critical)
   - Versiebeheer van risico's
   - Waar het risico plaatsvindt
   - Mogelijke fixes (oplossingen)









