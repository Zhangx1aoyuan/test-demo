class Mydiedai():
    def __init__(self):
        self.n = 0
        self.m = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.m:
            self.n += 2
        else:
            raise StopIteration
        return self.n


mdd = Mydiedai()
mdd.m = 50
# for i in mdd:
#     print(i)
li = list(mdd)
print(li)