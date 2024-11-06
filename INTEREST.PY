#
# Adrian
# Interest
#

# 1. Input
def calculate_interest(principal, rate, time):
    interest = (principal*rate*time)/100
    return interest

# 2. Process
y = calculate_interest(1000, 5, 2)

# 3. Output
print(f"Interest: {y}")