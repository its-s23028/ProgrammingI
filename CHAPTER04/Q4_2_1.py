def today(num=0):
    if num == 0:
        day = "今日"
    elif num == 1:
        day = "明日"
    elif num == -1:
        day = "昨日"
    else:
        day = "今日より一日超えて離れた日"
    print(day)


today(-1)
