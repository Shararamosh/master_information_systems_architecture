import re
import random
import string


def generate_password():
    all_symbols = []
    for i in range(3):
        all_symbols.append(random.choice(string.ascii_lowercase))
        all_symbols.append(random.choice(string.ascii_uppercase))
        all_symbols.append(random.choice(string.digits))
        all_symbols.append(random.choice(string.punctuation))
    random.shuffle(all_symbols)
    return "".join(all_symbols)


def generate_email(last_name, first_name, phone_number):
    return last_name+"."+first_name+phone_number+"@sfedu.ru"


original_file_path = "Задание Магистры Datafile.txt"
invalid_file_path = "Задание Магистры Datafile Invalid.txt"
try:
    original_file = open(original_file_path, "r+")
except OSError as exception:
    print(exception)
    exit()
try:
    invalid_file = open(invalid_file_path, "w+")
except OSError as exception:
    print(exception)
    exit()
original_file_lines = original_file.readlines()
original_file.seek(0)
original_file.truncate()
pattern = r", [A-Z]{1}[a-z]+, [A-Z]{1}[a-z]+, \d{7}, [A-Z]{1}[A-Za-z.-]+\n"
pattern_compiled = re.compile(pattern)
original_file.write("EMAIL, NAME, LAST_NAME, TEL, CITY, PASSWORD\n")
for i, line in enumerate(original_file_lines):
    if pattern_compiled.fullmatch(line):
        person_data = line[:-1].split(", ")
        if person_data[3] == "0000000": #Некорректный номер телефона.
            continue
        email = generate_email(person_data[2], person_data[1], person_data[3])
        password = generate_password()
        original_file.write(email+line[:-1]+", "+password+"\n")
    else:
        invalid_file.write(line)
original_file.close()
invalid_file.close()