# PoC Snyk tool - Supply Chain Security

Proof of Concept voor de automatische installatie van Snyk tool en het uitvoeren van code security tests gericht op de software supply chain van huisartsenpraktijken.

## Wat het project doet

Dit project is een Proof of Concept voor het automatisch installeren en gebruiken van de Snyk tool om kwetsbaarheden in de software supply chain te detecteren.

De PoC bestaat uit:
- De vereisten om de Snyk tool te kunnen gebruiken
- Een Python-script dat de Snyk tool automatisch installeert.
- Een overzicht van hoe de Snyk tool wordt uitgevoerd en toegepast.

Het project demonstreert hoe huisartsenpraktijken inzicht kunnen krijgen in beveiligingsrisico's binnen hun software.

## Waarom dit project nuttig is

Huisartsenpraktijken werken met gevoelige patiëntgegevens en zijn afhankelijk van verschillende softwarecomponenten. Kwetsbaarheden in deze software supply chain kunnen leiden tot datalekken of verstoringen van zorgprocessen. Dit project is nuttige omdat het kwetsbaarheden in eigen broncode detecteert en het eenvoudig te integreren is in bestaande ontwikkel- beheerprocessen.
De PoC ondersteunt huisartsenpraktijken bij het verbeteren van hun digitale weerbaarheid.

## Aan de slag

#### Compatibiliteit

Het script ondersteunt de volgende platforms:

- Windows
- Linux
- macOS
  
Lees eerst de vereisten:

-> Requirements.md
  
Volg daarna het stappenplan:

-> docs/stappenplan_snyk_tool.md

## Troubleshooting

- **PermissionError bij installatie van Snyk:**
  Zorg dat Powershell als Administrator geopend is. Het script moet draaien in een map waar je schrijfrechten hebt.

- **Geen projecten gevonden:**
  Controleer of je projectbestanden aanwezig zijn in de map die wordt gescand.

- **npm niet gevonden:**
  Voer uit het volgende; Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

