from collections import Counter

def checkMagazine(magazine, note):
#     # Write your code here
    a = Counter(magazine)
    b = Counter(note)
    return "Yes" if ( a & b ) == b else "No"

#     from collections import Counter
#     def ransom_note(magazine, rasom):
#         return (Counter(rasom) - Counter(magazine)) == {}





x,y=['give', 'me', 'one', 'today', 'night'],['give', 'one', 'grand', 'today']
#x,y=['two', 'times', 'three', 'is', 'not', 'four'],['two', 'times', 'two', 'is', 'four']
#checkMagazine(x,y)
