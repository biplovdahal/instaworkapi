from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests


class listings(APIView):
	def get(self, request, *args, **kw):
		city = request.GET.get('city', None)
		response = requests.get('https://instawork.com/react/get_jobs?filters=&locality='+city+'&page=1').json()
		return Response(response)




