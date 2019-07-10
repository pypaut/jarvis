from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

### SETTINGS
firefox_path = '/usr/bin/firefox'
chromium_path = '/snap/bin/chromium'
priscille_ig = 'https://www.instagram.com/priscillerzr'


### ENGINE
def Say(message):
    print('>> ' + message)


def MyCommand():
    command = input()
    return command


def CheckCommand(command):
    if 'clean' in command and 'eye' in command:
        webbrowser.get(chromium_path).open(priscille_ig)
        Say('Sure, let me help.')

    elif ('what' in command or 'What') and 'up' in command:
        Say('I\'m fine, what about you?')

    elif 'email' in command:
        Say('I was not configured to send mails')

    else:
        Say('I beg your pardon?')


### LIFE LOOP
Say('Hello, Geoffrey.')
while True:
    CheckCommand(MyCommand())
