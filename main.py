def computeRate(days, code):
    
    # if the code selected was A
    
    if code == 'A':
    
    # per day charge = $99.99
    
    # per day meal's charge = $169.00
    
    return (99.99+169.00)*days
    
    # if the code selected was C
    
    elif code == 'C':
    
    # per day charge = $99.99
    
    # per day meal's charge = $112.00
    
    return (99.99+112.00)*days
    
    # if user do not want meals
    
    elif code == 'X':
    
    # per day charge = $99.99
    
    return 99.99*days
    
    # input days of stay
    
    days = int(input("Enter number of days of stay: "))
    
    # input if user want meals included
    
    includeMeal = input("Want to add meals? (y/n) ")
    
    # if user selected yes for meal
    
    if includeMeal == 'y':
    
    # ask him which code of meal he wants
    
    print("A: 3 meals per day, costs $116.00 per day")
    
    print("C: breakfast included, costs $112.00 per day")
    
    mealCode = input("Enter code: ")
    
    # if the code is invalid
    
    # ask again untill its valid
    
    while mealCode!='A' and mealCode!='C':
    
    print("OOPS! Invalid Code!!!")
    
    mealCode = input("Enter code: ")
    
    # if user does not want a meal
    
    else:
    
    mealCode = 'X'
    
    # call the function
    
    total_cost = computeRate(days, mealCode)
    
    # print the result
    
    print("Total bill: $", str(total_cost))
