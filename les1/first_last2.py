def first_last(s):
    ret = s[:2] + s[-2:]
    return ret

s1 = "spring"
s2 = first_last(s1)
print(s2)

s2 = first_last("hello")
print(s2)

print(first_last("abc"))
