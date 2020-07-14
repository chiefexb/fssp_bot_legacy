import asyncio
from aiohttp import web
from aiohttp import ClientSession
import logging
import json
#import requests

class Web(object):

    async def search (self,data,logger):
    #d = await data

    #'search/physical'
    #-data-urlencode "region=66" \    --data-urlencode "lastname=Иванов" \    
    #--data-urlencode "firstname=Иван" \    --data-urlencode "token=yourapikey"
        
        data['token']=fssp_token
        fssp_url= 'https://api-ip.fssprus.ru/api/v1.0/search/physical'
        headers = {   
            'Content-Type': 'application/json'
        }
        logger.info(data)
        async with ClientSession() as session:
            async with session.get( fssp_url,
                                    data=json.dumps(data),
                                    headers=headers) as resp:
              dd = await resp.json()
              logger.info(dd)
              task = dd ['response']['task'] 
        return task    


    async def webhook (self,request):
        
        data = await request.json()
        user_id = data['message'][ 'from'][ 'id']
        #result = await conn.execute("select * from main where user_id={} and ".format(user_id)  )
        #records = await result.fetchall()
        #if len ( records  ) ==0:
         #    result2 = await conn.execute("insert into main (user_id) values ({})".format(user_id)  )
        #print (data)
        request.app.logger.info(data )
        headers = {
            'Content-Type': 'application/json'
        }
        task='Ждемс'

        dd={'first_name':'Сергей','last_name':'Шило', 'region':'9','date':'15.06.1981'}
        task='Ждемс'
        task = await self.search (dd,  request.app.logger)

        message = {
            'chat_id': data['message']['chat']['id'],
            'text': task                              #data['message']['text']
        }


        async with ClientSession() as session:
            async with session.post(request.app.API_URL % request.app.telegram_token,
                                    data=json.dumps(message),
                                    headers=headers) as resp:
                try:
                    assert resp.status == 200
                except:
                    return web.Response(status=500)
        return web.Response(status=200)
    def configure(self, app): 
        #app.add_routes([web.post('/'+mywebhook, webhook)])
        router = app.router
        router.add_route('POST', '/webhook', self.webhook, name='webhook')
