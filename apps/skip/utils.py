from transliterate import translit


def format_and_translit_str(string: str) -> str:
    return translit(string.lower().capitalize(), 'ru')


def get_digits(string: str) -> str:
    digits = ''.join([i for i in string if i.isdigit()])
    return digits
