# Bot Discord per Assegnazione Ruoli

Bot Discord che permette agli utenti di scegliere i propri ruoli con un'interfaccia simile a SolarGuard.

## Setup

1. Clona questo repository
2. Installa le dipendenze: `pip install -r requirements.txt`
3. Modifica il file `main.py` con gli ID dei ruoli del tuo server Discord (variabile ROLES)
4. Aggiungi il token del bot come variabile d'ambiente `DISCORD_TOKEN` su Railway

## Utilizzo

- Il bot si avvia automaticamente su Railway
- Usa il comando `/ruoli` nel server Discord per aprire il menu di selezione
- Scegli i ruoli che preferisci dai menu a tendina

## Categorie disponibili:
- 🎨 Colore del tuo nome
- 👤 Genere
- 🎮 Giochi preferiti (selezione multipla)
- 🔔 Notifiche (selezione multipla)

## Configurazione Railway:
- Variabile d'ambiente: `DISCORD_TOKEN` = il_tuo_token_bot
- Build Command: `pip install -r requirements.txt`
- Start Command: `python main.py`
