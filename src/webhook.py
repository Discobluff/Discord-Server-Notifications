import os
from dotenv import load_dotenv
import requests

class WebhookCreationError(Exception):
    pass

class GithubWebhookError(Exception):
    pass

def linkWebhook(webhookUrl : str, repoName : str):
    load_dotenv()
    githubToken = os.getenv("GITHUB_TOKEN")
    username = os.getenv("GITHUB_USERNAME")

    url = f"https://api.github.com/repos/{username}/{repoName}/hooks"
    
    headers = {
        "Authorization": f"token {githubToken}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    payload = {
        "name": "web",
        "active": True,
        "events": ["push", "pull_request"],
        "config": {
            "url": webhookUrl + "/github",
            "content_type": "json"
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code not in (200, 201):
        raise GithubWebhookError()
    return response.json()
    
def createDiscordWebhook(channelId : str) -> str:
    load_dotenv()
    discordToken = os.getenv("BOT_TOKEN")
    
    url = f"https://discord.com/api/v10/channels/{channelId}/webhooks"
    
    headers = {
        "Authorization": f"Bot {discordToken}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": "Github",
        "avatar": None
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code not in (200, 201):
        raise WebhookCreationError()
    data = response.json()
    return data.get("url", "")

def createWebhook(repoName : str, discordChannelId : str) -> str:
    try:
        url = createDiscordWebhook(discordChannelId)
        linkWebhook(url, repoName)
        return "Le lien a été créé avec succès"
    except WebhookCreationError:
        return "Echec de la création du webhook Discord"
    except GithubWebhookError:
        return "Echec de la création du webhook Github"