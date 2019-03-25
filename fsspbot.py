import asyncio
import aiohttp
import logging
from aiohttp import web
import json
from lxml  import etree
from settings import config
from models import user_session, fact, get_user_session , add_fact
from aiopg.sa import create_engine
from sqlalchemy.sql import select

f = open('../bot.xml')
cfg = etree.parse(f)
cfg_root = cfg.getroot()
TOKEN = cfg_root.find('tel').text
f = open('scheme.xml')
schema = etree.parse(f)
schema_root = schema.getroot()


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
    async with request.app['db'].acquire() as conn:
        user_session_rec = await  get_user_session(conn, user_id)
    logging.info(user_session_rec)

    a=schema_root.findall('intent')
    fact_name=''
    for i in a:
        if i.attrib['name'] == user_session_rec.intent_name:
            m=i.find('message')
            act=i.attrib['action']
            message_text = m.text
            if 'fact' in i.attrib.keys():
                fact_name=i.attrib['fact']

    if len(fact_name) > 0:
        async with request.app['db'].acquire() as conn:
            fact_value= data['message']['text']
            await  add_fact (conn, user_id,fact_value=fact_value)
        async with request.app['db'].acquire() as conn:
            result = await conn.execute(
                fact.update()
                .returning(*fact.c)
                .where(fact.c.user_id == user_id)
                .where(fact.c.fact_name == fact_name)
                .values(fact_value=fact_value))
    message = {
        'chat_id': data['message']['chat']['id'],
        'text': message_text
    }
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(
            user_session.update()
            .returning(*user_session.c)
            .where(user_session.c.user_id == user_id)
            .values(intent_name=act))
        #user_session_rec = await  get_user_session(conn, user_id)
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
    app['schema'] = schema_root

    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    web.run_app(app, host='localhost', port=8080)



if __name__ == '__main__':
    main()
