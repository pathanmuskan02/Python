# Strings
str1 = '''If you trouble the trouble,
trouble will troubles you,
I am not the trouble, I am the truth ---by JAI Balayyaa@9999'''
lower = str1.lower()
print(lower)
capitalize = str1.capitalize()
print(capitalize)
print(str1.title())
upper = str1.upper()
print(upper)

# Checking methods
print(str1.islower())
print(str1.isupper())
print(str1.isalnum())
print("12nhj3g6gnjj8".isalnum())
print("23457".isdigit())
print(str1.count("trouble"))
print(str1)
print(str1.strip()) # removes starting and ending spaces of string and it will comes into lists
print(str1.lstrip()) # removes left side spaces of string 
print(str1.rstrip()) # removes right side  spaces of string 
words = str1.split()
print(type(words))

# Count the words in a string
str2 = "My name is muskan"
words = str2.split()
print(words)
print(len(words))

# Converts list into string
str2 = "My name is muskan"
combined_string = "".join(words)
print(combined_string)