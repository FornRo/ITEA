for i in lst:
    if i == wd:
        cop +=1
    elif i != wd:
        print(str(wd) + str(cop), end='') 
        wd, cop = i, 1
print(str(wd) + str(cop), end='')

# a4b2c1a2