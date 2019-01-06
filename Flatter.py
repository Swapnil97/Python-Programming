def Flatter(List,Flattered=[]):
    '''
    OBJECTIVE:TO flat the nested list inputted by user
    INPUTS: 1.List-Given List
            2.Flattered=new flattered list
    Return: New FLattered list
    '''
    
    if(len(List)==0):
        return Flattered
    elif(type(List[0])== list):
         Flattered.extend(List[0])     
         return Flatter(List[1:],Flattered)
    else:
        Flattered.append(List[0])
        return Flatter(List[1:],Flattered)
List1=[1,2,43,67,[1,7,9]]
print(Flatter(L))
