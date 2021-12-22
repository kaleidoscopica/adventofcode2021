def main():
    bingo_order = []
    bingo_data = []
    bingo_card_list = []
    bingo_cards = []

    with open('input.txt') as file:
        # read in the first line as the bingo order
        bingo_order = file.readline().strip()
        # create a 2nd list of all the bingo card data, just line by line for now
        bingo_data = file.read().splitlines()

    # convert bingo_order into a proper list (as currently it's just a string of numbers and commas)
    bingo_order = [int(num) for num in bingo_order.split(',')]

    # remove the blank lines (that turned into empty lists []) in bingo_data, and the leading whitespace
    bingo_data = [item.lstrip() for item in bingo_data if item != '']

    # go through each list of space-separated numbers in the original list and split them to a list of bingo cards
    # then convert each to an int instead of a string
    for item in bingo_data:
        bingo_card_list.append(item.split())
    bingo_card_list = [[int(num) for num in line] for line in bingo_card_list]

    # now, go through all the bingo card data and turn each 5 lines into a bingo card 
    # (the end result is a list of 5x5 matrices)
    while bingo_card_list:
       bingo_cards.append(bingo_card_list[0:5])
       del bingo_card_list[0:5]

    winning_bingo_cards = []
    last_winning_card = []

    print("Let's play bingo!")
    print()
    print("......")
    print()

    is_winning = False
    # for each number in the bingo_order list...
    for number in bingo_order:
        print(len(bingo_cards))
        # check each bingo card in bingo_cards...
        for i, bingo_card in enumerate(bingo_cards):
            # and check each line of the bingo_card...
            for j, line in enumerate(bingo_card):
                # ... to see if the number called matches a number on any of the lines
                for k, item in enumerate(line):
                    if line[k] == number:
                        bingo_cards[i][j][k] = 'X'

                        is_winning = win_condition(bingo_card)
                        if is_winning == True:
                            print("the following bingo card won!")
                            print(print_bingo_card(bingo_card))
                            print("winning bingo number:", number)
                            winning_bingo_number = number
                            del bingo_cards[i]
                            # if the length of the bingo_cards list is 1, this will be the last winning card
                            if len(bingo_cards) == 1 and len(last_winning_card) == 0:
                                last_winning_card.append(bingo_card)
                                print(number)
                                break
                        if len(bingo_cards) == 1 and len(last_winning_card) == 0:
                            break
    
    print(bingo_cards)

    print(len(winning_bingo_cards))
    print()
    print(last_winning_card)
                        

    # Calculate the sum of non-marked squares on the last winning bingo card
    sum = 0
    for x in range(0, 5):
        for y in range(0, 5):
            if last_winning_card[0][x][y] != 'X':
                sum += last_winning_card[0][x][y]
    
    final_score = sum * winning_bingo_number
    print("sum of non-marked items on the last winning bingo card:", sum)
    print("final score:", final_score)


def print_bingo_card(bingo_card):
    for x in range(0, 5):
        print(bingo_card[x])


def win_condition(bingo_card):
    is_winning = False

    # Checking to see if a horizontal line has hit bingo
    for x in range(0, 5):

        horizontal_line = []
        for y in range(0, 5):
            horizontal_line.append(bingo_card[x][y])
        if horizontal_line == ['X', 'X', 'X', 'X', 'X']:
            is_winning = True
    
    # Checking to see if a vertical line has hit bingo
    for y in range(0, 5):

        vertical_line = []
        for x in range(0, 5):
            vertical_line.append(bingo_card[x][y])
        if vertical_line == ['X', 'X', 'X', 'X', 'X']:
            is_winning = True

    return is_winning


main()