def vowels():
    a=input("Please type a sentence: ")
    return sum(map(a.lower().count,"aeiou"))

def overlapping_string_count():
    s=input("Please type a sentence: ")
    return len(re.findall('(?=bob)',s))

def find_long_alpha():
    s="Longestsubstringinalphabeticalorder"
    a=''
    b=''
    c=''
    for i in s:
        if a<=i:
            a=i
            b+=a
            if len(b)>len(c):
                c=b
        else:
            a=i
            b=a
    return c
