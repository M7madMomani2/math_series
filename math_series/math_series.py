def fibonacci(num):
    if num==0:
        return 0
    if num ==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)


def lucas(num):
    if type(num) != int or num < 0:
        return "invalid input"
    elif num == 0:
        return 2
    elif num == 1:
        return 1
    else:
        return lucas(num-1) + lucas(num-2)



def sum_series(num, val1=0, val2=1):
    if type(num) != int or num < 0:
        return "invalid input"
    elif num== 0:
        return val1
    elif num== 1:
        return val2
    else:
        return sum_series(num-1,val1,val2) + sum_series(num-2,val1,val2)
print(fibonacci(10))