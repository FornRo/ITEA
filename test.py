'''
'''

#______________________________________
txt = 'Target'              # [-5 end; 0 start; +5 end]
i = -1                      # індексація від -1 до lenght(str)
while i >= -len(txt) +1 :   # пербор від -1 до -5 
    print(txt[i], end = '') # print 'a' по символьно
    i -= 1                  # -1 >> -2 >> -3 >> -4 >> -5
                            # тежсаме буде
                            # 5 >> 4 >> 3 >> 2 >> 1 >> 0