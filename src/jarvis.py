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
        """
        Execute actions depending on @phrase.

        @phrase should always be lower case.
        """
        if not ("jarvis" in phrase):
            return
        words = phrase.split(" ")
        if words[1] == "open":
            name = "".join(words[2:])
            try:
                subprocess.call(name)
                self.say(f"Opening {name}.")
            except FileNotFoundError:
                self.say(f"Could not find {name}.")
                return
        elif any(w in phrase for w in ["hello", "Hello"]):
            self.say(f"Hello, {parameters.NAME}.")
        else:
            self.say("I cannot execute your command yet.")
