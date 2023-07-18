import random

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
smp = random.sample(num, k=4)
num4 = "".join(smp)
while True:
    val = input("2345")
    if val == num4:
        print("ok")
        break
    else:
        print("ng")
