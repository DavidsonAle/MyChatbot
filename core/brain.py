#! usr/bin/env python3
# coding: utf-8

import natural_language_processor
import logging as lg

"""
======================
Simple Chatbot Project
======================

Version : 1.0
Goal : Running a chatbot in local using NLP interface
"""


class Chatbot :
    """ This class will design the chatbot process by fisrt defining every component and after running each part of the process"""

    def __init__(self, nom = "Uriel"):
        self.nom = nom


    def settings(self, nlp, automaton = None):
        self.nlp = nlp
        self.automaton = automaton
        lg.info("The Chatbot is adjusted")


if __name__ == "__main__":
    default_nlp = natural_language_processor.NaturalLanguageProcessor()
    default_automaton = None
    chatbot = Chatbot()
    chatbot.settings(default_nlp,default_automaton)







