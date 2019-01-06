def increment(num):
    '''
    OBJECTIVE: to find the successor of defined function
    INPUTS: 1.num-given number as argument 
    RETURN:successor of given number
    '''
    '''
    APPROACH:add 1 in the given number
    '''
    return num+1
def sum2(num1,num2):
    '''
    OBJECTIVE:Find addition of two number without using + operator
    INPUT: 1.num1-first operand
    2. num2- second operand
    RETURN: addition of two number
    '''
    '''
    APPROACH:invoke increment and predecessor function
    '''
    assert num1 and num2 >=0
    if num2==0:
        return num1
    else:
        return sum2(increment(num1),num2-1)
number1=10
number2=20
result=sum2(number1,number2)
print(result)</strong>
 

 Mohit Arora
Mohit Arora 1 year ago  
Reply to this followup discussion
Resolved   Unresolved
smrity chaudhary
smrity chaudhary 1 year ago
 

def increment(number):
    '''
     objective: increment a given number by 1
     input parameter:
         number: number which is to be incremented
     return value: incremented number
     '''

    #approach: 1 is added to the number
    
    number = number + 1

    return number


def addition(number1 , number2):
    '''
     objective: sum of two user entered number
     input parameter:
         number1: first number entered by user
         number2: second number entered by user
        
     return value: sum of two numbers
     '''
    #approach: by calling increment function and addition function recursively

    
    if number2 == 0:
        return number1
    return addition(increment(number1) , number2-1)




def main():
    '''
     objective: sum of two user entered number
     input values:
         number1: first number entered by user
         number2: second number entered by user
        
     output value: sum of two numbers
     '''
    #approach:by calling addition function

    number1 = int(input("enter the first number: "))
    number2 = int(input("enter the second number: "))
    print("Sum of two numbers: " , addition(number1,number2))

if (__name__=='__main__'):
    main()
 

Reply to this followup discussion
Resolved   Unresolved
Mohit Arora
Mohit Arora 1 year ago
 

x=4
y=9
def increment(i):
    '''
    objective:to increment the value of a number
    input parameters:i-a number which value is to be incremented
    approach:using addition operator
             (+)
    '''
    i+=1
    return i
    
def sum(x,y):
    '''
    objective:to add two numbers
    input parameteres:
         x-first number
         y-second number
    approach-use the function increment and recursion
    return value-sum of the two numbers
    '''
    for i in range(0,y):
            j=increment(x)
            x=j
    return x
print('The sum of',x,'and',y,'is: ',sum(x,y))
