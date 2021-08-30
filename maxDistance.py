'''
Fiven a text and a subtext always inside of the text.
Found the max distance (left or right) between the start of the text to the start of the subtext
or the end of the subtext to the end of the subtext

text and subtext must be in English alphabet
'''

def maxDistance(text,subText):
    nText = len(text)
    nSub = len(subText)
    if text.isalpha() and subText.isalpha():
        if 1 <= nText <= 2147483647 or 1 <= nSub <= nText:
            if nSub == 1 :
                a = text.find(subText)
                b = nText - text.rfind(subText) - a + 1
                arrayLong = [a, b]
                return max(arrayLong)
            else:
                a = text.find(subText)
                b = nText - text.rfind(subText) - a
                arrayLong = [a, b]
            return max(arrayLong)
        else:
            return -1
    else:
        return -1
