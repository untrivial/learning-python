def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str)-1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num

def is_palindrome_one_liner(s):
    s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
    return s == s[::-1]

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False 
        i += 1
        j -= 1
    return True

def is_anagram_concise(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

def is_anagram(s1, s2):
    ht = dict()
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    for i in ht:
        if ht[i] != 0:
            return False
    return True

def is_palin_perm(input_str):
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    odd_count = 0
    for k, v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False
    return True

def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)

    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True

def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    d = dict()
    
    for i in str_1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            return False

    return all(value == 0 for value in d.values())

def is_unique(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True

def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)
    # set converts input_str into a set by removing all duplicates. Sets do not allow duplicate values

def is_unique_3(input_str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

# Integer to String
# ord() returns an integer that represents Unicode code point of the character passed
# chr() is the opposite

def int_to_str(input_int):
    
    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

    output_str = []

    if input_int == 0:
        output_str.append('0')
    else:   
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str
    
def str_to_int(input_str):

    if input_str[0] == "-":
        is_negative = True
        input_str = input_str[1:]
    else:
        is_negative = False
    
    output_int = 0

    if input_str == "0":
        return 0
    else:
        for i in range(len(input_str)):
            output_int += 10**(len(input_str) - i - 1) * (ord(input_str[i]) - ord("0"))
    
    if is_negative:
        return (output_int * -1)
    else:
        return output_int