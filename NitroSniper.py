import discord
import requests
import os

token = os.getenv("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
	print('Sniper Ready')

async def on_message():
	if 'discord.gift/' in message.content or 'discord.com/gifts/' in message.content:
		code = message.content.split('/')[-1]
		redeem_link = f'https://discord.com/api/v8/entitlements/gift-codes/{code}/redeem'
		headers = {
        	'Authorization': token,
        	'content-type': 'application/json',
        	'payment_source_id': 'null',
        	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.14 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36'
        }
		response = requests.post(redeem_link, headers=headers)
		print(f'Sniped {code}')
		if response.status_code == 200:
			print(f'Congrats! Successfully sniped {code}')
		else:
			print(f'Failed: {response.text}')

client.run(token, bot=False)