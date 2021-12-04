def main():

    instructions = []

    with open('input.txt') as file:
        instructions = [ line.strip() for line in file ]
        
    horizontal = 0
    depth = 0
    aim = 0

    for instruction in instructions:
        if instruction[0] == 'f':
            horizontal += int(instruction[-1])
            depth += aim * int(instruction[-1])
        elif instruction[0] == 'u':
            aim -= int(instruction[-1])
        elif instruction[0] == 'd':
            aim += int(instruction[-1])

    total = horizontal * depth
    print(total)
    
main()