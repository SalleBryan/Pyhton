import sys
def collatz(number):
    #Even number check and operation
    if (number % 2 == 0):
        ans = number // 2
        print(ans, end=" ")
        return ans
    
    #Odd number check and operation
    elif (number % 2 != 0):
        ans = 3 * number + 1
        print(ans, end=" ")
        return ans    
    
try:
    #Collatz loop
    print("Enter a number: ", end="")
    num = int(input())
    
    while (num != 1):
        ans = collatz(num)
        num = ans

#Clean Exit
except KeyboardInterrupt:
    sys.exit()

except ValueError:
    print("You Must Enter an integer!!")