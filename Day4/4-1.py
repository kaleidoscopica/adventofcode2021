def main():

    bingo_order = []
    bingo_data = []
    bingo_cards = []

    with open('input.txt') as file:
        # read in the first line as the bingo order
        bingo_order = file.readline().strip()

        # create a 2nd list of all the bingo card data, just line by line for now
        for line in file:
            if line.strip():
                bingo_data.append(list(map(int, file.readline().split())))
    
    # now convert bingo_order into a proper list (as currently it's just a string of numbers and commas)
    bingo_order = [int(num) for num in bingo_order.split(',')]

    # now remove the blank lines (that turned into empty lists []) in bingo_data
    bingo_data = [item for item in bingo_data if item != []]

    # now, go through all the bingo card data and turn each 5 lines into a bingo card 
    # (the end result is a list of 5x5 matrices)
    while bingo_data:
        bingo_cards.append(bingo_data[0:5])
        del bingo_data[0:5]
    
    print(bingo_order)
    #print(bingo_cards)

    # for each number in the bingo_order list...
    for number in bingo_order:
        # check each bingo card in bingo_cards...
        for i, bingo_card in enumerate(bingo_cards):
            # and check each line of the bingo_card...
            for j, line in enumerate(bingo_card):
                # ... to see if the number called matches a number on any of the lines
                for k, item in enumerate(line):
                    if number in line:
                        bingo_cards[i][j][k] = 'X'

                        is_winning = win_condition(bingo_card)
                        print("Is winning?", is_winning)

    print(bingo_cards)
    print(bingo_order)

main()

def win_condition(bingo_card[]):
    is_winning = False

    horizontal_line = []
    vertical_line = []

    for x in range(0, 5):
        for y in range(0, 5):
            horizontal_line.append(bingo_card[x][y])
        if horizontal_line == ['X', 'X', 'X', 'X', 'X']:
            is_winning = True
    
    for 
    

    return is_winning