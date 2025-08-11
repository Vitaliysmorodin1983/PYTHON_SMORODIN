from уроки_4.calculator import Calculator

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-4, -6)
    assert res == -10
def test_sum_positive_and_negative_nums(): 
    calculator = Calculator()
    res = calculator.sum(-6, 6) 
    assert res == 0 




#print ("start")
#res = calculator.sum(4, 6)
#rsa = 10
#ssert res == 10
#res = calculator.sum(-6, -10)
#assert res == -18
#res = calculator.sum(-6, 6)
#assert res == 0
#res = calculator.sum(5.6, 5.3)
#res = round(res, 1)
#print(res)
#assert res == 10.9
#numbers = [2, 3, 5, 7, 11]
#res = calculator.avg(numbers)
#assert res == 5.6
#print(res)
#print ("finish")
#if (4 + 6 == rsa):
#    print(rsa)