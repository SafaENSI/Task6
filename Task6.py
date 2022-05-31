# ********working day - Task 6*********** #
import sys
from time import perf_counter


def get_number_of_answers(data):
    questions = []
    for char in data:
        if char not in questions:
            questions.append(char)

    return len(questions)


def read_file(file):
    try:
        # The readlines() method returns a list containing each line in the file as a list item
        with open(file) as f:
            content = f.readlines()
            content = [info.strip() for info in content]

    except:
        print('Error to read file')
        sys.exit()

    return content


if __name__ == "__main__":
    start_timer = perf_counter()

    input_data = read_file("data.txt")
    Sum = 0
    Current_answers = ''
    for line in input_data:
        if line != '':
            Current_answers += line
        else:
            Sum += get_number_of_answers(Current_answers)
            Current_answers = ''
#check the last tine
    Sum += get_number_of_answers(Current_answers)

    print(Sum)
    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)
