def main():

    diagnostic_logs = []

    with open('input.txt') as file:
        diagnostic_logs = [ line.strip() for line in file ]

    oxygen_generator_rating_list = diagnostic_logs.copy()
    co2_scrubber_rating_list = diagnostic_logs.copy()

    # Finding the (binary) oxygen generator rating
    for bit in range(12):

        count_zeroes = 0
        count_ones = 0

        for log in oxygen_generator_rating_list:
            if log[bit] == '0':
                count_zeroes += 1
            elif log[bit] == '1':
                count_ones += 1

        print("bit", bit, "zeroes:", count_zeroes)
        print("bit", bit, "ones:", count_ones)

        if count_zeroes <= count_ones and len(oxygen_generator_rating_list) > 1:
            for log in oxygen_generator_rating_list:
                if log[bit] == '0':
                    valueToBeRemoved = log
                    # have to make sure all instances of valueToBeRemoved are removed since there are duplicates
                    oxygen_generator_rating_list = [value for value in oxygen_generator_rating_list if value != valueToBeRemoved]
        elif count_zeroes > count_ones and len(oxygen_generator_rating_list) > 1:
            for log in oxygen_generator_rating_list:
                if log[bit] == '1':
                    valueToBeRemoved = log
                    oxygen_generator_rating_list = [value for value in oxygen_generator_rating_list if value != valueToBeRemoved]

    # Finding the (binary) CO2 scrubber rating
    for bit in range(12):

        count_zeroes = 0
        count_ones = 0

        for log in co2_scrubber_rating_list:
            if log[bit] == '0':
                count_zeroes += 1
            elif log[bit] == '1':
                count_ones += 1

        print("bit", bit, "zeroes:", count_zeroes)
        print("bit", bit, "ones:", count_ones)

        if count_zeroes > count_ones and len(co2_scrubber_rating_list) > 1:
            for log in co2_scrubber_rating_list:
                if log[bit] == '0':
                    valueToBeRemoved = log
                    # have to make sure all instances of valueToBeRemoved are removed since there are duplicates
                    co2_scrubber_rating_list = [value for value in co2_scrubber_rating_list if value != valueToBeRemoved]
        elif count_zeroes <= count_ones and len(co2_scrubber_rating_list) > 1:
            for log in co2_scrubber_rating_list:
                if log[bit] == '1':
                    valueToBeRemoved = log
                    co2_scrubber_rating_list = [value for value in co2_scrubber_rating_list if value != valueToBeRemoved]


    oxygen_generator_rating = int(oxygen_generator_rating_list[0], 2)
    co2_scrubber_rating = int(co2_scrubber_rating_list[0], 2)

    print("Oxygen generator rating: ", oxygen_generator_rating)
    print("CO2 scrubber rating: ", co2_scrubber_rating)

    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    print("Life support rating: ", life_support_rating)

main()