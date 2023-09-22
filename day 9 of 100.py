# Function to count vowels in a string
def count_vowels(string):
    #Define a set of vowels
    vowels = "aeiouAEIOU"

    #Initialize a count variable to 0
    count = 0

    #Iterate through each character in the string 
    for char in string:
        #check if the character is a vowel
        if char in vowels:
            count += 1

    return count
#Input a string from the user 
input_string = input("Enter a string: ")

#Call the functiion to count vowels and print the result
vowel_count = count_vowels(input_string)
print("number of vowels in the string:", vowel_count) 