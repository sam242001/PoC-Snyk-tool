Om deze Proof of Concept te kunnen uitvoeren, zijn de volgende vereisten nodig.

## 1. Snyk account
- Maak een gratis Snyk account aan via: https://app.snyk.io/login
- Inloggen kan via Github, Google, Bitbucket, Entra ID of Docker ID.
- Een gratis account is voldoende.

## 2. Node.js
Node.js is vereist voor het gebruik van de Snyk CLI.

### Installatie:
- Ga naar: https://nodejs.org/en/download
- Download en installeer de prebuilt Node.js.
- Open de bestand in Downloads map
- Volg de stappen in de wizard

### Controleer installatie:
In Powershell voer uit als administrator het volgende:
- node -v
- npm -v

Als versienummer wordt getoond is Node goed geïnstalleerd.

*Indien npm -v niet werkt in Powershell:*

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

