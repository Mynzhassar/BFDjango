def swap_case(s):
    res = ""
    for char in s:
        if 65 <= ord(char) and ord(char) <= 90: res += chr(ord(char) + 32)
        elif 97 <= ord(char) and ord(char) <= 122 : res += chr(ord(char) - 32)
        else: res += char
    
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)