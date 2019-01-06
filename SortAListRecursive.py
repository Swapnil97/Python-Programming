def miniIndex(List,lower,upper):
'''
OBJECTIVE:TO FIND THE INDEX OF MINIMUM ELEMENT OF THE LIST
INPUTS:1.List-LIST INPUTTED BY THE USER
RETURN:INDEX OF MINIMUM ELEMENT
'''
'''
APPROACH:BY USING RECURSION
'''
if lower==upper:
return upper
elif List[lower]<List[upper]:
return miniIndex(List,lower,upper-1)
else:
return miniIndex(List,lower+1,upper)
l=[1,6,84,2,4]
miniIndex(l,0,4)
