s = 53
if s <= 1:
    print("素数じゃない")
else:
    for i in range(2, s):
        if s % i == 0:
            print("素数じゃない")
            break
    else:
        print("素数だ")
