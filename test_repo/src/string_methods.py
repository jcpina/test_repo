'''
Created on Nov 25, 2022

@author: jcp
'''

name = "monsieur pina jean charles"

print("The raw variable name: " + name)
print("The raw variable name with a tab: \t" + name)
print("variable name with name.title(): \t" + name.title())
print("variable name with name.upper(): \t" + name.upper())
print("variable name with name.lower(): \t" + name.lower())

#Stripping whitespace
language = " python "
print("The raw variable language\n" + language)
print("The variable language with language.rstrip\n" + language.rstrip())
print("The variable language with language.lstrip\n" + language.lstrip())