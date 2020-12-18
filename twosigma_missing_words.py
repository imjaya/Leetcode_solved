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