class Fibonacci:
    def __init__(self, terms):
        self.terms = terms
        self.count = 0
        self.n1, self.n2 = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.terms:
            if self.count == 0:
                self.count += 1
                return self.n1
            elif self.count == 1:
                self.count += 1
                return self.n2
            else:
                self.n1, self.n2 = self.n2, self.n1 + self.n2
                self.count += 1
                return self.n2
        else:
            raise StopIteration

# Testing the Fibonacci iterator
fib = Fibonacci(5)
for num in fib:
    print(num)
