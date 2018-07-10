#! usr/bin/env python3
# coding: utf-8

import os
import threading

file_path = os.path.dirname(os.path.abspath(__file__))
print(file_path)

import brain
import natural_language_processor

class CLUI(threading.Thread):
    """
    This class will help to trigger threading actions during the process
    Right now this is potentially useless
    """

    def __init__(self,chatbot):
        threading.Thread.__init__(self)
        self.chatbot = chatbot

    def run(self):
        print("============= DEBUT DE LA DISCUSSION ==============")
        self._loop = True
        while self._loop :
            message = input("Please write a message to CHATBOT {} : \n".format(self.chatbot.nom))
            if message == "exit":
                #self.brain.exit()
                self._loop = False
                print("============= FIN  DE  LA DISCUSSION ==============")
                return None

            else :
                print("CHATBOT {} says :".format(self.chatbot.nom), self.chatbot.nlp.answer(message)) #On ne prend qu'un argument

if __name__ == "__main__":

    default_nlp = natural_language_processor.NaturalLanguageProcessor()
    default_nlp.get_connect()

    default_automaton = None
    default_chatbot = brain.Chatbot("David")
    default_chatbot.settings(default_nlp, default_automaton)
    default_clui = CLUI(default_chatbot)
    default_clui.run()





