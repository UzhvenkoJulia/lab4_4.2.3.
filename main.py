from utils import is_power_of_five, is_power_of_two

def main():
    number = 16
    if is_power_of_five(number):
        print(f"{number} є степенем 5")
    else:
        print(f"{number} не є степенем 5")

    if is_power_of_two(number):
        print(f"{number} є степенем 2")
    else:
        print(f"{number} не є степенем 2")

if __name__ == "__main__":
    main()
