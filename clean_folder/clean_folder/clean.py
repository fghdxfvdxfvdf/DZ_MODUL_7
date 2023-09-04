import re
from setuptools import setup

#1
def do_setup(args_dict):
    return setup(**args_dict)
    # print(args_dict)

#2
def do_setup_1(args_dict, requires):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires)
    # print(requires)

#3
def do_setup_2(args_dict, requires, entry_points):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
          entry_points=entry_points
        #   Add the required option
          )
    # print(entry_points)

#4
def is_integer(s):
    # print(s)
    # >>>+34
    # print(type(s))
    # >>><class 'str'> 
    if len(s) == 0:
        return False
    else:
        s = s.strip()
        k = ''
        for i in s:
            if i.find("-") != (-1):
                continue
            if i.find("+") != (-1):
                continue
            else:
                k = k + i
        print("k==", k)
        if k.isdigit():
            return True
        else:
            return False

#5
def capital_text(s):
    s_list = s.split()
    # print("s_list ==", s_list, type(s_list), len(s_list))
    s_list[0] = s_list[0].capitalize()
    # print("s_list ==", s_list, type(s_list), len(s_list))

    s = ''
    for i in range(len(s_list)):
        if s_list[i].find('!') != (-1):
            # print(s_list[i+1].capitalize())
            s_list[i+1] = s_list[i+1].capitalize()
            # print(s_list[i+1])
        if s_list[i].find('?') != (-1):
            # print(s_list[i+1].capitalize())
            s_list[i+1] = s_list[i+1].capitalize()
        if s_list[i].find('.') != (-1):
            # print(s_list[i+1].capitalize())
            s_list[i+1] = s_list[i+1].capitalize()
        # print(s_list[i])
        s = s + s_list[i]
        s = s + ' '
    s = s.strip()
    # print('k ==', k, type(k), len(k))
    return s

#6
def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse == False:
        try:
            if riddle.index(start_letter):
                n = riddle.find(start_letter)
                # print(n)
                # print("riddle[n:n+5] ==", riddle[n:n+word_length], type(riddle[n]))
                return(riddle[n:n+word_length])
        except:
            return ''
    else:
        try:
            if riddle.index(start_letter):
                n = riddle.find(start_letter)
                # print(n)
                print("riddle[n:n-5] ==", riddle[n:n+word_length], type(riddle[n]))
                return(riddle[n:n-word_length:-1])
        except: 
            return ''

#7
def data_preparation(list_data):
    k = []
    for i in list_data:
        # print("i ==", i, len(i))
        if len(i)>2:
            i.remove(max(i))
            i.remove(min(i))
            for j in i:
                k.append(j)
        else:
            for j in i:
                k.append(j)
    k.sort(reverse=True) 
    return k

#8
def token_parser(s):
    tokens = re.findall(r'\d+|[\-\+\*\/\(\)]', s)
    return tokens

#9
def all_sub_lists(data):
    sub_lists = [[]]
    n = len(data)
    for i in range(n):
        # print(data[i])
        for j in range(i + 1, n + 1):
            # print('j ==', j)
            # print['i ==', i]
            sub_lists.append(data[i:j])
        # print("sub_lists ==", sub_lists)
        sub_lists.sort(key=len)
        # print("sub_lists ==", sub_lists)
    return sub_lists

#10
def make_request(keys, values):
    # print(keys)
    # print(values)
    pass
    tuple_res = {}
    if len(keys) == len(values):
        # print(True)
        pass
        for i in range(len(keys)):
                tuple_res.update({keys[i]:values[i]})
        print(tuple_res)
        return tuple_res
    else:
        return {}

#11
telefon_dist = {
    1: [".", ",", "?", "!", ":"],
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"],
    0: [" "]
}

def sequence_buttons(string):
    # Створюємо порожній словник для заміни символів
    map_telefon = {}
    
    # Заповнюємо словник згідно із заданим словником telefon_dist
    for key, val in telefon_dist.items():
        for i in val:
            map_telefon[ord(i)] = str(key) * (val.index(i) + 1)
    
    # Перекладаємо введений текст
    translated_tel = string.upper().translate(map_telefon)
    
    return translated_tel

#12
def file_operations(path, additional_info, start_pos, count_chars):
    # print(path)
    # print(additional_info)
    # print(start_pos)
    # print(count_chars)
        
    
    with open(path, 'a') as file:
        file.write(additional_info)
        with open(path, 'r') as file:
            file.seek(start_pos)
            all_file = file.read(count_chars) 

#13
def get_employees_by_profession(path, profession):
    k =''
    with open(path, 'r') as file:
            # file.seek(start_pos)
            all_file = file.readlines()
            print(all_file, type(all_file))
            for i in all_file:
                if i.find(profession)!=(-1):
                    #  print(i)
                     m = i.split()
                     k += m[0]
                     k += ' '
            k = k.strip()
            # print(k, type(k), len(k))
            return k

#14
def to_indexed(source_file, output_file):
    with open(source_file, 'r') as file:
            
            # all_file = file.readline()
            all_file = file.readlines()
            # all_file = file.read()
            print(all_file, type(all_file), len(all_file))

    with open(output_file, 'w') as file:
        k = ''
        for i in range(len(all_file)): 
            # k += f'{i}: {all_file[i]}'
        # print(k)               
            k = file.write(f'{i}: {all_file[i]}')
        return k          

#15
def flatten(data):
    flattened = []
    for item in data:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

#16
def decode(data):
    result = []

    # перевірка на наявність списку
    if len(data) == 0:
        return []

    def decode_helper(index):
        if index >= len(data):
            return 

        current_char = data[index]
        if isinstance(current_char, str):
            # Якщо поточний символ - рядок, то додайте його до результату
            result.append(current_char)
        elif isinstance(current_char, int):
            # Якщо поточний символ - ціле число, то розмножте попередній символ
            previous_char = result[-1]
            multiplied_chars = previous_char * current_char
            result[-1] = multiplied_chars
            # print("multiplied_chars ==", multiplied_chars)
            # print("previous_char ==", previous_char)

        # Рекурсивно викликайте функцію з наступним індексом
        decode_helper(index + 1)

    decode_helper(0)
    k = ''.join(result)
    
    return list(k)

#17
def encode(message):
    if not message:
        return []

    char = message[0]
    count = 1
    while count < len(message) and message[count] == char:
        count += 1

    return [char, count] + encode(message[count:])