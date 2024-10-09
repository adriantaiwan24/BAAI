#
# Adrian
# Compare two numbers ad print the bigger one
#

# 1. Input
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))

# 2. Process 
# Compare two numbers
if n1 > n2:
    output = f"Number 1 ({n1}) is bigger than Number 2 ({n2})"
elif n1 < n2:
    output = f"Number 2 ({n2}) is bigger than Number 1 ({n1})"
elif n1 == n2:
    output = f"Number 1 ({n1}) is equal to Number 2 ({n2})"

# 3. Output
print(output)