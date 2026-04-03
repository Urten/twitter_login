from twitter_login import Client
from dotenv import load_dotenv
import time
import os
import json
from twitter_login.castle_token.token import CastleToken

load_dotenv()

USERNAME=os.getenv('USERNAME')
EMAIL=os.getenv('EMAIL')
PASSWORD=os.getenv('PASSWORD')
CUID=os.getenv('CUID')

if USERNAME is None or EMAIL is None or PASSWORD is None:
    raise Exception('Please set USERNAME, EMAIL and PASSWORD environment variables')



init_time = int(time.time() * 1000)


castle_token = CastleToken(init_time=init_time, cuid=CUID)



client = Client()
async def test_flow():
    # await client.login(
    #     user_identifiers=[USERNAME, EMAIL],
    #     password=PASSWORD,
    #     cookies_file='cookies.json',
    #     castle_fingerprint=castle_token
    # )
    
    with open('mookies.json', encoding='utf-8') as f:
        cookies_json = json.load(f)
    
    
    await client.login_with_cookies(cookies=cookies_json)
    
    client.save_cookies('cookies.json')
    
    tweet = await client.create_tweet(text="Hello Family")
    print(tweet.text)
    
import asyncio
asyncio.run(test_flow())