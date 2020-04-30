''' _________________________________________________________________ 72
3)Создать программу, которая будет выводить информацию о
компьютере на котором запущена (ОС, Платформа, количество ядер)
'''
import platform
def main():
    # ОС, Платформа
    print('_ОС, Платформа_', end = ' : ')
    print(platform.platform(aliased=0, terse=0), end = ' ')
    print(platform.win32_edition())

    # CPU
    print('_CPU_', end = ' : ')
    print(platform.processor())

main()
