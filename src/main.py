import time
import random

def main() -> None:
    while 1: 
        print("Press [ENTER] when you're ready or [Q] to quit.")
        answer: str = input()

        if answer.lower() == 'q':
            break

        start = time.time()

        quote: str = get_quote()
        print(quote)
        user_quote: str = input("")

        elapsed = time.time() - start
        
        accuracy: int = get_accuracy(user_quote, quote)
        missed_chars: int = get_missed_chars(user_quote, quote)
        wpm: int = get_wpm(elapsed, quote, user_quote, missed_chars, accuracy)

        print("\nAccuracy: " + str(accuracy) + "%")
        print("WPM: ", wpm)


def get_quote() -> str:
    quotes = list(open("quotes.txt", 'r'))
    return quotes[random.randint(0, len(quotes)-1)].strip('\n')


def get_accuracy(input, original) -> int:
    correct_chars = ""
    
    if len(input) >= len(original):
        for x in range(len(original)):
            if original[x] == input[x]:
                correct_chars += input[x]
    elif len(input) < len(original):
        for x in range(len(input)):
            if original[x] == input[x]:
                correct_chars += input[x]
    if not len(correct_chars) == 0 and not len(input) == 0:
        return int((len(correct_chars) / len(input)) * 100)
    else:
        return 0


def get_missed_chars(input, original) -> int:
    final_string = ""

    if len(input) >= len(original):
        for x in range(len(original)):
            if input[x] != original[x]:
                final_string += input[x]
    elif len(input) < len(original):
        for x in range(len(input)):
            if input[x] != original[x]:
                final_string += input[x]
    return final_string


def get_wpm(elapsed_time, input, original, missed_chars, accuracy) -> int:
    if len(input) > 0:
        total_chars_typed = len(input) if len(input) <= len(original) else len(original)
        return max(int((total_chars_typed / 5 - len(missed_chars)) / (elapsed_time / 60)), 0)
    else:
        return -1


if __name__ == "__main__":
    main()
