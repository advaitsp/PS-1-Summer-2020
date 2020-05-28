import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# The findall() Function
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# The search() function
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# The split() Function
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# The sub() Function
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)