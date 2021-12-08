def main():

    bingo_order = []
    bingo_cards = []

    with open('input.txt') as file:
        bingo_order = file.readline().strip()
        bingo_cards = [ line.strip() for line in file ]
    
    valueToBeRemoved = ''
    bingo_cards = [value for value in bingo_cards if value != valueToBeRemoved]
    
    print(bingo_cards)

main()