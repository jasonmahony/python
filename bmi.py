def bmi(weight, height):
    bmi = (weight/height**2)
    print(bmi)
    return ("Underweight" if bmi <= 18.5 else "Normal" if bmi <= 25 else "Overweight" if bmi <= 30 else "Obese")
    
print(bmi(90, 1.80))