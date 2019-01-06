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

def sortTheList(List,start=0):
    '''
    OBJECTIVE:TO SORT THE LIST BY FINDING MINIMUM ELEMENT USING FUNCTION
    INPUTS:List=INPUTTED LIST BY USER
    RETURN:SORTED LIST
    '''
    '''
    APPROACH:BY USING RECURSION AND RECURSIVE FUNCTION miniIndex
    '''
    end=len(List)-1
    if(start<=end):
        minimum=miniIndex(List,start,end)
        temp=List[start]
        List[start]=List[minimum]
        List[minimum]=temp
        start=start+1
        sortTheList(List,start)
    return List
L=[3,5,7,9,4,-1,6]
sortTheList(L)
