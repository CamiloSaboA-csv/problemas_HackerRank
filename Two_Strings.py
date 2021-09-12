from collections import Counter
def twoStrings(s1, s2):
    # Write your code here
    a=Counter(s1)
    b=Counter(s2)
    union=a&b
    if union=={}:
        return "NO"
    else: return "YES"


a='hi'
b='world'

twoStrings(a,b)