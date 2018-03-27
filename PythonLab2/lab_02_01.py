def anagram_dict(words):
    a_list = {}
    for word in words:
        sword = ''.join(sorted(word))
        if sword not in a_list:
            a_list[sword]=[]
        a_list[sword].append(word)
    #a_list = {k:a_list[k] for k in a_list if len(a_list[k])>=2}
    a_list = {k: v for k,v in a_list.items() if len(v)>=2}
    return a_list
words={}
delimiters = [ ',', '.', '?', '!', ':']
file="file.txt"
with open(file,'r') as f:
    for line in f:
        for delimiter in delimiters:
            line = line.replace(delimiter, ' ')
        for word in line.split():
            words[word]=1
x=anagram_dict(words)
for row in x:
    print(x[row])