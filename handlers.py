#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Wincent Wang'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio



from aiohttp import web

from coreweb import get, post
from apis import Page, APIValueError, APIResourceNotFoundError




@get('/')
def index():
    return {
        '__template__': 'home.html'
    }

