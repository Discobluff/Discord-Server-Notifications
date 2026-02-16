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
            "url": webhookUrl,
            "content_type": "json"
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
    
def createDiscordWebhook(channelId : str, name : str) -> str:
    load_dotenv()
    discordToken = os.getenv("BOT_TOKEN")
    
    url = f"https://discord.com/api/v10/channels/{channelId}/webhooks"
    
    headers = {
        "Authorization": f"Bot {discordToken}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "name": name,
        "avatar": None
    }
    
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    return data.get("url", "")

if __name__ == "__main__":
    # url = createDiscordWebhook("1472994225216819408"," marge")
    # print(url)
    # linkWebhook(url, "Discord-Server-Notifications")
    
    content = {"content":"coucou"}
    requests.post("https://discord.com/api/webhooks/1473011873514258615/kMZ6rJk_L7AECKapOFNdxFbiGCRgXz81AyizYZ6THotoHHGKFjgHF96JoBsbTiyfmovN",json=content)