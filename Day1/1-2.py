def main():

    count = 0
    depths = []

    with open('input.txt') as file:
        for line in file:
            depths.append(int(line))
    
    for index in range(len(depths)-3):
        window1 = depths[index] + depths[index+1] + depths[index+2]
        window2 = depths[index+1] + depths[index+2] + depths[index+3]
        if window1 < window2:
            count += 1
    
    print(count)

main()