'''
Simple Rule based Command line Chat bot for Resturant Table Booking

'''
import time

class Resturant:

    company = "Lazzes Rasoi"
    max_tables = 10
    max_people = max_tables*7

    def __init__(self):
        pass

    def greet(self):
        print('#'*65)
        print(f'    Welcome to {self.company} ')
        print(f'    I am your Personal Command Line Assistant for Booking Table  ')
        print('#'*65)

    def peopleCount(self):
        print('#'*80)
        print(
            "How many people would you like to book for? ---> (Press integer from 1 to 7)")
        print("1. One\n2. Two\n3. Three\n4. Four\n5. Five\n6. Six\n7. Seven\n")

        self.input_people = int(input())
        print('-'*30)
        if self.input_people > 7:
            print("Invalid Input")
            print("@"*50)
            exit()
        else:
            print("Confirmed ", self.input_people, "People")
            print('~'*65+"\n")

    def bookingDate(self):
        print('#'*65)
        print(
            "When should we Book your Table? ---> (Press integer from 1 to 3)")
        print("1. Today\n2. Tommorow\n3. Day after Tommorow\n")

        self.input_day = int(input())
        print('~'*65+"\n")
        if self.input_day > 3:
            print("Invalid Input")
            print("@"*50)
            exit()
        elif self.input_day == 1:
            self.day = "Today"
        elif self.input_day == 2:
            self.day = "Tommorow"
        elif self.input_day == 3:
            self.day = "Day after Tommorow"
        else:
            print("Invalid Input")

    def bookingTime(self):
        print('#'*65)
        print(
            "At What time are you Ariving? ---> (Press integer from 1 to 3)")

        print("\t\t\tTimming")
        print('-'*40)
        print("1. Breakfast     (07:00 to 10:30)\n2. Lunch         (11:30 to 17:00)\n3. Dinner        (18:00 to 24:00 P.M)\n")

        self.input_time = int(input())
        print('~'*65+"\n")
        if self.input_time > 3:
            print("Invalid Input")
            print("@"*50)
            exit()
        else:
            print('#'*65)
            print("Enter Time in HH:MM formate ---> (like - 09:30, 15:49, 12:00)\n")
            self.time = input()
            print('-'*65+"\n")

    def anothrBooking(self):
        print("Press (Y) for Booking Again\nPress (N) for Exit")
        print('~'*40)
        inp_key = input().lower()
        if inp_key == 'n':
            print("Sussecfully Exited")
            exit()
        else:
            pass

    def avi_tables(self):
        pass


class Customer(Resturant):

    #   //  def __init__(self, name, location):
    #         self.name = name
    #         self.location = location

    def user_Details(self):
        print('-'*50)
        print("Enter Your Name")
        print('-'*50)
        self.name = input()
        location = ["Delhi", "Gurugram"]
        print('~'*50)
        print('''Choose the location ---> (Press 1 or 2)
              1. Delhi
              2. Gurugram''')
        print('~'*50)
        location_input = int(input())
        if location_input == 1:
            self.location = location[0]
        elif location_input == 2:
            self.location = location[1]
        else:
            print("Invalid Input")
            print("@"*50)
            exit()

    def conformation(self):
        print('~'*40)
        print('/'*40)
        print('~'*40)
        print(f'Name : {self.name}\nLocation : {self.location}\nTable for : {self.input_people}\nDate : {self.day}\nTime : {self.time}')
        print('-'*40)
        print("Do you want to confirm the details")
        print('-'*40)
        print('~'*40)
        print("Press (Y) for Confirm Booking\nPress (N) for Exit")
        print('~'*40)
        in_key = input().lower()
        if in_key == 'n':
            print("Sussecfully Exited")
            exit()
        else:
            print('''\n\nThank you for reservation,
I am going to ask human about your table
and get back to you.
                  ''')
            print('~'*40)
            print('/'*40)
            print('~'*40)
            time.sleep(7)
            '''
            Sending Users Data to Resturant and Confirming for the Table Booking
            '''
            print('-'*40)
            print("!!! CONFIRMED !!!")
            print('-'*40)
            print(
                f'Name : {self.name}\nLocation : {self.location}\nTable for : {self.input_people}\nDate : {self.day}\nTime : {self.time}')
            print('-'*40)
            print("Have a nice day :)")
            print('~'*40+"\n")
            print('@'*90)

    def getDetails(self):
        print(f"the name of the customer is {self.name}")
        print(f"the location of the customer is {self.location}")


if __name__ == "__main__":
    print("@"*50)
    print("\nPress (any Alphabet) for Booking table\nPress (N) for Exit")
    input_key = input().lower()
    if input_key == 'n':
        print("Sussecfully Exited")
        print("@"*50)
    else:

        # user 1
        LazzezR = Resturant()
        LazzezR.greet()
        naman = Customer()
        naman.user_Details()
        naman.peopleCount()
        naman.bookingDate()
        naman.bookingTime()
        naman.conformation()

        # print(naman.input_people)
        # naman.getDetails()

# user 2
        LazzezR = Resturant()
        LazzezR.greet()
        mayank = Customer()
        mayank.anothrBooking()
        mayank.peopleCount()
        mayank.user_Details()
        mayank.bookingDate()
        mayank.bookingTime()
        mayank.conformation()
