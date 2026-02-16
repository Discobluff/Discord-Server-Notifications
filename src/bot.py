import discord
import os
from dotenv import load_dotenv
from webhook import createWebhook

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
	print("Bot Ready !")

@bot.event
async def on_message(message):
	if message.content.startswith("!github "):
		githubRepo = message.content.split(" ")[1]
		channelId = message.channel.id
		await message.delete()
		response = createWebhook(githubRepo, channelId)
		await message.channel.send(response)
  
def run():
    load_dotenv()
    bot.run(os.getenv("BOT_TOKEN"))
    
if __name__ == "__main__":
    run()
    