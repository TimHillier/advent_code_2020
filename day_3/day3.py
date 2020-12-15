def part1():
    f = open('input.txt','r')

    current_x= 0
    current_y = 0
    change_x = 3
    change_y = 1
    trees_hit = 0

    current_line = f.readline().rstrip('\n')

    while(current_line):
        if(current_x >= len(current_line)):
            current_x = current_x % len(current_line)
        if(current_line[current_x] == '#'):
            trees_hit += 1
        current_x = current_x + change_x
        current_line = f.readline().rstrip('\n')
    print(trees_hit)

def part2():

    current_y = 0
#    change_x = 3
    change_y = 1
    product = 1
    current = 0
    


    x_array = [1,3,5,7,1]
    y_array = [1,1,1,1,2] # the only one I hae to worry about is the 2.
    for change_x in x_array:
        f = open('input.txt','r') #first line
        trees_hit = 0
        current_x= 0
        change_y = y_array[current]
        current_line = f.readline().rstrip('\n')
        while(current_line):
            if(current_x >= len(current_line)):
                current_x = current_x % len(current_line)
            if(current_line[current_x] == '#'):
                trees_hit += 1
            current_x = current_x + change_x
            current_line = f.readline().rstrip('\n')
            if(change_y > 1):
                current_line = f.readline().rstrip('\n')

        current += 1
        product *= trees_hit
        print(trees_hit)
    print(product)

part2()
