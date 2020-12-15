#get input


def part1(f):
    goal = 2020
    hashset = set()
    while(1):
        number = f.readline()

        if(number == ''):
            break

        number = int(number)

        if((goal - number) in hashset):
            print(number * (goal - number)) 
        hashset.add(number)
        hashset.add(goal-number)

def part2(f):
    goal = 2020
    subtract = 0
    hashset = set()
    lines = f.read().split("\n")
    lines = lines[:-1]
    lines.sort()

    for i in range(0,len(lines)-2):
        a = int(lines[i])
        start = i + 1
        end = len(lines) - 1
        while (start < end):
            #b = int(lines[start])
            c = int(lines[end])
            b = goal - (a + c)
            if (goal - (a + c) in hashset):
                print(a * b * c)
                           
            elif (a + b + c > 0): 
                end = end - 1
            else:
                start = start + 1
            hashset.add(a)
            hashset.add(c)
                
    
    


f = open("input.txt", "r")
#part1(f)
part2(f)
