def format_name(name):
    names = name.split(" ")
    if (names.__len__() == 1):
        return name
    real_name = "_".join(names[1:])
    return f'{names[0]}.{real_name}'

def get_first_name(name):
    names = name.split(" ")
    return names[0]

if __name__ == '__main__':
    print(format_name("C Varun"))
    print(format_name("C.Chomu"))