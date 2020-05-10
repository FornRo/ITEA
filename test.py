'''
for i in lst:
    if i == wd:
        cop +=1
    elif i != wd:
        print(str(wd) + str(cop), end='') 
        wd, cop = i, 1
print(str(wd) + str(cop), end='')

# a4b2c1a2
'''

#______________________________________
txt = 'Target'              # [-5 end; 0 start; +5 end]
i = -1                      # індексація від -1 до lenght(str)
while i >= -len(txt) +1 :   # пербор від -1 до -5 
    print(txt[i], end = '') # print 'a' по символьно
    i -= 1                  # -1 >> -2 >> -3 >> -4 >> -5
                            # тежсаме буде
                            # 5 >> 4 >> 3 >> 2 >> 1 >> 0