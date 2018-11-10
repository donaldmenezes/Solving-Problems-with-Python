def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    #return True if zip_code.isnumeric() == True and len(zip_code) == 5 else return False
    if zip_code.isnumeric() == True and len(zip_code) == 5:
        return True
    else: 
        return False
