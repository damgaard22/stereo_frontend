import time

while True:
    time.sleep(0.25)
    f = open('time.txt', 'r')
    print(f.read().strip())
    f.close()
