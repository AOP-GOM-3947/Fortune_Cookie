"""
* Name: Angel Gomez
* Date: November 12, 2024

* Progress: Completed

* Note: Though Completed (It can still be enhanced more)

"""
# Imports
from random import*
from time import*

# Fortune Cookie Class
class Fortune_Cookie:

    # Constructor Method
    def __init__(self, message = None):
        self.message = message

    # Step 1: Open Fortune Cookie
    def open_Fortune_Cookie(self):
        if self.message == None:
            # Update Fortune Cookie Message (Only Once)
            self.message = self.select_fortune()

            # Display Part 1 Of Result
            print("Opening Fortune: ", flush=True)

            # Wait For 1/2 a second
            sleep(1)

            # Call Function To Read & Display Fortune
            return self.read_my_fortune()
        else:
            print("You Already Opened Your Fortune Cookie.")

    # Step 2: Select A Fortune At Random From Given Text File
    def select_fortune(self):
        # Open Text File & Separate Each Line As An Element Within A List
        fortunes = open("fortune-cookies.txt").read().splitlines()

        # Choose A Random Line From Fortunes (List)
        my_fortune = choice(fortunes)

        return my_fortune
    
    # Step 3: Output The Fortune Message On Terminal Screen
    def read_my_fortune(self):
        if self.message != None:
            # Display Part 2 Of Result
            print("Your Fortune Is: ", end='', flush=True)

            # Pause For A Second
            sleep(0.5)
            
            # Print 5 Consecutive Periods Every Second
            for s in range(1, 9):
                print(".", end='', flush=True)
                sleep(0.5)

            # Make A NewLine
            print("\n")

            # Display Fortune Message
            print(self.message)

        else:
            print("Open Your Fortune Cookie!")

# Main Function 
def main(): 
    Angel = Fortune_Cookie()
    Angel.open_Fortune_Cookie()

# Access Main Function
if __name__ == "__main__":
    main()