import asyncio
import aiohttp
import logging
from aiohttp import web
import json
from lxml  import etree
from settings import config
from models import user_session, fact
from aiopg.sa import create_engine

f = open('../bot.xml')
cfg = etree.parse(f)
cfg_root = cfg.getroot()
TOKEN = cfg_root.find('tel').text
API_URL = 'https://api.telegram.org/bot%s/sendMessage' % TOKEN
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG, filename='/home/bot.log')


async def search_phis(self):

    return 1


async def index(request):
    #name = request.match_info.get('name', "Anonymous")
    text = "Hello"
    return web.Response(text=text)


async def handler(request):
    data = await request.json()
    logging.info(data)
    headers = {
        'Content-Type': 'application/json'
    }
    logging.info(data)
    user_id = data['message']['from']['id']
    intent_name='search'
    async with app['db'].acquire() as conn:
        await conn.execute( user_session.insert().values(user_id=user_id, intent_name=intent_name) )

    message = {
        'chat_id': data['message']['chat']['id'],
        'text': 'Для поиска по базе должников наберите /search'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(API_URL,
                                data=json.dumps(message),
                                headers=headers) as resp:
            try:
                assert resp.status == 200
            except:
                return web.Response(status=500)
    return web.Response(status=200)


async def init_pg(app):
    print ('init')
    conf = app['config']['postgres']
    engine = await create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


def main():
    # loop = asyncio.get_event_loop()
    app = web.Application()  # (loop=loop)
    app['config'] = config
    app.router.add_post('/webhook', handler)
    app.router.add_get('/', index)
    app['sessions'] = {}

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    web.run_app(app, host='localhost', port=8080)



if __name__ == '__main__':
    main()
