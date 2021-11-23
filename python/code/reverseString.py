'''
Given an string, reverse it
'''

#long way
def reverse_string(text):
  #reverse a string
  text = list(text)
  text = text[::-1]
  return "".join(text)


#second way shorter
def reverse_string(text):
  #reverse a string
  return text[::-1]
  

#traditional way
def reverse_string(text):
  #reverse a string
  for char in range(len(text)-1,-1,-1):
    return text[char]

  
 #list comprenhension and reversed list way way
def reverse_string(text):
  #reverse a string
  return ''.join(char for char in list(reversed(text)))
