from datetime import datetime

def main():

    current_datetime = datetime.now()
    current_time_formatted = current_datetime.strftime("%H:%M:%S")

    print(f"Current Time: {current_time_formatted}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("Press Enter to exit...")