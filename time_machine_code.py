
# Time Machine Code
def time_machine():
    print("Welcome to the Time Machine!")
    print("You can visit the following years: 1995, 2000, 2010, 2020")
    
    available_years = ["1995", "2000", "2010", "2020"]
    
    while True:
        year = input("Enter the year you want to travel to: ")
        
        if year in available_years:
            if year == "1995":
                print("You've arrived in 1995! The internet is in its early days.")
            elif year == "2000":
                print("Welcome to the year 2000! The Y2K bug was a big concern.")
            elif year == "2010":
                print("It's 2010! The rise of smartphones is happening.")
            elif year == "2020":
                print("You've landed in 2020. The world is dealing with a global pandemic.")
            break
        else:
            print("Invalid year! Please choose from 1995, 2000, 2010, or 2020.")
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != "yes":
                print("Thank you for using the Time Machine! Goodbye.")
                break

# Running the time machine
time_machine()
    