from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def TalkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

# Listen to commands

def MyCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for you next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '\n')

    # Loop back to continue listening

    except sr.UnknownValueError:
        assistant(MyCommand())

    return command


# If statements for executing commands

def assistant(command):
    if 'I need to clean my eyes' in command:
        firefox_path = '/usr/bin/firefox'
        url = 'https://www.instagram.com/priscillerzr'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        TalkToMe('I am a computer program. Don\'t bother asking.')

    if 'email' in command:
        TalkToMe('I was not configured to send mails')

        #TalkToMe('Who os the recipient')
        #recipient = MyCommand()

#        if 'Priscille' in recipient:
#            TalkToMe('What should I say')
#            content = MyCommand()
#
#            # Init gmail SMTP
#            mail = smtplib.SMTP('smtp.gmail.com', 587)
#
#            # Identify to server
#            mail.ehlo()
#
             # Encrypt
#            mail.starttls()

             # Login
#            mail.login('username', 'password')

            # Send message
#           mail.sendmail('PERSON NAME', 'emailaddress', content)

            # Close connection
#           mail.close()

#            TalkToMe('Email sent')

TalkToMe('I am ready for you command')

while True:
    assistant(MyCommand())
