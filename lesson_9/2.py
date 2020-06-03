''' _________________________________________________________________ 72
2) Описать класс структуры данных стэк 
(за основу внутри класса использовать список)
'''

class Block:
    def __init__(self, lst):
        self.lst = lst


    def empty_lst(self):
        return len(self.lst) != 0


    def push_lst(self, app):
        self.lst.append(app)
        return self.lst


    def pop_lst(self):
        if self.empty_lst:
            del self.lst[-1]
            return self.lst
        else:
            return 'error'
        

lst = [1, 2, 3]
lst = []
a = Block(lst)

print('element check =', a.empty_lst())

print(a.push_lst(12), 'this push in stek')

a.pop_lst()
print(lst)