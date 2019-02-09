'''
lambda operator or lambda function is used for creating small,
one-time and anonymous function objects in Python. lambda operator
can have any number of arguments, but it can have only one expression.
It cannot contain any statements and it returns a function object which
can be assigned to any variable.
'''

'''
The function taken by reduce takes two args and returns one value. reduce applies this function to the seq iteratively until 
there is one value left to be returned.
'''
def test_reduce(seq):
    from functools import reduce
    print(reduce(lambda x, y: x+y, seq))


'''
reduce is the hardest to be substituted in reduce, filter and map, because you need to find another new method to substitute it.
Here sum() is a very handy substitute.
'''
'''
also equal to add(seq[0],add(seq[1],add(seq[2],add(seq[3], ... ))))
'''
def substitute_reduce(seq):
    print(sum(seq))


'''
filter returns a filter object that is iterable and can be transformed into a list using list()
The function used by filter returns a boolean val, True or False.
Based on this function, filter builds a new iterable object that contains all the items in the seq that produces True
    in the function.
'''
def test_filter(wordseq):
    def short_word(word):
        if len(word) < 5:
            return True
    print(list(filter(short_word, wordseq)))


'''
filter can be perfectly substituted by the list generator.
'''
def substitute_filter(wordseq):
    def short_word(word):
        if len(word) < 5:
            return True
    print([word for word in wordseq if short_word(word)])


'''
map returns a map object that is also iterable.
The function taken by map takes one arg and returns one value.
map function produces the result of each item in seq through the function, and builds a list of the results.
'''
def test_map(seq, wordseq):
    def glue(x):
        return str(x[0])+x[1]
    print(list(map(glue, zip(seq, wordseq))))

'''
map can be perfectly substituted by list generator.
'''
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


