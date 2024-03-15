# open("file", "mode", "buffering")
# mode: r, w, a, r+, w+, a+
# r = read
# w = write
# a = append
# r+ = read and write
# w+ = write and read
# a+ = append and read
# buffering: 0, 1, >1
# 0 = no buffering means it will write to the file when it is closed (default)
# 1 = line buffering means it will write to the file when it sees a new line (not recommended)
# >1 = buffering in bytes means it will write to the file when it reaches the specified number of bytes (recommended)

# open a file and read it line by line
'''
with open ("data.txt", "r") as file:
    line = file.readline()
    
    while line:
        print(line.strip())
        line = file.readline()



# create a file and write to it
outfile = open("data.txt", "w")
outfile.write("Hello World\n")
outfile.write("John Doe\n")
outfile.close()

# another way to create a file and write to it
# with is good because it will automatically close the file for you
with open("data.txt", "w") as outfile:
    outfile.write("Hello World\n")
    outfile.write("John Doe\n")

inFile = open("data.txt", "r")
# reads the entire file
#all_contents = inFile.read() 
#read line only
line_contents = inFile.readline()
#print(all_contents)
print(line_contents)
inFile.close()


# only print 2nd line in file 
sales_file = open("sales_file.txt", "r")

total = 0

for line in sales_file:
    amount = int(line)
    total += amount
    
print(total)

sales_file.close()
'''

# only print 2nd line in file with while loop
sales_file = open("sales_file.txt", "r")
line = sales_file.readline()
total = 0

while line != "":
    total += int(line)
    line = sales_file.readline()
    
print(total)
sales_file.close()