def main():

    count = 0
    depths = []

    with open('input.txt') as file:
        for line in file:
            depths.append(int(line))
    
    for index in range(len(depths)-1):
        if depths[index] < depths[index+1]:
            count += 1
    
    print(count)

main()