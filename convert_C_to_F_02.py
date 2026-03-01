# FILE NAME - convert_C_to_F_02.py

# NAME: Casey Tatar
# DATE: 3/1/2026
# BRIEF DESCRIPTION:  Building off convert_C_F_01.py this module will first ask the user if they would like to convert from Celsius to Fahrenheit or from Fahrenheit to Celsius. Once the conversion has been established the user is prompted to enter a temperature and the equivalent temperature is output to the screen.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    temp_convert()
  
def temp_convert():
    
    print('===== Temperature Converter =====')
    print()
    print('1. Convert from Celsius to Fahrenheit')
    print('2. Convert from Fahrenheit to Celsius')

    answer = input(' \nPlease choose from the above menu: ')
    temp = float(input('Enter a temperature to convert: '))

    if answer == '1':
        convert_C_to_F = float(temp * (9/5) + 32)

        print()
        print(f'{temp:.1f} degrees Celsius is {convert_C_to_F:.1f} degrees Fahrenheit.')
        
    else: 
        convert_F_to_C = float((temp - 32) * 5/9)

        print()
        print(f'{temp:.1f} degrees Fahrenheit is {convert_F_to_C:.1f} degrees Celsius.')

main()









########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

I learned how to use spacing correctly to make sure that it matches the output. 





'''