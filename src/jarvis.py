import parameters
import subprocess


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
        if any(
            w in phrase for w in ["firefox", "Firefox", "browser", "Browser"]
        ):
            self.say("Opening your web browser.")
            subprocess.call("firefox")
        elif any(w in phrase for w in ["hello", "Hello"]):
            self.say(f"Hello, {parameters.NAME}.")
        else:
            self.say("I cannot execute your command yet.")
