user_num = None
res = None
while True:
    user_num = input('Enter a number from 1 to 999:\n')
    if user_num.isdigit() and (0 < int(user_num) < 1000):
        if len(user_num) == 1:
            res = int(user_num) ** 2
        elif len(user_num) == 2:
            res = int(user_num[0]) * int(user_num[1])
        else:
            res = int(user_num[::-1])
        break
print(res)
