# 获取全局变量global variant -- number的值：
def multiply(factor):
    return globals()['number'] * factor


# 使用关键词 global 获取，修改和使用number
def changemultiply(factor):
    global number
    number = 4
    return factor * number


def testglobals(factor):
    globals()['number'] = 3
    return globals()['number'] * factor


def test():
    print("testing the use of globals():")
    result = multiply(factor=2)
    print(result)
    print("\n")

    print("testing the use of keyword global:")
    result = changemultiply(factor=2)
    print(result)
    print("\n")

    print("testing if globals() could induct changes:")
    result = testglobals(2)
    print(result)
    print("so, the function globals() returns something like a dictionary.")
    print('\n')

    print("peeking into globals:")
    print(globals())
    print('\n')

    print('peeking into locals:')
    print(locals())
    print('\n')


if __name__ == '__main__':
    number = 3
    test()
