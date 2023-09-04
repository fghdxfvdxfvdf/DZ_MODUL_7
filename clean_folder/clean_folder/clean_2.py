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

# capital_text()