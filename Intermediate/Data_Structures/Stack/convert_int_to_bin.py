from stack import Stack

def convert_int_to_bin(dec_num):
    s = Stack()
    binary_equiv = ""

    while dec_num > 0:
        s.push(dec_num % 2)
        dec_num = dec_num // 2
    while not s.is_empty():
        bit = str(s.pop())
        binary_equiv += bit
    return binary_equiv

print("hello")
print(convert_int_to_bin(242))