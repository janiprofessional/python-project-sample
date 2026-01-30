import re
string = " P Y T H O N"
spaces = re.compile(r'\s+')
result = re.sub(spaces,"",string)
print("remove spaces with reg ex",result)
# output: remove spaces with reg ex PYTHON

str = "C O D I N G"
str = str.replace(" ","")
print("remove space with replace ",str)
# output: remove space with replace  CODING