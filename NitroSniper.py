import discord
import requests
import re
import os

token = os.getenv("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
	print(f'[ + ] Sniper {client.user.name} Ready')

@client.event
async def on_message(message):
	link = re.search(r'https?://(discord\.com/gifts|discord\.gift)/\w+', message.content)
	if(not link):
		return

	code = link.group().split('/')[-1]

	redeem_link = f'https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem'

	headers = {
	    'authority': 'discord.com',
	    'authorization': token,
	    'accept-language': 'en-US',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.14 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
	    'content-type': 'application/json',
	    'accept': '*/*',
	    'origin': 'https://discord.com',
	    'sec-fetch-site': 'same-origin',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-dest': 'empty',
	}

	data = '{"channel_id":null,"payment_source_id":null}'

	response = requests.post(f'https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem', headers=headers, data=data)

	if response.status_code == 200:
		print(f'[ + ] Congrats! Successfully claimed code {code}')
	else:
		print(f'[ - ] Error claiming code {code}: {response.json()["message"]}')

client.run(token, bot=False)