
import aiohttp
import asyncio

base_url = "https://api-ip.fssprus.ru/api/v1.0"

async def fetch(client):
    async with client.get('http://python.org') as resp:
        assert resp.status == 200
        return await resp.text()

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

async def getphysical  (arg)
    async with session.get(base_url+'/search/physical', params= {'token'    :self.token,
         'region'   :self.region,
         'firstname':self.firstname,
         'lastname' :self.lastname}) as resp
         if resp.status==200:
             await  jsdata=resp.json()
             task=jsdata['response']['task']
             async with aiohttp.ClientSession() as session:
             
async with session.get(base_url+'/status', params= params=
        {'token':self.token,
        'task':self.task})    as resp
         if resp.status==200:
             await  jsdata=resp.json()
             status=jsdata['response']['status']
             