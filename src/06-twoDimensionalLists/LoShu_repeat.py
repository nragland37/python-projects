#**************************************************************************************************** 
#
#       This program updates the LoShu.py program to ask the user if they would like to try again.
# 
#****************************************************************************************************

def getInput(square):
    print('Enter all values: ')
    
    for i in range(len(square)):
        print(f'\n{"Row " + str(i):^11}\n{"-" * 11}')
        for j in range(len(square[i])):
            success = False
            
            while not success:
                try:
                    value = int(input('enter: '))
            
                    if 1 <= value <= 9:
                        square[i][j] = value
                        success = True
                    else:
                        raise ValueError('Value must be between 1 and 9.')
                except ValueError as e:
                    print(f'\nError: {e}\n')
                    
    return square

#****************************************************************************************************

def checkLeftDiagnol(square):
    return sum([square[i][i] for i in range(len(square))]) == 15

#****************************************************************************************************

def checkRightDiagnol(square):
    return sum([square[i][2 - i] for i in range(len(square))]) == 15

#****************************************************************************************************

def checkRows(square):
    return all([sum(r) == 15 for r in square]) 
       
#****************************************************************************************************

def checkCols(square):
    return all([sum([square[r][c] for r in range(len(square))]) == 15 for c in range(len(square[0]))])

#****************************************************************************************************

def checkLoShu(square):
    checks = [
        checkLeftDiagnol(square), 
        checkRightDiagnol(square), 
        checkRows(square), 
        checkCols(square)
    ]
    
    return all(checks) 

#****************************************************************************************************

def display(square):
    print(f'\n{"Square:":^11}\n{"-" * 11}')
    
    for r in square:
        for c in r:
            print(f'{c:<5}', end='')
        print() 
        
#****************************************************************************************************

def main():
    ch = 'y'
    while ch.lower() == 'y':
        square = [[0] * 3 for _ in range(3)]
        square = getInput(square)
        display(square)
        
        if checkLoShu(square):
            print('\nThis is a Lo Shu Magic Square.')
        else:
            print('\nThis is not a Lo Shu Magic Square.')
            
        ch = input('\nWould you like to try again? (y/n): ')
        while ch.lower() not in ['y', 'n']:
            print('Invalid input. Try again.')
            ch = input('\nWould you like to try again? (y/n): ')

#****************************************************************************************************

if __name__ == '__main__':
    main()

#****************************************************************************************************
'''

Enter all values: 

   Row 0   
-----------
enter: 1  
enter: 2
enter: 3

   Row 1   
-----------
enter: 3
enter: 2
enter: 1

   Row 2   
-----------
enter: 1
enter: 2
enter: 3

  Square:  
-----------
1    2    3    
3    2    1    
1    2    3    

This is not a Lo Shu Magic Square.

Would you like to try again? (y/n): y
Enter all values: 

   Row 0   
-----------
enter: 4
enter: 9
enter: 2

   Row 1   
-----------
enter: 3
enter: 5
enter: 7

   Row 2   
-----------
enter: 8
enter: 1
enter: 6

  Square:  
-----------
4    9    2    
3    5    7    
8    1    6    

This is a Lo Shu Magic Square.

Would you like to try again? (y/n): n

'''