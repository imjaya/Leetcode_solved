#make a dict of bigger string and then for every word in the second string remove the count in the dict, return the list of remaining words
def missingWords(s, t):
    ls = s.split(' ')
    lt = t.split(' ')
    counter = collections.Counter(lt)
    res = []
    for s in ls:
        if s in counter:
            counter[s] -= 1
            if counter[s] == 0:
                del counter[s]
        else:
            res.append(s)
    return " ".join(res)