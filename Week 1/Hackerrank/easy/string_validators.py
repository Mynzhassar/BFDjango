def is_alpha(s):
    for c in s:
        if (65 <= ord(c) and ord(c) <= 90) or (97 <= ord(c) and ord(c) <= 122):
            return True
    
    return False

def is_digit(s):
    for c in s:
        if 48 <= ord(c) and ord(c) <= 57:
            return True
    
    return False

def is_alnum(s):
    if is_alpha(s) or is_digit(s): return True
    return False

def is_lower(s):
    for c in s: 
        if 97 <= ord(c) and ord(c) <= 122:
            return True

    return False

def is_upper(s):
    for c in s: 
        if 65 <= ord(c) and ord(c) <= 90:
            return True

    return False

if __name__ == '__main__':
    s = input()
    if is_alnum(s): print("True")
    else: print("False")

    if is_alpha(s): print("True")
    else: print("False")

    if is_digit(s): print("True")
    else: print("False")

    if is_lower(s): print("True")
    else: print("False")

    if is_upper(s): print("True")
    else: print("False")

