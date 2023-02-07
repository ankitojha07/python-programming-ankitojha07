class DeQueueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def isempty(self):
        return len(self._data) == 0
    
    def addfirst(self,e):
        self._data.insert(0, e)

    def addlast(self,e):
        self._data.append(e)

    def removefirst(self):
        if self.isempty():
            print('Empty DEQueue')
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print('Empty queue')
            return
        return self._data.pop()

    def first(self):
        if self.isempty():
            print('Empty queue')
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print('Empty queue')
            return
        return self._data[-1]

d = DeQueueArray()
d.addfirst(9)
d.addfirst(12)
d.addfirst(14)
d.addfirst(14)
d.addlast(20)


print(d.removefirst())
print(d.first())

print(d._data)

