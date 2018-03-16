from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from rest_framework.exceptions import APIException





class listings(APIView):
	def get(self, request, *args, **kw):
		city = request.GET.get('city', '')
		filters = request.GET.get('filters','')
		filterDictionary = {
			'assistant_floor_manager':'1',
			'bartender':'2',
			'counter_staff':'3',
			'dishwasher':'4'
		}
		if city:
			city=city
		for key, value in filterDictionary.iteritems():
			if filters == key:
				filters=value
		try:
			response = requests.get('https://instawork.com/react/get_jobs?filters='+filters+'&locality='+city+'&page=1')
			return Response(response)
		except:
			return('internal errror!')




