# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
import webbrowser
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet

class OpenVideo(Action):
   def name(self):
      return "open_video"

   def run(self, dispatcher, tracker: Tracker, domain):
      video = 'https://youtu.be/Jz28OYKlaLU'
      # dispatcher.utter_message("Opening Video <a href='" + video + "'>click</a>")
      webbrowser.open(video)
      return []


class GetPrice(Action):
   def name(self):
      return "get_price"

   def run(self, dispatcher, tracker: Tracker, domain):
      price = 'price of this product is 100 Rs only'
      dispatcher.utter_message(price)
      return []

class Bargain(Action):
   def name(self):
      return "bargain_price"

   def run(self, dispatcher, tracker: Tracker, domain):
      print("Call Action")
      prices = tracker.latest_message['entities']
      print(prices)

      price = tracker.get_slot('price')
      print(price)

      pric = tracker.latest_message.get("entities")
      print(pric)
      # print(tracker)
      # price = 'price of this product is 100 Rs only'
      # print(price)
      dispatcher.utter_message("price")
      return []