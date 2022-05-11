#!/usr/bin/env python3

# Created by Devin Jhu
# Created on March 2022
# The loop multiplier


def main():
    # this program shows the sum of number entered
    counter = 1
    sum = 1

    # input
    number = input("Enter number (integer): ")

    # process & output
    try:
        number_int = int(number)
        if number_int > 0:
            while counter <= number_int:
                sum = sum * counter
                counter = counter + 1
            print("{0}! = {1}".format(number_int, sum))
        else:
            print("Not a positive number")
    except Exception:
        print("Not a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
