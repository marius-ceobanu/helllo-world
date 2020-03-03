import sys


def hello_world():
    return "Hello, World!"


def hello(name):
    if name != "":
        return "Hello, " + name + "!"
    else:
        return "Hello, World!"


list = sys.argv


""" def hello_list(y):
    w = print(*y, sep = ", ") """


# print(hello(""))
# print(hello_world())


def print_hello(name):
    print(hello(name))


# name = input("what's your name?")
# print_hello(name)


def main():
    # print_hello(sys.argv[1])
    print("Hello, " + (" ".join(list[1:])) + "!")

  
main()

