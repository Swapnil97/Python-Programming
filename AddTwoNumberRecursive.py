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
print(result)
