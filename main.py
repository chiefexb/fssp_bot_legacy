import asyncio
from aiohttp import web
from aiohttp import ClientSession
import logging
import json
#import requests
from aiohttp.abc import AbstractAccessLogger
from handler import *
from aiopg.sa import create_engine
from settings import config


class AccessLogger(AbstractAccessLogger):

    def log(self, request, response, time):
        self.logger.info(f'{request.remote} '
                         f'"{request.method} {request.path} '
                         f'done in {time}s: {response.status}'  )

async def init(loop):
    fssp_token: config ['fssp_token']  
    mywebhook='webhook'
    mydict={} #task_status start
    app = web.Application()
    app.mydict =mydict
    from aiopg.sa import create_engine
    app.telegram_token= config ['telegram_token']
    app.API_URL = 'https://api.telegram.org/bot%s/sendMessage'
 
    web_handlers = Web()
    web_handlers.configure(app)

    logging.basicConfig(
        filename='/home/example.log',
        level=logging.DEBUG,
        format="%(asctime)s | %(name)s | %(levelname)s - %(message)s",
    )

    logger = logging.getLogger(__name__)
    ch = logging.StreamHandler()
    logger.addHandler(ch)
    app.logger=logger
    #web.run_app(app)
    handler = app.make_handler()
    srv = await loop.create_server(handler, '127.0.0.1', 8080)
    print('Server started at http://127.0.0.1:8080')


    return srv, app, handler

async def finalize(srv, app, handler):
    sock = srv.sockets[0]
    app.loop.remove_reader(sock.fileno())
    sock.close()

    #await handler.finish_connections(1.0)
    srv.close()
    await srv.wait_closed()
    await app.finish()

def main():
    loop = asyncio.get_event_loop()
    srv, app, handler = loop.run_until_complete(init(loop))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete((finalize(srv, app, handler)))


if __name__ == '__main__':
    main()
