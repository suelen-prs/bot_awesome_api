# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "moeda_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        moeda = tracker.get_slot("moeda_dois")
        url = f'https://economia.awesomeapi.com.br/json/last/BRL-{moeda}'
        usuario = tracker.get_slot('usuario')

        json_data = requests.get(url).json()
        nome_moeda = json_data[2].get('url')
        compra = json_data[7].get('url')
        venda = json_data[8].get('url')
        variacao = json_data[6].get('url')
        print(nome_moeda, compra, venda, variacao)
        resp = f'{usuario}, essas são as informações solicitadas: /n {nome_moeda}, {compra}, {venda}, {variacao}'
        


        dispatcher.utter_message(text = resp)

        return [SlotSet("moeda_dois", url)]
