def makeAnagram(a, b):
    # Write your code here
    from collections import Counter
    a,b=list(sorted(a)),list(sorted(b))
    a_count=Counter(a)
    b_count=Counter(b)
    x=((b_count-a_count)+(a_count-b_count)).values()
    x=sum(x)
    return x










a,b= 'faacrxzwscanmligyxyvym','jaaxwtrhvujlmrpdoqbisbwhmgpmeoke'
#a,b='aaaaaaabc','aaaaabde'
x=100000000

x=makeAnagram(a,b)

print(x)
