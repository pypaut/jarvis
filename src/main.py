import parameters

from jarvis import Jarvis


def main():
    """
    Basic loop, listen and execute.
    """
    bot = Jarvis()
    bot.say(f"Hello, {parameters.NAME}.")

    is_running = True
    while is_running:
        phrase = bot.listen()
        bot.process(phrase)


if __name__ == "__main__":
    main()
