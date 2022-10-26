import discord
from dotenv import load_dotenv
import os
import menu

#Indiquer où est le fichier de config
load_dotenv(dotenv_path="config")

#Création du client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#Evenements
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    #Sécurité
    if message.author == client.user:
        return

    if message.content == "!menu":
        menuJours = menu.menuDuJours(menu.majMenu())
        messageText = ""
        messageText += "🍽 ___***" + menuJours[0] + "***___ 🍽" + "\n"
        
        for i in range(len(menuJours[1])):
            messageText += '• ' + menuJours[1][i] + "\n"
        await message.channel.send(messageText)

    if message.content == '!menuAll':
        dico = menu.majMenu()
        messageText = ""
        for jours in dico:
            messageText += "🍽 ___***" + jours + "***___ 🍽" + "\n"
            for y in range(len(dico[jours])):
                messageText += '• ' + dico[jours][y] + "\n"
            messageText += '\n'
        await message.channel.send(messageText)

#Démarrage du client
client.run(os.getenv("TOKEN"))
