# instaworkapi

python manage.py runserver

I've created one endpoint that lets you query using filters(job position)/city

example:
http://127.0.0.1:8000/?city=San-Francisco-CA&filters=bartender

You need to pass city or filters respectively.

These are the avaiable filters:
'assistant_floor_manager'
'bartender'
'counter_staff'
'dishwasher'
