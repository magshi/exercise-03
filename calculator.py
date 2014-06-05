import arithmetic


def main():
    while True:
        input = raw_input()
        split_string = input.split()

        if split_string[0] == 'q':
            break

        else:
            if split_string[0] == '+':
                num1 = int(split_string[1])
                num2 = int(split_string[2])
                print arithmetic.add (num1, num2)

            elif split_string[0] == '-':
                num1 = int(split_string[1])
                num2 = int(split_string[2])
                print arithmetic.subtract (num1, num2)

            elif split_string[0] == '*':
                num1 = int(split_string[1])
                num2 = int(split_string[2])
                print arithmetic.multiply (num1, num2)

            elif split_string[0] == '/':
                num1 = int(split_string[1])
                num2 = int(split_string[2])
                print arithmetic.divide (num1, num2)

            elif split_string[0] == 'square':
                num1 = int(split_string[1])
                num2 = int(split_string[2])
                print arithmetic.square (num1, num2)

            elif split_string[0] == 'cube':
                num1 = int(split_string[1])
                num2 = int(split_string[2])
                print arithmetic.cube (num1, num2)

            elif split_string[0] == 'pow':
                num1 = int(split_string[1])
                num2 = int(split_string[2])
                print arithmetic.power (num1, num2)

            elif split_string[0] == 'mod':
                num1 = int(split_string[1])
                num2 = int(split_string[2])
                print arithmetic.mod (num1, num2)

            else:
                print "I don't understand." 

if __name__ == '__main__':
    main()