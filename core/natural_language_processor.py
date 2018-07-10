# coding: utf-8

import json
from settings import *
import logging as lg

lg.basicConfig(level=lg.INFO)
try :
    import apiai
    lg.info("Connection to library DialogFlow : ok")
except ImportError :
    raise lg.warning("The library is not reachable")


class NaturalLanguageProcessor:
    """
    This class manage the treatment of message from users
    """

    def __init__(self):
        self.CLIENT_ACCESS_TOKEN = None
        self.request = None

    def get_connect(self):
        global DIALOGFLOW_TOKEN
        print(DIALOGFLOW_TOKEN)
        try :
            self.CLIENT_ACCESS_TOKEN = DIALOGFLOW_TOKEN
            self._processor = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
            self.request = self._processor.text_request()
            lg.info("Connection to DialogFlow : ok")
        except Exception:
            raise lg.warning("The connection failed : Please insure the internet connection is working or the credentials are correct")

    def treat_message(self, message, user_id = "Guest", lang = 'fr', full = False):
        self.request.lang = lang
        self.request.session_id = user_id
        self.request.query = message

        try :
            response_json = self.request.getresponse()
            response_dict = json.loads(response_json.read().decode('utf-8'))

            intent = response_dict["result"]["metadata"]["intentName"]
            score = response_dict["result"]["score"]
            answer = response_dict["result"]["fulfillment"]["speech"]

            if full :
                return response_dict
            else :
                return {"intent" : intent,"score" : score,"nlp_answer" : answer}


        except Exception :
            raise Warning("""The treatment has failed : Please insure the content is valid :\n>>{}""".format(message))

    def answer(self, message, user_id = "Guest", lang = 'fr', full = False):
        processor_result = self.treat_message(message,user_id,lang,full)
        if not full :
            intent = processor_result["intent"]
            score = processor_result["score"]
            return """J'ai détecté l'intention suivante "{}" avec un score de : {}""".format(intent, score)

if __name__ == "__main__" :
    default_processor = NaturalLanguageProcessor()
    default_processor.get_connect()

    default_message = "Hello World"
    print(self.answer(default_message))







