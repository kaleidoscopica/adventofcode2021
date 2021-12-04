def main():

    diagnostic_logs = []

    with open('input.txt') as file:
        diagnostic_logs = [ line.strip() for line in file ]

    oxygen_generator_rating_list = diagnostic_logs.copy()
    co2_scrubber_rating_list = diagnostic_logs.copy()

    for bit in range(12):

        positional_list = [0] * (12 - bit)
        print(positional_list)
        for log in oxygen_generator_rating_list:
            for x in range(len(positional_list)):
                positional_list[x] += int(log[x])
        print(positional_list)
        print(bit)
        print(len(oxygen_generator_rating_list) / 2)

        if positional_list[bit] >= (len(oxygen_generator_rating_list) / 2):
            for log in oxygen_generator_rating_list:
                if log[bit] == '0' and len(oxygen_generator_rating_list) > 1:
                    valueToBeRemoved = log
                    # have to make sure all instances of valueToBeRemoved are removed since there are duplicates
                    oxygen_generator_rating_list = [value for value in oxygen_generator_rating_list if value != valueToBeRemoved]
        else:
            for log in oxygen_generator_rating_list:
                if log[bit] == '1' and len(oxygen_generator_rating_list) > 1:
                    valueToBeRemoved = log
                    oxygen_generator_rating_list = [value for value in oxygen_generator_rating_list if value != valueToBeRemoved]


    for count, position in enumerate(positional_list):

        new_positional_list = [0] * (len(positional_list) - count)
        for log in oxygen_generator_rating_list:
            for x in range(len(new_positional_list)):
                new_positional_list[x] += int(log[x])
        print(new_positional_list)

        if position <= new_positional_list[count]:
            for log in co2_scrubber_rating_list:
                if log[count] == '0' and len(co2_scrubber_rating_list) > 1:
                    valueToBeRemoved = log
                    # have to make sure all instances of valueToBeRemoved are removed since there are duplicates
                    co2_scrubber_rating_list = [value for value in co2_scrubber_rating_list if value != valueToBeRemoved]
        else:
            for log in co2_scrubber_rating_list:
                if log[count] == '1' and len(co2_scrubber_rating_list) > 1:
                    valueToBeRemoved = log
                    co2_scrubber_rating_list = [value for value in co2_scrubber_rating_list if value != valueToBeRemoved]

    print(co2_scrubber_rating_list)
    print(oxygen_generator_rating_list)

    oxygen_generator_rating = int(oxygen_generator_rating_list[0], 2)
    co2_scrubber_rating = int(co2_scrubber_rating_list[0], 2)

    print("oxygen generator rating: ", oxygen_generator_rating)
    print("co2 scrubber rating: ", co2_scrubber_rating)

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print("life support rating: ", life_support_rating)

main()