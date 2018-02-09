#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Wincent Wang'

'''
async web application.
'''

import time
import hashlib
import json

from urllib import request,response,parse
import logging; logging.basicConfig(level=logging.INFO)


def message_notify(content,phone):
	logging.info("message send to %s"%phone)


def mail_notify(content,address):
	logging.info("mail send to %s"%address)


def wechat_notify(content,uid):
	logging.info("wechat send to %s"%uid)

def message_init(content,phone):
	pass

def mail_init(content,address):
	pass

def wechat_init(content,uid):
	pass





