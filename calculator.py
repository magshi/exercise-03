"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""


def main():
    while True:
        input = raw_input()
        split_string = input.split()

        if split_string[0] == 'q':
            break

if __name__ == '__main__':
    main()