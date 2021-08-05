import time

def doSomething():
    return 'hello world'

def delayFunction(func, delay):
    time.sleep(delay / 1000) # s / 1000 > ms
    return func()

if __name__ == '__main__':
    assert delayFunction(doSomething, 2000) == 'hello world'
