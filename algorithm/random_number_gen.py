import random
import os


def random_generator(counter = 500000, start = 1000, end = 9999):

    random_numbers = [random.randint(start, end) for _ in range(counter)]


    return random_numbers



def random_to_file(counter = 500000, start = 1000, end = 9999, file_name = "_number_random.txt"):
    
    random_nums = random_generator(counter, start, end)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = str(counter)+file_name
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, "w") as file:
        for num in random_nums:
            file.write(str(num) + "\n")
    
    return file_path



if __name__ == '__main__':

    print(f"for test generate 3 number betwin 1000 to 9999 : {random_generator(counter=3)}")