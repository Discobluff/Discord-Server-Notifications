from webhook import createWebhook

if __name__ == "__main__":
    repoName = input("Enter the name of the repository : ")
    discordId = input("Enter the channel ID (activate Developer Options, then right click on the channel : )")
    createWebhook(repoName, discordId)