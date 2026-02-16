import os
from dotenv import load_dotenv
import requests

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
    data = response.json()
    return data.get("url", "")

def createWebhook(repoName : str, discordChannelId : str):
    url = createDiscordWebhook(discordChannelId)
    linkWebhook(url, repoName)

if __name__ == "__main__":
    createWebhook("Discord-Server-Notifications", "1472994225216819408")