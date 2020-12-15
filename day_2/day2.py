
def part1():
    f = open("input.txt", "r")

    # 0,2,4? 4 since the space is there. 
    # so for each line we need index 0, 2, 4 and then everything after the :
    string = f.readline().rstrip('\r\n')

    good = 0

    while(string):
        parts = string.split(' ')
        low = parts[0].split('-')[0]
        high = parts[0].split('-')[1]
        letter = parts[1][0]

        count = parts[2].count(letter)
        if (count >= int(low) and count <= int(high)):
            good += 1
        string = f.readline().rstrip('\r\n')
    print(good)

def part2():
    f = open("input.txt", "r")

    string = f.readline().rstrip('\r\n')

    good = 0

    while(string):
        parts = string.split(' ')
        spot1 = parts[0].split('-')[0]
        spot2 = parts[0].split('-')[1]
        letter = parts[1][0]

        if (parts[2][int(spot1)-1] == letter or parts[2][int(spot2)-1] == letter):
            good += 1
            if (parts[2][int(spot1)-1] == letter and parts[2][int(spot2)-1] == letter):
                good -= 1
        string = f.readline().rstrip('\r\n')
    print(good)




part1()
part2()
