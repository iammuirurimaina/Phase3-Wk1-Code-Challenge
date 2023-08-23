def consonant_value():
   
    alphabet_dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #place each character in alphabet in the dictionary with its index as the value and the character as the index
    for index, char in enumerate(alphabet, start=1):
        alphabet_dict[char] = index

    print("Alphabet Dictionary:", alphabet_dict)

    
    input_word = input("Enter a lowercase word: ")
    vowels = "aeiou"

    
    max_value = 0
    max_consonant = ""

   
    for char in input_word:
        
        if char not in vowels and char in alphabet_dict:
            value = alphabet_dict[char]
           
            if value > max_value:
                max_value = value
                max_consonant = char

   
    if max_consonant:
        print(f"The consonant with the largest value is '{max_consonant}' with a value of {max_value}.")
    else:
        print("No consonants found in the input word.")


consonant_value()
