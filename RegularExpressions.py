#building an email address text scrapper. a program that looks for email addresses among a list of email addresses
#this is called regular expression

import re

pattern = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

text = "hi, my name is olly and i live in new haven. this is \
       my email address - oluoma_u@gmail.com, you can also email me via oluomachizaram@gmail.com"

result = pattern.findall(text)

print(result)