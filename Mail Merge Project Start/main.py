#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

placeholder = "[name]"
with open("Input/Names/invited_names.txt") as name_data:
    names = name_data.readlines()



# with open("Input/Letters/starting_letter.txt", mode="r")as letter_data:
#     letter = letter_data.read()
#print(letter)

with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()
new_content = ""
for name in names:
    name = name.strip()
    new_letter = letter.replace(placeholder, name)

    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as writing_file:
        writing_file.write(new_letter)



# written = open("Input/Letters/starting_letter.txt", mode="w")
# written.write(new_content)
# written.close()





