import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requests
#import psycopg2
import anvil.http
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_revenue():
  return app_tables.revenue.search()

@anvil.server.callable
def get_weather_data(latitude, longitude):
  resp = anvil.http.request("https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=hourly,daily&appid=%s&units=imperial" 
        % (latitude, longitude, "406842bf5d22b71021767b3a27177afe"),
        json=True)
  # convert timestamp to datetime object
  time = datetime.fromtimestamp(resp['current']['dt'])
  # return time and temperature data
  return {
    'time':time, 
    'temp':resp['current']['temp']
  }

@anvil.server.callable
def get_user_signups():
# Here's some dummy data that you might return from your database, as an example
  return [{'signups': 120, 'date':datetime(2019, 6, 10, 0, 0)}, 
          {'signups': 180, 'date':datetime(2019, 6, 3, 0, 0)}, 
          {'signups': 150, 'date':datetime(2019, 5, 27, 0, 0)}]

@anvil.server.callable
def get_marketing_data():
    # access data on your local machine and return as a Python list
    return [{'strategy':'Strategy A', 'count':200}, 
            {'strategy':'Strategy B', 'count':185}, 
            {'strategy':'Strategy C', 'count':175}]