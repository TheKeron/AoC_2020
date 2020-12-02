with open('inputday2.txt', 'r') as infile:
    arr = [*infile.read().splitlines()]

def day2():
    solution = 0

    for i in range(len(arr)):
        counter = 0
        crit = arr[i].split(':')
        string = crit[1]
        number = crit[0].split()
        expected = number[1]
        foo = number[0].split('-')

        for j in range(0, 2):
            if expected == string[int(foo[j])]:
                counter += 1
        
        if counter == 1:
            solution += 1

    print(solution)

day2()
