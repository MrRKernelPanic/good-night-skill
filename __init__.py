# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

# Creating a skill extending MycroftSkill
class good-night-skill(MycroftSkill):
    
    def __init__(self):
        super(good-night-skill, self).__init__("good-night-skill")

    def initialize(self):
        # Creating an intent requiring vocab
        good-night = IntentBuilder("good-nightIntent")
                           .require("good-night").build()
        # Associating a callback with the Intent
        self.register_intent(good-night, self.handle_good-night)
        
    def handle_good-night(self):
        # Sending a command to Mycroft, speak dialog
        self.speak_dialog("good-night")
        
    def stop(self):
        pass


def create_skill():
    return good-night-skill()
