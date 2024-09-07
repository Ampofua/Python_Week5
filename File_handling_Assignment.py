# Create a text file and open it in write mode
with open("my_file.txt", "w") as file:
    file.write("I am attracted to the color brown \n")
    file.write("Funny enough I dont have any brown outfits \n")
    file.write("3, 23 are my favorite prime numbers \n")
    file.write("I want to excel in my python studies")


# File reading and display
with open("my_file.txt" , "r") as file:
    content = file.read()
    
print("File contents:\n")
print(content)



#Implement error handling
try:
    with open("my_file.txt", "w") as file:
      file.write("I am attracted to the color brown \n")
      file.write("Funny enough I dont have any brown outfits \n")
      file.write("3, 23 are my favorite prime numbers \n")
      file.write("I want to excel in my python studies")


    with open("my_file.txt" , "r") as file:
      content = file.read()
    
    print("File contents:\n")
    print(content)

except FileNotFoundError as fnf_error:
    print(f"Error: {fnf_error}. The file could not be found.")

except PermissionError as perm_error:
    print(f"Error: {perm_error}. You do not have permission to access this file.")

except Exception as error:
    print(f"An unexpected error occurred: {error}")

finally:
    print("Operation completed, whether successful or not.")
    
