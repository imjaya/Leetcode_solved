import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if(len(nums1)<=len(nums2)):
            X=nums1.copy()
            Y=nums2.copy()
        else:
            X=nums2.copy()
            Y=nums1.copy()
            
        x=len(X)
        y=len(Y)
        start=0
        end=x
        
        while(start<=end):
            partX=int((start+end)/2)
            partY=int((x+y+1)/2)-partX
            
            if(partX==0):
                maxLeftX=-math.inf
            else:
                maxLeftX=X[partX-1]
                
            if(partX==x):
                minRightX=math.inf
            else:
                minRightX=X[partX]
            
            if(partY==0):
                maxLeftY=-math.inf
            else:
                maxLeftY=Y[partY-1]
                
            if(partY==y):
                minRightY=math.inf
            else:
                minRightY=Y[partY]
                
                
            if (maxLeftX <= minRightY and maxLeftY <= minRightX):
                if ((x + y) % 2 == 0):
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
                else:
                    return max(maxLeftX, maxLeftY)
                
            elif (maxLeftX > minRightY):
                end = partX - 1
            else:
                start = partX + 1
            
        
                
            
        
            
        