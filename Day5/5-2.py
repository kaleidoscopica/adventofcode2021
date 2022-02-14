def main():
    steam_vent_data = []
    steam_vents = [[0 for col in range(1000)] for row in range(1000)]   # initialize a 1000x1000 array of zeroes

    with open('input.txt') as file:
        # read in all lines as the steam vent data; replace the " -> " with ":"
        # (for readability, I like it better)
        steam_vent_data = file.read().replace(" -> ",":").splitlines()

    for index, vent in enumerate(steam_vent_data):
        x1, y1, x2, y2 = calculate_x_y(vent)
        if x1 != x2 and x2 > x1:
            x_list = list(range(x1, x2+1))   # list of all values of x the vent spans
        elif x1 != x2 and x1 > x2:
            x_list = list(range(x2, x1+1))
        if y1 != y2 and y2 > y1:
            y_list = list(range(y1, y2+1))   # list of all values of y the vent spans
        elif y1 != y2 and y1 > y2:
            y_list = list(range(y2, y1+1))
        print("For steam vent", index, ".....")
        print("x1:", x1, "x2:", x2)
        print("y1:", y1, "y2:", y2)
        print("x_list is therefore:", x_list)
        print("y_list is therefore:", y_list)

        # Only do horizontal and vertical vents.
        # I.e., only mark steam vents if either x or y change, but not both.
        if x1 == x2:
            # Mark vertical vents by starting at the column with index y1
            # Increment the value in steam_vents by 1 for each occurrence
            for value in y_list:
                steam_vents[x1][value] += 1

        elif y1 == y2:
            # Mark horizontal vents by starting at the row at index x1 in steam_vents 
            # Increment the value in steam_vents by 1 for each occurrence
            for value in x_list:
                steam_vents[value][y1] += 1
    
    overlap_points = 0
    for i, row in enumerate(steam_vents):
        for j, column in enumerate(row):
            if steam_vents[i][j] >= 2:
                overlap_points += 1
    print(overlap_points)


def calculate_x_y(steam_vent_data):

    import re

    x1 = steam_vent_data.split(',')[0]   # find the first ([0]) instance of text split on the comma
    y1 = re.findall(r',(.+?):', steam_vent_data)[0]   # find the text between , and :
    x2 = re.findall(r':(.+?),', steam_vent_data)[0]   # find the text between : and ,
    y2 = steam_vent_data.rpartition(',')[-1]   # find the last occurrence of text after the comma
    return int(x1), int(y1), int(x2), int(y2)   # return all as ints


main()