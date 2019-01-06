def merge(A,B,index1=0,index2=0,C=[]):
    '''
    Objective : Merge two sorted lists - efficiently
    parameters :
        A : sorted list A
        B : sorted list B
        index1 : index tracker for list A
        index2 : index tracker for list B
        C : the merged list
        
    '''

    # end of list A reached
    if( index1 == len(A) ):
        # end of list B reached
        if( index2 == len(B) ):
            return C
        else:
            C.append(B[index2])
            index2 +=1
            return merge(A,B,index1,index2,C)

    else:
        # end of list B reached
        if( index2 == len(B) ):
            # list B is done, A is still not done
            C.append(A[index1])
            index1 +=1
            return merge(A,B,index1,index2,C)

        else:
            if(A[index1]<B[index2]):
                C.append(A[index1])
                index1 += 1
                return merge(A,B,index1,index2,C)
            else:
                C.append(B[index2])
                index2 += 1
                return merge(A,B,index1,index2,C)

list1=[1,2,5,8,9]
list2=[2,4,5,80,90]
list3=merge(list2,list2)
print(list3)
