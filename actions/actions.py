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
      print(price)
      dispatcher.utter_message(price)
      return []

class Bargain(Action):
   def name(self):
      return "bargain_price"

   def run(self, dispatcher, tracker: Tracker, domain):
      print("Call Bargain Action")
      price = tracker.latest_message['entities']
      print(price)

      # [{'entity': 'price', 'start': 26, 'end': 28, 'confidence_entity': 0.996370196342468, 'value': '80', 'extractor': 'DIETClassifier'}]
      dispatcher.utter_message("price")
      return []