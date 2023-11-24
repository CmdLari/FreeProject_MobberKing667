import os
import random
from tokenize import StringPrefix
import discord
from discord.ext import commands
from discord import Client


client = discord.Client()

STA = (
    "https://static.bnn.de/karlsruhe/karlsruhe-stadt/H%C3%A4sslich.jpg-cwfruz/alternates/SQUARE_BASE/H%C3%A4sslich.jpg",
    "Wusstet ihr, das Stuttgart die schlechteste Luft Deutschlands hat?",
    "Wer Stuttgart liebt, muss das Leben hassen",
    "Deine Mudda is aus Stuttgart!",
    "https://luftdaten.info/wp-content/uploads/2017/01/feinstaubalarm_website.png",
    "Stuttgart is wie Essen ohne Knoblauch",
)

HH = (
    "Wusstest du, dass 250 Menschen täglich in die Hansestadt ziehen",
    "In Hamburg wohnen die besseren Stuttgarter!",
    "In Hamburg is Party",
    "https://media2.giphy.com/media/l4FGqZ0SJWW6u1jgY/giphy.gif?cid=ecf05e47wm7w8l5ldg6t26h6e2jfkwhxkf6ltf0myxigx3hb&rid=giphy.gif",
)

DRK = (
    "https://media2.giphy.com/media/l4Jzgmad24DGBqQ4U/giphy.gif?cid=ecf05e47vk91i4ir02vfpvd9crquva3titi2gwa4vh7et8q4&rid=giphy.gif",
    "Komm nach Hamburg! Partey!",
    "Die direkten und indirekten Kosten alkoholbedingter Krankheiten werden pro Jahr auf 40 Milliarden Euro geschätzt.",
    "12,6 Prozent der Bevölkerung im Alter von 18 bis 64 Jahren (rund 6,7 Millionen Menschen) trinken laut Statistiken von 2018 riskante Durchschnittsmengen, also so viel Alkohol, dass sie ihre Gesundheit damit gefährden.",
    "Ab 40 Gramm Alkohol pro Tag, das entspricht zwei Halben Bier oder zwei Vierteln Wein, ist es wahrscheinlich, dass die Leber langfristig leidet.",
    "https://media3.giphy.com/media/TgC8jEirdyKICUVPPs/giphy.gif?cid=790b7611ba9435ddd4fadeadb99b9a88787ba09592f2ed8e&rid=giphy.gif",
    "https://media4.giphy.com/media/3ohfFJUMgs8m5F9qec/giphy.gif?cid=ecf05e47bd49nfupc8puxzpdt6pitk9uwzbf7eifore0lbnl&rid=giphy.gif",
    "Better to be a well-known drunkard than an anonymous alcoholic.",
    "Let us drink to bread, for without bread, there would be no toast.",
    "Here’s to alcohol, Which often makes one see double And feel single.",
    "Alcohol may be man’s worst enemy, but the Bible says love your enemy.",
    "Here’s to your liver! May it live as long as you last.",
    "Here’s to doing and drinking, Not sitting and thinking.",
    "When the liquor is inside, The pain goes elsewhere.",
)

PF = (
    "Kroketten sind besser als Pommes.",
)

TFT = (
    "https://media2.giphy.com/media/xXHEDLRTGvRNqT0d11/giphy.gif?cid=ecf05e47rx40ki6qyxs88h2trb2d7u2e4n8zx6uiid7dol9k&rid=giphy.gif",
    "https://media3.giphy.com/media/v0Q0PXuTW572ZHe7k3/giphy.gif?cid=ecf05e471gedpo21ua02xxvyndkz3n82u5tp9by58fybxi0c&rid=giphy.gif",
    "https://media2.giphy.com/media/HAUGxU70sYfpsUlfPm/giphy.gif?cid=ecf05e473x59k0p4231qlykc5yspt5gvgnwro7tkdii1bqwk&rid=giphy.gif",
)

FOOD = (
    "https://media.giphy.com/media/TNeilKIVOAKmk/giphy.gif",
    "https://media.giphy.com/media/DZQuf6L7aNsaI/giphy.gif",
    "https://media.giphy.com/media/xT1R9DXgQBOUGpmJQk/giphy.gif",
    "https://media1.giphy.com/media/Ff2LmUUzZQAeY/giphy.gif?cid=790b76114925bf2b2ee97618bc232773dbcafd821559c639&rid=giphy.gif",
    "https://media.giphy.com/media/l0HlRbvm8of0UYPAs/giphy.gif",
)

NCE = (
    "**is it though...?**",
)

PLY = (
    "https://media.giphy.com/media/L5aC2b3jRvURi/giphy.gif",
    "https://media.giphy.com/media/cHqKAAIYc6sIRsHFjW/giphy.gif",
    "https://media.giphy.com/media/cHqKAAIYc6sIRsHFjW/giphy.gif",
)

RDT = (
    "Get of Reddit! Get a Life!",
)

HIM = (
    "**Grüßli Müsli!**",
)

CU = (
    "**Ciao Kakao**",
)



@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    print (msg.attachments)
    text = msg.content.lower()
    if msg.author.id == 585381257140240425 and "tft" in text:          
        await msg.channel.send("Moin Felix! Vergiss nicht, hoch zu leveln!")
    if msg.author.id == 275618638860386304 and "nice" in text:          
        await msg.channel.send("Moin Jonas! Und: Nope!")
    if "stuttgart" in text:
        await msg.channel.send (random.choice(STA))
    if "hamburg" in text:
        await msg.channel.send (random.choice(HH))
    if "alkohol" in text:
        await msg.channel.send (random.choice(DRK))
    if "party" in text:
        await msg.channel.send (random.choice(DRK))
    if "trinken" in text:
        await msg.channel.send (random.choice(DRK))
    if "bier" in text:
        await msg.channel.send (random.choice(DRK))
    if "pommes" in text:
        await msg.channel.send (random.choice(PF))
    if "fritten" in text:
        await msg.channel.send (random.choice(PF))
    if "tft" in text:
        await msg.channel.send (random.choice(TFT))
    if "essen" in text:
        await msg.channel.send (random.choice(FOOD))
    if "noice" in text:
        await msg.channel.send (random.choice(NCE))
    if "nice" in text:
        await msg.channel.send (random.choice(NCE))
    if "sehr gut" in text:
        await msg.channel.send (random.choice(NCE))
    if "zocken" in text:
        await msg.channel.send (random.choice(PLY))
    if "spielen" in text:
        await msg.channel.send (random.choice(PLY))
    if "reddit" in text:
        await msg.channel.send (random.choice(RDT))
    if "moin" in text:
        await msg.channel.send (random.choice(HIM))
    if "hallo" in text:
        await msg.channel.send (random.choice(HIM))
    if "bye" in text:
        await msg.channel.send (random.choice(CU))
    if "ciao" in text:
        await msg.channel.send (random.choice(CU))
    if "tschau" in text:
        await msg.channel.send (random.choice(CU))
    if msg.author.id == 321734674177327114:
        await msg.channel.send ("Ciao, Pasci!")
    if msg.author.id == 321734674177327114 and "hamburg":
        await msg.channel.send ("Du wirst hier nur geduldet!")

with open('DiscordBot_MobberKing667_Token.txt') as fp:
    client.run(fp.read().strip())
