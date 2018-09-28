class Calculator(object):
    def __init__(self, m, n):
        self.n = n
        self.m = m

    def sum(self):
        result = self.m
        if self.n < 0:
            for i in range(abs(self.n)):
                result -= 1
        else:
            for i in range(self.n):
                result += 1
        return result

    def divide(self):
        result =0
        negresult = self.m > 0 & self.n < 0 | self.m < 0 & self.n > 0
        self.n = abs(self.n)
        self.m = abs(self.m)
        if self.n == 0:
            result = "error"
        else:
            while self.m-self.n >= 0:
                self.m -= self.n
                result += 1

        return -result if negresult else result


def main():
    cal = Calculator(0, 0)
    a = cal.sum()
    b= cal.divide()
    print("sum =",a)
    print("quotient = ",b)


if __name__ == "__main__":
    main()