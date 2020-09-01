class ListDivideException(Exception):
    pass

def listDivide(numbers, divide=2):
    divisible_by_divide=0
    for number in numbers:
        if number % divide == 0 :
            divisible_by_divide += 1
    return divisible_by_divide

def testListDivide():
    try:
        print(listDivide([1,2,3,4,5])) #should return 2
        print(listDivide([2,4,6,8,10])) #should return 5
        print(listDivide([30, 54, 63,98, 100], divide=10)) #should return 2
        print(listDivide([])) #should return 0
        print(listDivide([1,2,3,4,5], 1)) #should return 5
        #print(listDivide([1,2,3,4,5], 'A')) #should rais exception
    except:
        raise ListDivideException

#divisible_by_divide = listDivide ([1,2,3,4,5,6,7,8,9],3)
#print (divisible_by_divide)
testListDivide()