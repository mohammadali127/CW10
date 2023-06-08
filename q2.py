class FibonacciIter:
    def __init__(self):
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        value = self.a
        self.a,self.b = self.b , self.a+self.b
        return value

obj = FibonacciIter()
for i in range(10):
    print(f"{i+1} : {next(obj)}")
