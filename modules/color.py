
def cprint_upred(text):
    """
    Функция вывода текста красного цвета
    """
    return "\033[1m\033[31m{}\033[0m".format(text)


def cprint_redtext(text):
    """
    Функция вывода в консоль текста красного цвета
    """
    print("\033[1m\033[31m{}\033[0m".format(text))


def cprint_yellow(text):
    """
    Функция вывода текста желтого цвета
    """
    return "\033[33m{}\033[0m".format(text)


def cprint_blue(text):
    """
    Функция вывода текста синего цвета
    """
    return "\033[34m{}\033[0m".format(text)


def cprint_text(text):
    """
    Функция вывода в консоль текста синего цвета
    """
    print("\033[34m{}\033[0m".format(text))