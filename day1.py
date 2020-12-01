with open('inputday1.txt', 'r') as infile:
    num = [int(x) for x in infile.read().splitlines()]

def day1(): 
    for i in range(len(num)):
        for j in range(len(num)):
            for k in range(len(num)):
                if (num[i] + num[j] + num[k]) == 2020:
                    print(num[i] * num[j] * num[k])
                    return

day1()   