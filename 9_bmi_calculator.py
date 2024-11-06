#
# Adrian
# BMI Calculator
#

while True:
    # 1. Input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # 2. Process
    bmi = weight/(height**2)

    # 3. Output
    print(f"Your BMI is {bmi}")
    answer = input("Continue (yes/no): ").strip().lower()
    if answer == "no":
        break