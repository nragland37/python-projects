# try exceptions with files
"""
try:
    with open("sales_file.txt", "r") as sales_file:
        total = 0
        
        for line in sales_file:
            amount = int(line)
            total += amount
            
        print(total)
        
except FileNotFoundError:
    print("File not found")

    
fileName = input("Enter file name: ")

try:
    inFile = open(fileName, "r")
    
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)
    
"""

try:
    total = 0
    infile = open("sales_file.txt", "r")
    for line in infile:
        amount = float(line)
        total += amount
    infile.close()

except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Non-numeric data found in the file.")
except Exception as e:
    print(e)
# optional - runs if no exceptions are caught
else:  
    print(total)
# optional - always runs whether there is an exception or not
finally:  
    print("Done")
