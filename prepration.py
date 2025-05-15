# making function for calculating speed 

def cal_speed():
    try:
        distance = float(input("Enter the distance traveld in (kilometers): "))
        time_mins = float(input("Enter the time in (minutes): "))

        time_huors = time_mins / 60

        if time_huors == 0 :
            print("The time can't be zero")
            return
        speed = distance / time_huors
        print(f"Your speed is {speed:.2f} Km/h")

    except ValueError :
        print("invalid syntex, Please Enter numeric value for both \"Time\" and \"Distance\"")

cal_speed ()
        