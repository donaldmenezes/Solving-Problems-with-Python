def array_product(list1, list2):
    """
    assumes list1 and list2 are of equal length and all the elements of list1 and list2 are integers
    returns an array of product of each element of the list
    
    >>> array_product([1,2,3], [3,2,1])
    [3,4,3]
    """
    
    lgth = len(list1)
    product_list = []
    
    for i in range(0, lgth):
        product_list.append(list1[i] * list2[i])
            
    return product_list
    
    
## one line program  
## return [x∗y for x,y in zip(a,b)]
