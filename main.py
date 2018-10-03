#!/usr/bin/env python2
from hermes_python.hermes import Hermes
​
def intent_received(hermes, intent_message):
    print('Intent {}'.format(intent_message.intent))
​
    hermes.publish_end_session(intent_message.session_id, None)
​
with Hermes('localhost:1883') as h:
    h.subscribe_intents(intent_received).start()
