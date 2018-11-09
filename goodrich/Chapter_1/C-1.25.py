def remove_punctuation(string):
    """
    """
    
    string_list = []
    for char in string:
        string_list.append(char)
        
    for char in string_list:
        if char in '.,/?"-':
            string_list.remove(char)
            
    return "".join(string_list)
    
    
string = 'Let’s try, Mike.'
print(remove_punctuation(string))


## punctuation_marks = ',.;:?!−_()[]\'\/<">{}#=' 
## for punctuation in punctuation_marks: 
##     string = string.replace(punctuation, "") 
##   return string
