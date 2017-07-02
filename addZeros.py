import csv
import argparse


def parse_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, required=True, dest='src')
    parser.add_argument('--dst', type=str, required=True, dest='dst')
    return parser.parse_args()


def write_to_file(user_data):
    with open(parse_config().dst, 'a') as file:
        for row in user_data:
            file.write(';'.join([str(elem) for elem in row]))
            file.write('\n')


def process_user(user_data):
    required = [[2014, 1], [2014, 2], [2014, 3], [2014, 4], [2014, 5], [2014, 6], [2014, 7], [2014, 8], [2014, 9],
                [2014, 10], [2014, 11], [2014, 12],
                [2015, 1], [2015, 2], [2015, 3], [2015, 4], [2015, 5], [2015, 6], [2015, 7], [2015, 8], [2015, 9],
                [2015, 10], [2015, 11], [2015, 12],
                [2016, 1], [2016, 2], [2016, 3], [2016, 4], [2016, 5], [2016, 6], [2016, 7], [2016, 8], [2016, 9],
                [2016, 10]]
    j = 0
    index = 0
    while index < len(required):
        #print index, user_data[j]
        #print j
        if len(user_data) - 1 < j:
            current_entry_year = 0
            current_entry_month = int(user_data[1][4])
            current_id1 = user_data[1][0]
            current_id2 = user_data[1][1]
            current_id3 = user_data[1][2]
        else:
            current_entry_year = int(user_data[j][3])
            current_entry_month = int(user_data[j][4])
            current_id1 = user_data[j][0]
            current_id2 = user_data[j][1]
            current_id3 = user_data[j][2]


        if current_entry_year == required[index][0] and current_entry_month == required[index][1]:
            j += 1
            index += 1
            continue
        else:
            user_data_first_part = [user_data[x] for x in range(0, j)]
            user_data_sec_part = [user_data[x] for x in range(j, len(user_data))]

            month_to_append = required[index][1]
            year_to_append = required[index][0]

            new_row = []
            new_row.append(
                [current_id1, current_id2, current_id3, str(year_to_append), str(month_to_append), "0", "0", "0", "0",
                 "0", "0", "0", "0", "0", "0", "0", "0", "0,00", "0,00", "0,00", "0,00"])
            user_data = user_data_first_part + new_row + user_data_sec_part
            #print index, user_data


    print "Loop iters: " + str(j)
    write_to_file(user_data)

if __name__ == '__main__':
    with open(parse_config().src, 'rb') as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        rows = [i for i in file]
        i = 1
        while i < len(rows) - 1:
            user = []
            #print "new user"
            user.append(rows[i])
            i += 1
            while rows[i - 1][2] == rows[i][2]:
                user.append(rows[i])
                if i < len(rows) - 1:
                    i += 1
                else:
                    break
            # print user
            process_user(user)
