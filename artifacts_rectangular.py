from copy import deepcopy
alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
artifacts="1A 1B,2C 2C"
searched="1B"
N=3
temp_artifact_list=list(map(str,artifacts.split(",")))
#artifact_list=list(map(str,artifacts.split(" ")))
artifact_list=[]
for i in temp_artifact_list:
    artifact_list.append(i.split())
artifact_list=[j for sub in artifact_list for j in sub]
searched_list=list(map(str,searched.split()))
print(artifact_list)
print(searched_list)
area=[[0 for _ in range(N)] for _ in range(N)]
count=1
top_row=0
top_column=0
bottom_row=0
bottom_column=0

for i in range (0,len(artifact_list)-1,2):
    top_row=int(artifact_list[i][:-1])-1
    top_column=alphabets.index(artifact_list[i][-1])
    bottom_row=int(artifact_list[i+1][:-1])-1
    bottom_column=alphabets.index(artifact_list[i+1][-1])
    print(top_row,top_column,bottom_row,bottom_column)
    if(top_row==bottom_row):
        for i in range(0,bottom_column-top_column+1):
            area[top_row][top_column+i]=count
        
    elif(top_column==bottom_column):
        for i in range(0,bottom_row-top_row+1):
            area[top_row+i][top_column]=count
    else:
        area[top_row][top_column]=count
        area[top_row+1][top_column]=count
        area[top_row][top_column+1]=count
        area[bottom_row][bottom_column]=count
    count=count+1
print(area)        
area_copy=deepcopy(area)
for i in searched_list:
    row=int(i[0])
    column=alphabets.index(i[1])
    #print(row,column)
    area_copy[row-1][column]="X"
print(area_copy)
#print(area)
area = [j for sub in area for j in sub]
area_copy = [j for sub in area_copy for j in sub]
completed=0
partial=0
for i in range(count-1,0,-1):
    #print(i)
    #print("area count",i,area.count(str(i)))
    #print("area copy count",i,area_copy.count(str(i)))
    if (area_copy.count(i)==0):
        completed+=1
    elif(area_copy.count(i)!=area.count(i)):
      partial+=1
    
print(completed, partial)