from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

### SETTINGS
firefox_path = "/usr/bin/firefox"
chromium_path = "/snap/bin/chromium"
priscille_ig = "https://www.instagram.com/priscillerzr"


### DATA
greetings_words = [
    "hi",
    "hello",
    "greetings",
    "good evening",
    "good morning",
]

wattup_words = [
    "how are you",
    "what's up",
    "what",
    "is",
    "up",
]


### ENGINE
def Say(message):
    print(">> " + message)


def MyCommand():
    command = input()
    return command


def Contains(Message, Family):
    """
    Message : String
    Family : String[]

    Return whether Message contains any word from Family or not.
    """
    MessageWords = Message.split()
    for word in MessageWords:
        if word.lower() in Family:
            return True
    return False


def CheckCommand(command):
    if "i need" in command and "clean" in command and "eye" in command:
        Say("Sure, let me help.")
        webbrowser.get(chromium_path).open(priscille_ig)

    elif Contains(command, wattup_words):
        Say("I'm fine, what about you?")

    elif Contains(command, greetings_words):
        Say("Hello!")

    elif "email" in command:
        Say("I was not configured to send emails")

    else:
        Say("I beg your pardon?")


### LIFE LOOP
Say("Hello, Geoffrey.")
while True:
    CheckCommand(MyCommand())
