import csv
import argparse


def parse_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, required=True, dest='src')
    parser.add_argument('--dst', type=str, required=True, dest='dst')
    return parser.parse_args()


def process_user(user_data, dst):
    j = 1
    while j < len(user_data):
        current_entry_year = int(user_data[j - 1][3])
        next_entry_year = int(user_data[j][3])
        current_id1 = user_data[j - 1][0]
        current_id2 = user_data[j - 1][1]
        current_id3 = user_data[j - 1][2]

        current_entry_month = int(user_data[j - 1][4])
        next_entry_month = int(user_data[j][4])

        if (current_entry_year == next_entry_year and current_entry_month == next_entry_month - 1) \
                or (current_entry_year == next_entry_year - 1 and current_entry_month == 12 and next_entry_month == 1):
            j += 1
            continue
        else:
            user_data_first_part = [user_data[x] for x in range(0, j)]
            user_data_sec_part = [user_data[x] for x in range(j, len(user_data))]

            if current_entry_month == 12:
                month_to_append = 1
                year_to_append = current_entry_year + 1
            else:
                month_to_append = current_entry_month + 1
                year_to_append = current_entry_year
            new_row = []
            new_row.append(
                [current_id1, current_id2, current_id3, str(year_to_append), str(month_to_append), "0", "0", "0", "0",
                 "0", "0", "0", "0", "0", "0", "0", "0", "0,00", "0,00", "0,00", "0,00"])
            user_data = user_data_first_part + new_row + user_data_sec_part
    print user_data[j - 1][2]
    with open(parse_config().dst, 'a') as file:
        for row in user_data:
            file.write(';'.join([str(elem) for elem in row]))
            file.write('\n')


if __name__ == '__main__':
    with open(parse_config().src, 'rb') as csvfile:
        file = csv.reader(csvfile, delimiter=';')
        rows = [i for i in file]
        i = 1
        dst_list = []
        while i < len(rows) - 1:
            user = []
            # print "new user"
            user.append(rows[i])
            i += 1
            while rows[i - 1][2] == rows[i][2]:
                user.append(rows[i])
                if i < len(rows) - 1:
                    i += 1
                else:
                    break
            process_user(user, dst_list)
