import time
import quote_manager

def main() -> None:
    while 1: 
        print("\nPress [ENTER] when you're ready or [Q] to quit.")
        answer: str = input()

        if answer.lower() == 'q':
            break

        start = time.time()

        quote: str = quote_manager.get_quote()
        print(quote)
        user_quote: str = input("")

        elapsed = time.time() - start
        
        accuracy: int = quote_manager.get_accuracy(user_quote, quote)
        missed_chars: int = quote_manager.get_missed_chars(user_quote, quote)
        wpm: int = quote_manager.get_wpm(elapsed, quote, user_quote, missed_chars, accuracy)

        print("\nAccuracy: " + str(accuracy) + "%")
        print("WPM: ", wpm)


if __name__ == "__main__":
    main()
