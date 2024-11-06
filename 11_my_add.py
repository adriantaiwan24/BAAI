#
# Adrian
# My Add
#

def my_add(input):
    sum = 0
    for x in input:
        sum+= int(x)
    return(sum)

# 1. Input
input = [10, 20, 30]

# 2. Process
answer = my_add(input)

# 3. Output
print(f"Answer: {answer}")
