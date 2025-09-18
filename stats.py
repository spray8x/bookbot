def get_num_words(x):
    l = x.split(" ")
    return len(l)
def get_num_char(x):
    x = x.lower().replace(' ', '')
    d = dict()
    for i in x:
        a = 0
        if i.isalpha() == True:
            if i in d.keys():
                a = d[i] + 1
            else:
                a = 1
            d.update({i:a})
        else:
            pass
    return d
def sort_on(items):
    return items["num"]
def create_dict_list(dict):
    l = []
    for i in dict:
        d = {"char" : i, "num" : dict[i]}
        l.append(d)
    l.sort(reverse = True, key=sort_on)
    return l

