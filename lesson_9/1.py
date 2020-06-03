''' _________________________________________________________________ 72
1) Описать класс прямоугольника, конструктор в качестве аргументов должен
принимать размеры сторон, класс должен иметь методы возвращающие 
площадь, периметр прямоугольника. Объект прямоугольника должен корректно
отображаться в функции print.
'''

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def perimeter(self):
        return (self.x + self.y) * 2


    def area(self):
        return self.x * self.y

s = Block(5, 10)
b = Block(15, 20)

print(f'P={s.perimeter()} S={s.area()}')

print(f'P={b.perimeter()} S={b.area()}')