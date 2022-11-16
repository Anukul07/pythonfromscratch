
# expand tabs:
""" print('Hello world')
print(("\t World").expandtabs(tabsize=16)) """

# print("Hello\b World")
# raw string :
# print(r"Hello\nWorld")

# print(r"Hello\world")

""" """ """ a ="Hello\tWorld"
# print(dir(a)) """ """
# re.sub(" ", "",a)
# print(a.isdigit())
# print(a.isidentifier())
print(a.rstrip())
print(a.lstrip())
print(a.capitalize())
print(a.replace("H", 'P'))
print(a.replace(" ","")) 
print(a.expandtabs(tabsize=16)) """

""" a = "Hello World"
b = a.strip()
print(b) """

# Escape character 
""" txt = "We are the so-called \"Vikings\" from the north."
print(txt) """

# Zeros fill
""" txt = "50"
x = txt.zfill(10)
print(x)
 """
# slicing :
""" a= "hello world" 
print(a[0:7]) """


x,y = int(input("Enter a number")), input("Enter a string")
print(x,y)