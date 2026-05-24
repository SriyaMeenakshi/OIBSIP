def calculate_bmi(weight, height): #Function to calculate BMI
    if weight<=0 or height<=0:
        print("Invalid input. Please enter proper values.")
        return None
    else:
        return weight/height**2
def get_category(bmi): #Function to determine BMI category
    if bmi is None:
        return
    if bmi<18.5:
        return "You are underweight."
    elif bmi<25:
        return "You have a normal weight."
    elif bmi<30:
        return "You are overweight."
    else:
        return "You are obese."
def main():
    try:
        print("BMI CALCULATOR")
        weight=float(input("Enter your weight in kgs: "))
        height=float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        if bmi is not None:
            print(f"Your BMI is: {bmi:.2f}")
        category = get_category(bmi)
        if category:
            print(category)
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")
    

if __name__=="__main__":
    main()
