import random

# "Be the change that you wish to see in the world."
def get_quote() -> str:
    quotes = list(open("quotes.txt", 'r'))
    return quotes[random.randint(0, len(quotes)-1)].strip('\n')


def get_accuracy(input, original) -> int:
    max_chars = len(original)
    final_string = ""
    for x in range(len(input)-1):
        if original[x] == input[x]:
            final_string += input[x]

    return int((len(final_string) / max_chars) * 100)


def get_missed_chars(input, original) -> int:
    final_string = ""
    for x in range(len(input)-1):
        if original[x] != input[x]:
            final_string += input[x]
    return final_string


def get_wpm(elapsed_time, input, original, missed_chars, accuracy) -> int:
    return int((len(input) / 5 - len(missed_chars)) / (elapsed_time / 60))
