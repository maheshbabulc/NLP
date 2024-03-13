
# b={"a",123}
# # b.clear()
# def sum(a,b):
#     c=a+b
#     b.clear()
#     return c
# print(sum(1,2))
# print(b)

b = {"a", 123}

def sum(a, b):
    c = a + b
    b.clear()  # This 'b' is the function parameter, not the global variable
    return c

print(sum(1, 2))
print(b)
