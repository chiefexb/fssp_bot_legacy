
import aiohttp
import asyncio

base_url = "https://api-ip.fssprus.ru/api/v1.0"



async def main():
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

    region=''
    lastname=''
    firstname=''
    r_status_code=''
    status=-1
    answ=''
    result=''
    task=''
    token=''

async def getphysical  (user_id):

