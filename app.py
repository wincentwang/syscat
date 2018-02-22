#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Wincent Wang'

'''
async web application.
'''
import asyncio, os, json, time

from datetime import datetime
	
from aiohttp import web
from jinja2 import Environment, FileSystemLoader
import logging; logging.basicConfig(level=logging.INFO)
from datetime import datetime
from coreweb import add_routes, add_static
import websockets


def init_jinja2(app, **kw):
	logging.info('init jinja2...')
	options = dict(
	    autoescape = kw.get('autoescape', True),
	    block_start_string = kw.get('block_start_string', '{%'),
	    block_end_string = kw.get('block_end_string', '%}'),
	    variable_start_string = kw.get('variable_start_string', '{{'),
	    variable_end_string = kw.get('variable_end_string', '}}'),
	    auto_reload = kw.get('auto_reload', True)
	)
	path = kw.get('path', None)
	if path is None:
	    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
	logging.info('set jinja2 template path: %s' % path)
	env = Environment(loader=FileSystemLoader(path), **options)
	filters = kw.get('filters', None)
	if filters is not None:
	    for name, f in filters.items():
	        env.filters[name] = f
	app['__templating__'] = env

@asyncio.coroutine
def logger_factory(app, handler):
    @asyncio.coroutine
    def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        return (yield from handler(request))
    return logger


@asyncio.coroutine
def response_factory(app, handler):
    @asyncio.coroutine
    def response(request):
        logging.info('Response handler...')
        r = yield from handler(request)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and t >= 100 and t < 600:
            return web.Response(t)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response


async def echo(websocket, path):
    message = await websocket.recv()
    print('recv', message)

    for x in range(100):
    	await websocket.send(message+str(x))
async def init(loop):
	app = web.Application(loop=loop, middlewares=[
	    logger_factory, response_factory
	])

	init_jinja2(app)
	add_routes(app, 'handlers')
	add_static(app)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9091)
	logging.info('server started at http://127.0.0.1:9091...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))

start_server =websockets.serve(echo, '127.0.0.1', 9092)

loop.run_until_complete(start_server)
loop.run_forever()
