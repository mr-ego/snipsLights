#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
​
def intent_received(hermes, intent_message):
    result_sentence = "hello in this lonely beach"
    hermes.publish_end_session(intent_message.session_id, result_sentence)

with Hermes('localhost:1883') as h:
    h.subscribe_intents(intent_received).start()
