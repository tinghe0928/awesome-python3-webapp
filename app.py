#! /usr/bin/env python3

import logging
import asyncio
import os
import time
from datetime import datetime
from aiohttp import web


def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app._make_handler(), '0.0.0.0', 9000)
    logging.info('Server started at http://127.0.0.1:9000')
    return srv


logging.basicConfig(level=logging.INFO)
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
