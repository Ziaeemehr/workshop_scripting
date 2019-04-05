num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']

from sys import exit

def nested_loop():
    for number in num_list:
        print(number)
        exit(0)
        for letter in alpha_list:
            print(letter)

if __name__ == '__main__':
    nested_loop()
