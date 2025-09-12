def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)  

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Example usage:
weight = int(input("enter height"))
height = int(input("enter weight"))

bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is {bmi}, which is considered {category}.")
