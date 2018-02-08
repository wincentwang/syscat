# -*- coding: utf-8 -*-
from io import StringIO
import asyncio
import websockets
import psutil
import time
import os.path
import asyncio
import logging
import argparse
import websockets
from collections import deque
from urllib.parse import urlparse, parse_qs

 
async def echo(websocket, path):
    message = await websocket.recv()
    print('recv', message)
    yield from websocket.send(message)

start_server = websockets.serve(echo, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()




def getSysInfo():
	f = StringIO()
	f.write("-----------------------------CPU INFO---------------------------------<br>")
	f.write("CPU LOGICAL:%d <br>"%psutil.cpu_count())
	f.write("CPU PHYSIC:%d <br>"%psutil.cpu_count(logical=False))
	f.write("-----------------------------MEM INFO---------------------------------<br>")
	f.write("PHYSIC MEM<br>")
	f.write("Total: %.1f G<br>"%(psutil.virtual_memory().total/1024/1024/1024))
	f.write("Available:%.1f G<br>"%(psutil.virtual_memory().available/1024/1024/1024))
	f.write("Percent:%.1f %%<br>"%psutil.virtual_memory().percent)
	f.write("Used:%.1f G<br>"%(psutil.virtual_memory().used/1024/1024/1024))
	f.write("Free:%.1f G<br>"%(psutil.virtual_memory().free/1024/1024/1024))
	f.write("Active:%.1f G<br>"%(psutil.virtual_memory().total/1024/1024/1024))
	f.write("Inactive:%.1f G<br>"%(psutil.virtual_memory().total/1024/1024/1024))
	f.write("Wired:%.1f G<br>"%(psutil.virtual_memory().total/1024/1024/1024))
	f.write("SWAP MEM<br>")
	f.write("Total:%.1f G<br>"%(psutil.virtual_memory().total/1024/1024/1024))
	f.write("Used:%.1f G<br>"%(psutil.virtual_memory().used/1024/1024/1024))
	f.write("Percent:%.1f %%<br>"%(psutil.virtual_memory().percent))
	f.write("Free:%.1f G<br>"%(psutil.virtual_memory().free/1024/1024/1024))
	f.write("Sin:%.1f G<br>"%(psutil.virtual_memory().total/1024/1024/1024))
	f.write("Sout:%.1f G<br>"%(psutil.virtual_memory().total/1024/1024/1024))
	f.write("Total:%.1f G<br>"%(psutil.virtual_memory().total/1024/1024/1024))
	f.write("-----------------------------DISK INFO---------------------------------<br>")
	f.write("Total:%.1f G<br>"%(psutil.disk_usage('/').total/1024/1024/1024))
	f.write("Used:%.1f G<br>"%(psutil.disk_usage('/').used/1024/1024/1024))
	f.write("Free:%.1f G<br>"%(psutil.disk_usage('/').free/1024/1024/1024))
	f.write("Percent:%.1f %%<br>"%psutil.disk_usage('/').percent)
	return f

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    f=getSysInfo()
    return [f.getvalue().encode('utf-8')]

httpd = make_server('', 8001, application)
print('Serving HTTP on port 8001...')
httpd.serve_forever()