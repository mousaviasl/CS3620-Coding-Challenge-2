def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Example usage
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi}")