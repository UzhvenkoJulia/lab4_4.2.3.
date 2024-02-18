from utils import is_power_of_five

def main():
    # виклик ф is_power_of_five з utils.py
    number = 125
    if is_power_of_five(number):
        print(f"{number} є степенем 5")
    else:
        print(f"{number} не є степенем 5")

if __name__ == "__main__":
    main()
