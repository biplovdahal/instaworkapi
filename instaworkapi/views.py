from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from rest_framework.exceptions import APIException
import json




class listings(APIView):
	def get(self, request, *args, **kw):
		filters = request.GET.get('filters','')
		headers = {
		'pragma': 'no-cache',
		'cookie': 'csrftoken=ou2Df6FeCv5a4C4310fum4WcuXLXC3Wb; _ga=GA1.2.170570142.1521337017; optimizelyEndUserId=oeu1521504784553r0.14219540205380743; _gid=GA1.2.1726092097.1521855652; __stripe_mid=ae96b5fd-589e-48a7-b7f9-fc1748e9120e; intercom-id-fz3btoxd=f909eeaf-e4d7-48f9-a728-b87cf5581e16; __stripe_sid=e5cf134a-e278-4119-9e46-7b0cfd519746; _gat=1; amplitude_idinstawork.com=eyJkZXZpY2VJZCI6IjhlM2YxOGJiLTljZmYtNGVhZi1hZjlhLTkwNGFjMTZhMGE3ZlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTUyMjAyMjYxNzU1MiwibGFzdEV2ZW50VGltZSI6MTUyMjAyMzE3MDAyMiwiZXZlbnRJZCI6OSwiaWRlbnRpZnlJZCI6Mywic2VxdWVuY2VOdW1iZXIiOjEyfQ==',
		'dnt': '1',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
		'accept': '*/*',
		'cache-control': 'no-cache',
		'authority': 'instawork.com',
		'x-requested-with': 'XMLHttpRequest',
		'referer': 'https://instawork.com/jobs/San-Francisco-CA/',
		}
		if filters:
			filters = filtersw
		else:
			filters = ''
			
		params = (
			('filters', filters),
			('ne', '37.788760764160884,-122.39031945949705'),
			('sw', '37.76840900250346,-122.44010125881346'),
			('geo', '37.77374349853694,-122.41816110000002'),
			('page', '1'),
			('_', '1522022617182'),
		)

		response = requests.get('https://instawork.com/react/get_jobs', headers=headers, params=params)
		businesses = response.json()['businesses']
		jobs = response.json()['jobs']

		for job in jobs:
			business_dict = businesses[str(job['businessId'])]
			job.update(business_dict)

		with open('output_data_no_duplicate.json','w') as outfile:
			json.dump([i for n, i in enumerate(jobs) if i not in jobs[n + 1:]], outfile,indent=4)
		
		return Response([i for n, i in enumerate(jobs) if i not in jobs[n + 1:]])




