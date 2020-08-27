import fileinput

import math
#from math import acos, sin, cos, radians, floor
from collections import defaultdict
RADIUS_MILES = 3963

class DestinationCalculator:
    def __init__(self):
        self.l1=[]
        self.l2=[]
        self.city_dict={}
    
    def process(self, A: str) -> str:
        
        
        if(A.startswith("LOC")):
            L=A.split(":")
            #R=A[4:-1].index(':')+4
            #P=A[8:-1].index(':')+8
            #print(R,P)
            Lat=L[2]
            Lon=L[3]
            city=L[1]
            self.city_dict[city]=Lat,Lon
            #print(self.city_dict)
            return(city)
        
        else:
            L=A.split(":")
            ticket=L[1]
            city_A=L[2]
            city_B=L[3]
            Lat_A=float(self.city_dict[city_A][1])
            Lat_B=float(self.city_dict[city_B][1])
            Lon_A=float(self.city_dict[city_A][0])
            Lon_B=float(self.city_dict[city_B][0])
            delta_phi=abs(math.radians(Lat_A)-math.radians(Lat_B))
            angular_distance=math.acos((math.sin(math.radians(Lon_A))*math.sin(math.radians(Lon_B)))+(math.cos(math.radians(Lon_A))*math.cos(math.radians(Lon_B))*math.cos(delta_phi)))
            distance=RADIUS_MILES*angular_distance
            distance=int(distance)
            return(ticket+":"+city_A+":"+city_B+":"+str(distance))
        # line_list=line.split(":")
        # print(line_list)
        # if(line_list[0]=="LOC"):
        #     if not self.l1:
        #         self.l1=list(map(float,line_list[2:]))
        #         return(line_list[1])
        #     else:
     #         self.l2=list(map(float,line_list[2:]))
        #         return(line_list[1])
        # else:
        #     delta_phi=abs(radians(self.l1[1])-radians(self.l2[1]))
        #     angular_distance=acos((sin(radians(self.l1[0]))*sin(radians(self.l2[0])))+(cos(radians(self.l1[0]))*cos(radians(self.l2[0]))*cos(delta_phi)))
        #     distance=RADIUS_MILES*angular_distance
        #     line=line[5:]
        #     self.l1=self.l2
        #     self.l2=[]
        #     return(line+":"+str(distance).split(".")[0])

            
if __name__ == "__main__":