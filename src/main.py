import parameters

from jarvis import Jarvis


def main():
    bot = Jarvis()
    bot.say(f"Hello, {parameters.NAME}.")

    isRunning = True
    while isRunning:
        phrase = bot.listen()
        bot.process(phrase)


if __name__ == "__main__":
    main()
