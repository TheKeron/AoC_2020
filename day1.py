import fileinput

num = [*fileinput.input(files = 'inputday1.txt')]

def day1(): 
    for i in range(len(num)):
        for j in range(len(num)):
            for k in range(len(num)):
                if (int(num[i]) + int(num[j]) + int(num[k])) == 2020:
                    print(int(num[i]) * int(num[j]) * int(num[k]))
                    return

day1()      