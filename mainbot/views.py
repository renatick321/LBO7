#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
import telebot
from time import sleep

TOKEN = '1221596086:AAF9ZAqadOm27uNAPVZ8VMHkywJWLmol2Ac'
tbot = telebot.TeleBot(TOKEN)
tbot.remove_webhook()
sleep(3)
tbot.set_webhook(url="http://renatick321.pythonanywhere.com/bot/1221596086:AAF9ZAqadOm27uNAPVZ8VMHkywJWLmol2Ac", 
				certificate=open("/home/renatick321/LBO/mainbot/YOURPEM.cer", 'r'))
# For free PythonAnywhere accounts
# tbot = telebot.TeleBot(TOKEN, threaded=False)

@csrf_exempt
def index(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        tbot.process_new_updates([update])
        return HttpResponse("")
    else:
        raise PermissionDenied


@tbot.message_handler(content_types=["text"])
def get_okn(message):
    tbot.send_message(message.chat.id, "Hello, bot!")