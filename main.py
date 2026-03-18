import random
import string

alphanumeric = string.digits + string.ascii_letters
special_chars = string.punctuation

characters = alphanumeric * 3 + special_chars

colors = [
    "\033[91m",
    "\033[92m",
    "\033[93m",
    "\033[94m",
    "\033[95m",
    "\033[96m",
    "\033[97m",
    "\033[90m",
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
    "\033[37m",
]


def main():
    try:
        while True:
            char = random.choice(characters)
            color = random.choice(colors)
            print(f"{color}{char} \033[0m", end="", flush=True)
    except KeyboardInterrupt:
        print("\033[0m")


if __name__ == "__main__":
    main()
