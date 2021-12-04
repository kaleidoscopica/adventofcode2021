def main():

    diagnostic_logs = []

    with open('input.txt') as file:
        diagnostic_logs = [ line.strip() for line in file ]

    positional_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for log in diagnostic_logs:
        for x in range(len(positional_list)):
            positional_list[x] += int(log[x])

    gamma = ''
    epsilon = ''

    for position in positional_list:
        if position > 500:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print("gamma rate:   ", gamma)
    print("epsilon rate: ", epsilon)

    power_consumption = int(gamma, 2) * int(epsilon, 2)
    print(power_consumption)
    
main()