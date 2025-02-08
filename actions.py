import re
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# OpenWeatherMap API Configuration
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "95b0fd65111d09e4afba92292f61f3d9"  
CITY = "Athens"  

class ActionConfirmOrder(Action):
    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pizza_type = tracker.get_slot("pizza_type")
        pizza_size = tracker.get_slot("pizza_size")

        if not pizza_type:
            dispatcher.utter_message(text="What kind of pizza would you like? (e.g., Margherita, Pepperoni, etc.)")
            return []

        if not pizza_size:
            pizza_size = "regular"

        dispatcher.utter_message(text=f"Your order for a {pizza_size} {pizza_type} pizza has been placed. It will be delivered soon!")
        return []

class ActionTrackOrder(Action):
    def name(self) -> Text:
        return "action_track_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        order_status = "Your order is being prepared and will be delivered in 30 minutes."
        dispatcher.utter_message(text=order_status)
        return []

class ActionModifyOrder(Action):
    def name(self) -> Text:
        return "action_modify_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        modification_details = tracker.get_slot("modification_details")
        pizza_type = tracker.get_slot("pizza_type")
        pizza_size = tracker.get_slot("pizza_size")

        if not pizza_type:
            dispatcher.utter_message(text="Could you please specify the type of pizza you're modifying?")
            return []

        if modification_details:
            cleaned_modification = re.sub(r"^(I want|Can I|I'd like|Please|to add|Add|Remove)", "", modification_details, flags=re.IGNORECASE).strip(" ?.")

            if "remove" in modification_details.lower():
                dispatcher.utter_message(text=f"Your {pizza_size if pizza_size else 'regular'} {pizza_type} pizza has been updated to exclude {cleaned_modification}.")
            else:
                dispatcher.utter_message(text=f"Your {pizza_size if pizza_size else 'regular'} {pizza_type} pizza has been updated to include {cleaned_modification}.")

            return []

        dispatcher.utter_message(text="What changes would you like to make to your order?")
        return []

class ActionCancelOrder(Action):
    def name(self) -> Text:
        return "action_cancel_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your order has been canceled.")
        return []

class ActionCheckStoreHours(Action):
    def name(self) -> Text:
        return "action_check_store_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

    
        store_hours = "Our store is open from 10:00 AM to 11:00 PM every day."
        dispatcher.utter_message(text=store_hours)
        return []

class ActionCheckWeather(Action):
    def name(self) -> Text:
        return "action_check_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            params = {"q": CITY, "appid": WEATHER_API_KEY, "units": "metric"}
            response = requests.get(WEATHER_API_URL, params=params)

            if response.status_code == 200:
                weather_data = response.json()
                weather_condition = weather_data["weather"][0]["description"]
                temperature = weather_data["main"]["temp"]
                dispatcher.utter_message(text=f"The current weather in {CITY} is {weather_condition} with a temperature of {temperature}°C.")
            else:
                dispatcher.utter_message(text="Sorry, I couldn't retrieve the weather data.")
        except Exception:
            dispatcher.utter_message(text="Sorry, I couldn't retrieve the weather data.")

        return []
