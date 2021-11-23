'''
Given an string, reverse it
'''

#long way
def reverseString(text):
  #reverse a string
  text = list(text)
  text = text[::-1]
  return "".join(text)


#second way shorter
def reverseString(text):
  #reverse a string
  return text[::-1]
  

#traditional way
def reverseString(text):
  #reverse a string
  for char in range(len(text)-1,-1,-1):
    return text[char]

  
 #list comprenhension and reversed list way way
def reverseString(text):
  #reverse a string
  return ''.join(char for char in list(reversed(text)))
