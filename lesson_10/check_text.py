lst = ['Little', 'by', 'little']
my = ['Little', 'by', 'little']

lst = 'Little by little'.split()
my = 'Little by little'.split()


def check_inp(lst, my):
    bed = int()
    index = int()
    # look who is big
    index = len(a_b(lst, my))
    print(index)
    # check
    for word in range(index):  # длина списк (слово)
        try:
            leter_word = a_b(lst[word], my[word])
        except IndexError:
            try:
                leter_word = my[word]
            except IndexError:
                leter_word = lst[word]
        for leter in range(len(leter_word)):  # длина слова (буквы)
            try:
                if(my[word][leter] != lst[word][leter]):
                    bed += 1
                    print('e', end='')
                else:
                    print(leter, end='')
            except IndexError:
                print('t', end='')
                bed += 1
        print(end=' ')
    print(bed)


def a_b(first, second):
    a = len(first)
    b = len(second)
    if a > b:
        return first
    else:
        return second


check_inp(lst, my)
