# Some simple functions in python

def main():
    helloWorld()
    testCalculateSum()
    testFibonacci()


def helloWorld():
    print("Hello World! Here are some basic python functions. \n")
    
def calculateSum(values):
    sum = 0
    for val in values:
        sum += val
    return sum

def testCalculateSum():
    values = [1,2,3,4,5,6,7,8,9,10]
    print("Calculated Sum: " + str(calculateSum(values)))

def fibonacci(n):
    # Base case at n=0,1
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) +fibonacci(n-2)

def testFibonacci():
    fib = int(input("Enter your desired fibonacci number: "))
    num = fibonacci(fib)
    print(num)







    # This is a comment from the test Branch 


if __name__ == "__main__":
    main()

