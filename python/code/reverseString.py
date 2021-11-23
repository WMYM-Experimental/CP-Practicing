'''
Given an arry, reverseit
'''

def reverseString(text):
  #reverse a string
  text = list(text)
  text = text[::-1]
  return "".join(text)
