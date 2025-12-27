Volg dit stappenplan nadat je eerst de vereisten in 'Requirements.md' hebt uitgevoerd.

Dit stappenplan beschrijft hoe het Python sccript de Snyk tool installeert, koppelt en hoe scans worden uitgevoerd.

## Stap 1: Snyk API token ophalen

1. Ga naar:

- https://app.snyk.io/login en log in op je Snyk account.

2. Ga naar:

- Account Settings -> Auth Token

3. Kopieer je token en bewaar deze tijdelijk (nodig voor authenticatie)

## Stap 2: Python Script uitvoeren

Open PowerShell in de map waar het script staat en voer uit met het volgende commando:

**python snyk_installer.py --token <JOUW_TOKEN>**

Het script voert automatisch uit:
- Installatie van Snyk tool
- Verifiëren van verbinding met je Snyk account

Als het script succesvol is afgerond is Snyk klaar voor gebruik.

## Stap 3: Kwetsbaarheden detecteren

Na het uitvoeren van de Python script in PowerShell voer uit:

**snyk code test**

Hiermee worden kwetsbaarheden gedetecteerd. Indien kwetsbaarheden worden gevonden worden ze in de terminal getoond.

## Stap 4: Kwetsbaarheden monitoren in Snyk Dashboard

Om de kwetsbaarheden in een dashboard te tonen moet hiervoor een project worden aangemaakt. 

Voer uit:

**snyk monitor**

Dit uploadt de scan naar je Snyk account en maakt automatisch een project in het webdashboard.

## Stap 5: Resultaten bekijken in Dashboard

1. Ga naar je Snyk account
2. Open het aangemaakte project
3. Hier zie je:
   - Kwetsbaarheden
   - Severity (Low / Medium / High / Critical)
   - Versiebeheer van risico's
   - Waar het risico plaatsvindt
   - Mogelijke fixes (oplossingen)









