class myLinkedList(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    def __add__(self, other):
        return self.myfunction(self, other)

    def myfunction(self, other):
        return self.val + other.val


test = myLinkedList(10)
other = myLinkedList(5)
test.myfunction = lambda a,b: a.val - b.val
print(test+other)
