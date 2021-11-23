'''
Given an arry, reverse it
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
