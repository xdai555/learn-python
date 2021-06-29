

class RoundFloat(object):
    def __init__(self, val):
        assert isinstance(val, float)
        self.value = round(val, 2)
    
    def __str__(self):
        return '%.2f' %self.value
    
    def __repr__(self):
        return self.__str__


class Time60():
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min
    
    def __str__(self) -> str:
        return '%d:%d'%(self.hr, self.min)

    def __add__(self, val):
        return self.__class__(self.hr + val.hr, self.min + val.min)

    def a(self):
        return ('aaa')

b = Time60(11,22)
print(getattr(b,"a")())