# input: LIST 
    # [1, 2, 3]
# Output: 
    # [(1, 1), (2, 4), (3, 9)]

def tuplesDouble(mylist):
    ''' Input: A list of integers 
        Output: List of tuples'''
    mylistOfDoubles = []

    for number in mylist:
        mytuple = (number, number * number)
        mylistOfDoubles.append(mytuple)
    return mylistOfDoubles

def tuplesFunction(mylist,myfunc):
    ''' Input: A list of integers and a mathematical function
        Output: List of tuples'''
    mylistOfDoubles = []

    for number in mylist:
        mytuple = (number, myfunc(number))
        mylistOfDoubles.append(mytuple)
    return mylistOfDoubles

def exampleExponential(number):
    ''' Example of a mathematical function '''
    return number ** 2

print(tuplesDouble([1, 2, 3]))
print(tuplesFunction([1, 2, 3],exampleExponential))
