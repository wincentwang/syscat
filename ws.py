import asyncio
import websockets
from aiohttp import web

async def echo(websocket, path):
	message = await websocket.recv()
	print('recv', message)
	await websocket.send(message)



async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=script.encode("utf-8"))

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/webscoket', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8002)
    print('Server started at http://127.0.0.1:8001...')
    return srv

start_server = websockets.serve(echo, 'localhost', 8002)
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


