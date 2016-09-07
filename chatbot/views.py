#!/usr/bin/env python
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
# Create your views here.

VERIFY_TOKEN='7thseptember2016'
PAGE_ACCESS_TOKEN='EAAZAB0AYNpNkBAB5IzMZBTDjZC4peAm861Q4KpzlmdrIff9mjgFtOdRM8V0MyOqS6HD57oqsWZClfVOS7pZB1TUhFBNphjFx9xq6wOPzo0TCelr0roBut5qiZAgaHBh0o8wbEShNYxW0qD2CTn0Nxmfzp3ivUWzcZA3G2IAMYJEpgZDZD'
class MyChatBotView(generic.View):
	def get(self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('oops invalid token')

		@method_decorator(csrf_exempt)
		def dispatch(self, request, *args, **kwargs):
			return generic.View.dispatch(self,request, *args, **kwargs)

		def post(self,request, *args, **kwargs):
			incoming_message= json.loads(self.request.body.decode('utf-8'))
			print incoming_message

def index(request):
	return HttpResponse("HELLO WORLD")
