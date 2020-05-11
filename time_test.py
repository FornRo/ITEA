import time
print(time.time())
print(time.ctime())
print(time.localtime())
t = time.strftime('number %d mothe %m', time.localtime())
print(type(t))
