class Name(object):
    def __init__(self, name):
        self.name1 = name
        self.name2 = 'jesus'

    def function(self):
        return self.name1, self.name2


print(Name('judas').function())
