def solution(N, artifacts, searched):
    # write your code in Python
    search = set(searched.split(' '))
    
    artifacts = artifacts.split(",")
    
    complete = 0
    incomplete = 0
    
    for artifact in artifacts:
        rect = artifact.split(' ')
        
        rect_cord = []
        
        if len(rect) >= 2:
            if rect[0][1] == rect[1][1]:
                x = int(rect[0][:-1])
                y = int(rect[1][:-1])
                for i in range(x, y + 1):
                    rect_cord.append(str(i)+rect[0][-1])
            elif rect[0][:-1] == rect[1][:-1]:
                x = ord(rect[0][-1])
                y = ord(rect[1][-1])
                for i in range(x, y + 1):
                    rect_cord.append(rect[0][:-1] + chr(i))
            else:
                x = rect[0][:-1]
                y = rect[1][:-1]
                a = rect[0][-1]
                b = rect[1][-1]
                rect_cord = [x+a, y+b, x+b, y+a]
        elif len(rect) == 1:
            rect_cord = rect[0]
        parts = len(rect_cord)
        for cord in rect_cord:
            if cord in search:
                parts -= 1
        if parts == 0: complete += 1
        elif parts != len(rect_cord): incomplete += 1
        
    return [complete, incomplete]