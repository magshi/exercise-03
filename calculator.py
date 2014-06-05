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

        else:
            if split_string[0] == '+':
                return "Someday I will know how to add!"
            elif split_string[0] == '-':
                return "Someday I will know how to subtract!"
            elif split_string[0] == '*':
                return "Someday I will know how to multiply!"
            elif split_string[0] == '/':
                return "Someday I will know how to divide!"
            elif split_string[0] == 's':
                return "Someday I will know how to square!"
            elif split_string[0] == 'c':
                return "Someday I will know how to cube!"
            elif split_string[0] == 'p':
                return "Someday I will know how to do powers!"
            elif split_string[0] == 'm':
                return "Someday I will know how to do modulus!"
            else:
                print "I don't understand." 

if __name__ == '__main__':
    main()