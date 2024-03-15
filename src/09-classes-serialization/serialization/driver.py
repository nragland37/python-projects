# ****************************************************************************************************
#
#       This program utilizes classes and serialization (converts the object into a binary stream)
#       to create a menu driven program that allows the user to perform various operations on a 
#       dictionary of Employee objects.
#
#       Other files required:
# 		  1.    employee.py - defines the Employee class
#         2.    employees.dat - stores the dictionary of Employee objects as a binary stream
#                               (not strictly required, the commented out code in load_employees()
#                               will create the file with the predefined employees if missing)
#
# ****************************************************************************************************

from employee import Employee
import pickle

# ****************************************************************************************************

FILENAME = "employees.dat"

# ****************************************************************************************************


def load_employees():
    try:
        with open(FILENAME, "rb") as f:
            employee_dict = pickle.load(f) 
            
        # predefined_employees = [
        #     Employee("Susan Meyers", 47899, "Accounting", "Vice President"),
        #     Employee("Mark Jones", 39119, "IT", "Programmer"),
        #     Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
        # ]
        
        # for employee in predefined_employees:
        #     emp = employee.get_id_number()
            
        #     if emp not in employee_dict:
        #         employee_dict[emp] = employee
                
    except IOError:
        employee_dict = {}
    except Exception as e:
        print(f"\nError: {e}")

    return employee_dict


# ****************************************************************************************************


def get_user_choice(employee_dict):
    MENU = {
        1: look_up,
        2: add,
        3: change,
        4: delete,
        5: display_all
    }
    success = True

    while success:
        print(f'\n\n{"Menu":^35}\n{"-" * 35}')
        print(
            "1. Look up an employee\n"
            "2. Add a new employee\n"
            "3. Change an existing employee\n"
            "4. Delete an employee\n"
            "5. Display all employees\n"
            "6. Quit the program\n"
        )
        try:
            ch = int(input("Enter your choice: "))

            if ch == 6:
                save_employees(employee_dict)
                print("\nGoodbye!")
                success = False
            else:
                MENU[ch](employee_dict)

        except ValueError as ve:
            print(f"\nError: {ve}")
        except KeyError as ke:
            print(f"\nError: {ke} is not a valid choice.")
        except Exception as e:
            print(f"\nError: {e}")


# ****************************************************************************************************


def look_up(employee_dict):
    success = True
    
    while success:
        try:
            number = int(input("Enter an employee ID number: "))
            
            if employee_dict.get(number, False):
                print(f'\n{"Name":20}{"ID":20}{"Department":20}{"Job Title":20}')
                print(f'{"-" * 80}')
                print(employee_dict[number])
                success = False
            else:
                raise ValueError("The specified ID number was not found.")
            
        except ValueError as ve:
            print(f"\nError: {ve}\n")
        except Exception as e:
            print(f"\nError: {e}\n")


# ****************************************************************************************************


def add(employee_dict):
    success = True
    
    while success:
        try:
            name = input("Enter employee name: ").title()
            id_number = int(input("Enter employee ID number: "))
            department = input("Enter employee department: ").title()
            job_title = input("Enter employee title: ").title()

            if id_number not in employee_dict:
                entry = Employee(name, id_number, department, job_title)
                employee_dict[id_number] = entry
                print("\nThe new employee has been added.")
                success = False
            else:
                raise ValueError("The specified ID number was not found.")
                
        except ValueError as ve:
            print(f"\nError: {ve}\n")
        except Exception as e:
            print(f"\nError: {e}\n")


# ****************************************************************************************************


def change(employee_dict):
    success = True
    
    while success:
        try:
            number = int(input("Enter an ID number: "))

            if number in employee_dict:
                name = input("Enter the new name: ")
                department = input("Enter the new department: ")
                job_title = input("Enter the new job title: ")

                entry = Employee(name, number, department, job_title)
                employee_dict[number] = entry
                print("Information updated.")
                success = False
            else:
                raise ValueError("The specified ID number was not found.")
                
        except ValueError as ve:
            print(f"\nError: {ve}\n")
        except Exception as e:
            print(f"\nError: {e}\n")


# ****************************************************************************************************


def delete(employee_dict):
    success = True
    
    while success:
        try:
            number = int(input("Enter an employee ID number: "))

            if number in employee_dict:
                del employee_dict[number]
                print("Entry deleted.")
                success = False
            else:
                raise ValueError("The specified ID number was not found.")
                
        except ValueError as ve:
            print(f"\nError: {ve}\n")
        except Exception as e:
            print(f"\nError: {e}\n")


# ****************************************************************************************************


def display_all(employee_dict):
    print(f'\n{"Name":20}{"ID":20}{"Department":20}{"Job Title":20}')
    print(f'{"-" * 80}')
    
    for employee in employee_dict.values():
        print(employee)


# ****************************************************************************************************


def save_employees(employee_dict):
    try:
        with open(FILENAME, "wb") as f:
            pickle.dump(employee_dict, f)
            
        print("The data has been saved.")
        
    except IOError: 
        print("\nError: Unable to save the data.")
    except Exception as e:
        print(f"\nError: {e}")


# ****************************************************************************************************


def main():
    employee_dict = load_employees()
    get_user_choice(employee_dict)


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************
"""

               Menu                
-----------------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Display all employees
6. Quit the program

Enter your choice: 1
Enter an employee ID number: 47899

Name                ID                  Department          Job Title           
--------------------------------------------------------------------------------
Susan Meyers        47899               Accounting          Vice President      


               Menu                
-----------------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Display all employees
6. Quit the program

Enter your choice: 2
Enter employee name: John Doe
Enter employee ID number: 15632
Enter employee department: Management 
Enter employee title: Manager

The new employee has been added.


               Menu                
-----------------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Display all employees
6. Quit the program

Enter your choice: 3
Enter an ID number: 47899
Enter the new name: Buzz Lightyear
Enter the new department: Space 
Enter the new job title: Space Cowboy
Information updated.


               Menu                
-----------------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Display all employees
6. Quit the program

Enter your choice: 5

Name                ID                  Department          Job Title           
--------------------------------------------------------------------------------
Mark Jones          39119               IT                  Programmer          
Joy Rogers          81774               Manufacturing       Engineer            
Buzz Lightyear      47899               Space               Space Cowboy        
John Doe            15632               Management          Manager             


               Menu                
-----------------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Display all employees
6. Quit the program

Enter your choice: 4
Enter an employee ID number: 47899
Entry deleted.


               Menu                
-----------------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Display all employees
6. Quit the program

Enter your choice: 6
The data has been saved.

Goodbye!

"""
