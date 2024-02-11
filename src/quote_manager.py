import random

# "Be the change that you wish to see in the world."
def get_quote() -> str:
    quotes = list(open("src/quotes.txt", 'r'))
    return quotes[random.randint(0, len(quotes))].strip('\n')


def get_accuracy(input, original) -> float:
    max_chars = len(original)
    final_string = ""

    for x in range(len(input)-1):
        if original[x] == input[x]:
            final_string += input[x]

    return (len(final_string) / max_chars) * 100