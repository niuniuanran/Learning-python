# In programming languages, a closure is a technique for implementing
# lexically scoped name binding in a language with first-class functions.
#  Operationally, a closure is a record storing a function together with an environment.


def multiplier(factor):
    print('locals of multiplier function:', locals())

    def multiplybyfactor(number):
        print('locals of multiplyfactor function:', locals())
        return factor * number
    return multiplybyfactor
# return 的是一个函数。
# multiplier是一个构造函数用的函数。
# 像 multiplyByFactor这样存储其所在作用域的函数称为闭包。 它储存了factor


def test():
    double = multiplier(2)
    triple = multiplier(3)

    print('double is a new function constructed by multiplier that takes one argument')
    d3 = double(3)
    print('double({}) = {}'.format(3, d3))
    t3 = triple(3)
    print('triple({}) = {}'.format(3, t3))

    print('multiplier({})({}) = {}'.format(3, 10, multiplier(3)(10)))


if __name__ == '__main__':
    test()
