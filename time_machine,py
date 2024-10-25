def time_machine():
    print("Welcome to the Time Machine!")
    print("You can visit the following years: 1066, 1492, 1776, 1914, 1945, 1969, 1989, 1995, 2001, 2020")

    # Dictionary of years and historical events
    events = {
        "1066": "You've arrived in 1066! The Norman Conquest of England is underway.",
        "1492": "It's 1492! Christopher Columbus has just reached the Americas.",
        "1776": "Welcome to 1776! The United States Declaration of Independence has been signed.",
        "1914": "You've landed in 1914. World War I has just begun.",
        "1945": "It's 1945! World War II has ended, and the United Nations is founded.",
        "1969": "You've arrived in 1969. Humans have landed on the Moon for the first time.",
        "1989": "Welcome to 1989! The Berlin Wall is falling, symbolizing the end of the Cold War.",
        "1995": "You've arrived in 1995! The internet is starting to become mainstream.",
        "2001": "It's 2001. The tragic events of September 11th have reshaped global politics.",
        "2020": "You've landed in 2020. The world is dealing with a global pandemic."
    }

    while True:
        year = input("Enter the year you want to travel to: ")

        if year in events:
            print(events[year])  # Output the event for the chosen year
            break
        else:
            print("Invalid year! Please choose from 1066, 1492, 1776, 1914, 1945, 1969, 1989, 1995, 2001, or 2020.")
            retry = input("Would you like to try again? (yes/no): ")
            if retry.lower() != "yes":
                print("Thank you for using the Time Machine! Goodbye.")
                break

# Running the time machine
time_machine()
