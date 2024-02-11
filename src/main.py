import time
import quote_manager

def main() -> None:
    quote: str = quote_manager.get_quote()
    print(quote)
    user_quote: str = input("\n: ")
    
    accuracy = quote_manager.get_accuracy(user_quote, quote)
    print("Accuracy: " + str(accuracy) + "%")


if __name__ == "__main__":
    main()