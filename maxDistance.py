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
