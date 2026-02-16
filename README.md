# Discord-Server-Notifications

## Description

This project is for handling all of your repos notifications in one Discord server. You select a repo and a discord channel and you will receive notifications for Pushes and Pull Requests of the repo.

## Configuration

- Copy .env.example to .env
- Fill your Github username
- Create a Github token with the scope `repo` and add it to the .env file
- Create a [Discord app](https://discord.com/developers/applications/)
- Create a bot for the app and copy the token to the .env file. Toogle `Message Content Intent` on.
- Invite the bot to your server `https://discord.com/oauth2/authorize?client_id=CLIENT_ID&permissions=536881152&scope=bot%20applications.commands` (CLIENT_ID is your app id)


## Requirements

- Python 3.10 or higher

## Utilisation

### Terminal

```bash
python3 src/terminal.py
```

### Discord bot