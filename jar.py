class Jar:
    def __init__(self, capacity=12):
        try: 
            if not isinstance(capacity,int) or capacity<0:
                raise ValueError
            self.jarcapacity=capacity
            self.cookie_count=0
        except ValueError:
            raise

    def __str__(self):
        return self.size*"🍪"

    def deposit(self, n):
        if n<0 or self.size+n>self.capacity:
            raise ValueError
        self.cookie_count=self.cookie_count+n

    def withdraw(self, n):
        if n<0 or self.size-n<0:
            raise ValueError
        self.cookie_count=self.cookie_count-n

    @property
    def capacity(self):
        return self.jarcapacity

    @property 
    def size(self):
        return self.cookie_count