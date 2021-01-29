import subprocess


def brightness(direction, value):
    """
    Control screen brightness

    @direction : should be up or down
    @value : int
    """
    try:
        assert direction == "up" or direction == "down"
    except AssertionError:
        return 1

    if direction == "up":
        option = "-inc"
    else:
        option = "-dec"
    subprocess.call(["xbacklight", option, value], shell=False)

    return 0
