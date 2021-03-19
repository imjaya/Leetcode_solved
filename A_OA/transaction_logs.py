def processLogFile(logs, threshold):
    """
    :type logs: List[str]
    :type threshold: int
    :rtype: List[str]
    """
    users={}
    for i in range(0,len(logs)):
        p=logs[i].split(" ")
        if(p[0]==p[1]):
            if(p[0] in users):
                users[p[0]]+=1
            else:
                users[p[0]]=1
        else:
            if(p[1] in users):
                users[p[1]]+=1
            else:
                users[p[1]]=1
            
            if(p[0] in users):
                users[p[0]]+=1
            else:
                users[p[0]]=1
                
    # print(users)
    result=[]
    for i in users:
        print(users[i])
        if(users[i]>=threshold):
            result.append(i)
    print(result)
    return(result)
            
                    