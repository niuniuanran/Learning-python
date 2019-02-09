# lambda operator or lambda function is used for creating small,
# one-time and anonymous function objects in Python. lambda operator
# can have any number of arguments, but it can have only one expression.
# It cannot contain any statements and it returns a function object which
# can be assigned to any variable.


def test_reduce(seq):
    from functools import reduce
    print(reduce(lambda x, y: x+y, seq))


def substitute_reduce(seq):
    print(sum(seq))


def test_filter(wordseq):
    def short_word(word):
        if len(word) < 5:
            return True
        else:
            return
    print(list(filter(short_word, wordseq)))


def substitute_filter(wordseq):
    print([word for word in wordseq if len(word) < 5])


if __name__ == '__main__':
    seq = [1, 2, 3, 4]
    wordseq = ['apple', 'pear', 'banana', 'haw', 'fig']
    test_reduce(seq)
    substitute_reduce(seq)
    test_filter(wordseq)
    substitute_filter(wordseq)


