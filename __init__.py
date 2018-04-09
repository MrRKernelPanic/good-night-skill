# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

# Creating a skill extending MycroftSkill
class GoodNightSkill(MycroftSkill):
    
    def __init__(self):
        super(GoodNightSkill, self).__init__("GoodNightSkill")

    def initialize(self):
        # Creating an intent requiring vocab
        good_night_intent = IntentBuilder("GoodNightIntent"). \
            require("GoodNightKeyword").build()
        # Associating a callback with the Intent
        self.register_intent(good_night_intent, self.handle_good_night_intent)
        
    def handle_good_night_intent(self, message):
        # Sending a command to Mycroft, speak dialog
        self.speak_dialog("goodnight")
        
    def stop(self):
        pass


def create_skill():
    return GoodNightSkill()
