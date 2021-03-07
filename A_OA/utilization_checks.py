'''
A new Amazon-developed scaling computing system checks the average utilization of the computing system every second while it monitors. It implements an autoscale policy to add or reduce instances depending on the current load as described below. Once an action of adding or reducing the number of instances is performed, the system will stop monitoring for 10 seconds. During that time, the number of instances does not change.

Average utilization < 25%: An action is instantiated to reduce the number of instances by half if the number of instances is greater than 1 (take the ceiling if the number is not an integer). If the number of instances is 1, take no action.
25% <= Average utilization <= 60%: Take no action.
Average utilization > 60%: An action is instantiated to double the number of instances if the doubled value does not exceed 2* 10^8. If the number of instances exceeds this limit upon doubling, perform no action.
Given an array of integers that represent the average utilization at each second, determine the number of instances at the end of the time frame.
'''


import math
def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """     
    r=len(averageUtil)
    i=0
    while(i<r):
        print(i)
        if(averageUtil[i]<25):
            if(instances==1):
                i+=1
            else:
                instances=math.ceil(instances/2)
                i+=11
        elif(averageUtil[i]>=25 and averageUtil[i]<=60):
            i+=1
        else:
            if(instances*2<=200000000):
                instances*=2
                i+=11
            else:
            
                i+=1
    return instances