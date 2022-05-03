# !/usr/bin/env python3

# created by Hertz Antonella
# created on may,3, 2022
# This program oops 3 counter from
# from 200 to 255.


def main():
    # variables
    counter = 0
    counter2 = 0
    counter3 = 0

    # using nested loops to display colors code
    # for every for loop starts from 200 to 256.
    for counter in range(200, 256):
        for counter2 in range(200, 256):
            for counter3 in range(200, 256):
                print("RGB '({0})''({1})''({2})".format(counter, counter2, counter3))


if __name__ == "__main__":
    main()
