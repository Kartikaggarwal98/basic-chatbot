#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
import random

# Create your views here.

VERIFY_TOKEN='7thseptember2016'
PAGE_ACCESS_TOKEN='EAAZAB0AYNpNkBAB5IzMZBTDjZC4peAm861Q4KpzlmdrIff9mjgFtOdRM8V0MyOqS6HD57oqsWZClfVOS7pZB1TUhFBNphjFx9xq6wOPzo0TCelr0roBut5qiZAgaHBh0o8wbEShNYxW0qD2CTn0Nxmfzp3ivUWzcZA3G2IAMYJEpgZDZD'

def post_facebook_message(fbid,message_text):
	post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":message_text}})
	status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
	print status.json()

chatdict={"quotes":["Don't cry because it's over, smile because it happened.",'Be yourself; everyone else is already taken.']
"jokes":['As long as there are tests, there will be prayer in schools.','What did one ocean say to the other ocean? Nothing, they just waved.','A day without sunshine is like, night.','Born free, taxed to death.','For Sale: Parachute. Only used once, never opened.']}
class MyChatBotView(generic.View):
	def get (self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Oops invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		incoming_mesage= json.loads(self.request.body.decode('utf-8'))
		print incoming_mesage

		for entry in incoming_mesage['entry']:
			for message in entry['messaging']:
				print message
				try:
					sender_id = message['sender']['id']
					message_text = message['message']['text']
					print "****",message_text,"****"
					print "------"
					print type(message_text)
					# for key,val in chatdict:
					# 	if message_text in key:
					# 		display_message=val[0]
					# 	else:
					# 		display_message="$$$error$$$"
					post_facebook_message(sender_id,message_text) 
				except Exception as e:
					print e,"*************"
					pass

		return HttpResponse()  

def index(request):
	return HttpResponse('Hello world')
