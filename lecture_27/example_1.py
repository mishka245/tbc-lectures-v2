from time import sleep


def my_bot():
    print("Hello, I am a bot.")

def main():
    while True:
        my_bot()
        timeout = 20 * 60
        print(f"Sleeping for {timeout} seconds...")
        sleep(timeout)


if __name__ == "__main__":
    main()
