class Jarvis:
    def __init__(self):
        pass

    def say(self, phrase):
        print('"' + phrase + '"')

    def listen(self):
        phrase = input("> ")
        return phrase

    def process(self, phrase):
        if not ("jarvis" in phrase or "Jarvis" in phrase):  # Not for me
            self.say("I do nothing.")
            return
        self.say("I cannot execute your command yet.")
