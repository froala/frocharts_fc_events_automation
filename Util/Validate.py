import numbers

def check_if_int(num):
    cast_to_int=(int(num) + 1)
    return isinstance(cast_to_int, int)

def check_if_function(strn):
    thisStr=str(strn)
    if thisStr.startswith('{}'):
        return True
    else:
        return False

def check_if_boolean(boolVal):
    if boolVal == True:
        return True
    elif boolVal == False:
        return True
    else:
        return False
    
def check_if_not_empty_string(strn):
    strn_chk = str(strn)
    if strn_chk and strn_chk.strip() :
        return True
    else:
        return False

def check_if_number(num):
    if isinstance(num, numbers.Real):
        return True
    else:
        return False
    
def check_if_url(strn):
    thisStr=str(strn)
    if thisStr.startswith('http'):
        return True
    else:
        return False