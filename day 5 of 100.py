# swap the values of two variables without using a temporary variable.
a = 5
b = 10

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("a =", a)
print("b =", b)
