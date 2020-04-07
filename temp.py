

#function to add no from o to n

def sum(n):
    totalsum=0
    for x in range(n+1):
        totalsum+=x
    return totalsum


def sum1(n):
    return (n*(n+1)/2)
        
    
def func_quad(lst):
    '''
    Prints pairs for every item in list.
    '''
    for item_1 in lst:
        for item_2 in lst:
            print ((item_1,item_2))
            
lst = [0, 1]

def test(lst):
    for nos in lst:
        print('test')
        
    for noss in lst:
        print(noss)
        print(noss)

def n_lst(n):
    new_list=[]
    for x in lst:
        new_list.append('new')
    print(new_list)
    
#%%
def sum2(n):
    if n<0: #if input no is negitive it print below statement
        print('enter a possitve no')
    else:
        
        sum=0
        while n!=0: #it will check no is greater then zero
            
            sum=n+sum # it will add number to sum
            n-=1 #it will decrease no by one
        print(sum) #finally it will print sum of n number 
        
            
    
    
#%%   
#swapping of a number
        
def swapping(a,b):
    temp=0
    temp=a
    a=b
    b=temp
    print('The value of a after swapping: {}'.format(a))
    print('The value of b after swapping: {}'.format(b))
    print('value of a after swap:',a)
    print('value of b after swap:',b)
 #%%   
#sum of natural no using for loop
def sum3(n):
    if n<0:
        print('you entered a non_natural no')
    else:
        sum=0
        for i in range(n+1):
            sum+=i
            i+=1
        print(sum)
        print (n)
#%%

            
        
    
        