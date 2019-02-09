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
    print(list(filter(short_word, wordseq)))


def substitute_filter(wordseq):
    def short_word(word):
        if len(word) < 5:
            return True
    print([word for word in wordseq if short_word(word)])


def test_map(seq, wordseq):
    def glue(x):
        return str(x[0])+x[1]
    print(list(map(glue, zip(seq, wordseq))))


def substitute_map(seq, wordseq):
    def glue(x):
        return str(x[0]) + x[1]
    print([glue(pair) for pair in zip(seq, wordseq)])


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    words = ['apple', 'pear', 'banana', 'haw', 'fig']
    test_reduce(nums)
    substitute_reduce(nums)

    test_filter(words)
    substitute_filter(words)

    test_map(nums, words)
    substitute_map(nums, words)


