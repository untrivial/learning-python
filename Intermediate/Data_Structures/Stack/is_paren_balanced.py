from stack import Stack

def is_match(one, two):
    if one == "(" and two == ")":
        return True
    elif one == "{" and two == "}":
        return True
    elif one == "[" and two == "]":
        return True
    else:
        return False

def is_paren_balanced(paren):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren) and is_balanced:
        next_value = paren[index]
        
        if next_value in "([{":
            s.push(next_value)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, next_value):
                    is_balanced = False
                    break
        index += 1

    return s.is_empty() and is_balanced


print(is_paren_balanced('()'))