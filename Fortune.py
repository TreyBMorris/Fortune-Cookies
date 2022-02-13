import random

def read_fortune(n):
    with open("fortune.txt", "r") as f:
        lines = f.readlines()
        print("Fortune:" , lines[n])

def lucky_numbers():
    lucky_numbers = [random.randrange(0,99), random.randrange(0,99), random.randrange(1,9), random.randrange(0,99), random.randrange(0,99), random.randrange(0,99)]
    print("Lucky Numbers ", lucky_numbers)


n = random.randint(0,99)

read_fortune(n)
lucky_numbers()
