import collections
def countLevelUpPlayers(cutOffRank, num, scores):
    count = collections.Counter(scores)
    ans, curRank = 0, 1
    for k, v in sorted(count.items(),reverse=True):
        if (curRank > cutOffRank):   #r k==0 if one testcase fails
            break
        ans += v
        curRank += v
    return ans


###############################################################
#Better Approach without using collection
###############################################################
def countLevelUpPlayers(cutOffRank, num, scores):
    if(cutOffRank == 0):
        return 0
    cache = [0]*101
    for n in scores:
        cache[n]+=1

    res = 0
    for i in range(100,0,-1):
        if (cutOffRank <= 0):
            break
        cutOffRank -= cache[i]
        res += cache[i]
        
    return res