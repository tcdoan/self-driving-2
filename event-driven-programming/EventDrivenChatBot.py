from datetime import datetime
import time

class EventDrivenChatBot:

    def __init__(self):
        self.accepted_messages = {}
        self.birth_time = datetime.now()
        self.first_age_request = True;
        self.register_callback("hi", self.respond_to_greeting)
        self.register_callback("bye", self.respond_to_departure)
        self.register_callback("age?", self.respond_to_age_request)
        self.register_callback("age?", self.respond_to_age_request_detailed)
        
    def register_callback(self, message, callback):
        if message not in self.accepted_messages:
            self.accepted_messages[message] = []
        self.accepted_messages[message].append(callback)

    def respond_to_greeting(self):
        print("Hello!")

    def respond_to_departure(self):
        print("Nice chatting with you!")
    
    def respond_to_age_request(self):
        if self.first_age_request:
            age = datetime.now() - self.birth_time
            print("I am ", age.seconds, "seconds old.")        

    def respond_to_age_request_detailed(self):
        if not self.first_age_request:
            age = datetime.now() - self.birth_time
            print("Technically,  I'm ", age.seconds, "seconds and", age.microseconds, "microseconds old.")
        self.first_age_request = False

    def handle_message(self, message):
        if message not in self.accepted_messages:
            print("sorry, I don't understand", message)
        else:
            callbacks = self.accepted_messages[message]
            for callback in callbacks:
                callback()
        
bot = EventDrivenChatBot()
bot.handle_message("hi")
time.sleep(2.2)
bot.handle_message("age?")
bot.handle_message("age?")
bot.handle_message("age?")
bot.handle_message("bye")