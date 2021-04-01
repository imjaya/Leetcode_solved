s="aaabbbacd"
while True:
    i, j = 0, 0
    new_string = ""  
    while i < len(s):
        # print(s)
        j = i
        while j + 1 < len(s) and s[j + 1] == s[i]:
            j += 1
        
        cnt = j - i + 1 
        if cnt < 3:
            new_string += s[i : j + 1]
        # print(s[i : j + 1])
        i = j + 1  
    if len(s) == len(new_string): 
        break
    elif len(s) > len(new_string):
        s = new_string
    else:  
        assert False
print(s)  



######################################################################3
s="aabbccddeeedcba"
stack = []
stack.append([s[0], 1])

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if stack[-1][1] >= 3:
            stack.pop()
        if stack and stack[-1][0] == s[i]:
            stack[-1][1] += 1
        else:
            stack.append([s[i], 1])
    else:
        stack[-1][1] += 1
        
# handle end
if stack[-1][1] >= 3:
    stack.pop()
    
out = []
for ltrs in stack:
    out += ltrs[0] * ltrs[1]
print(''.join(out))
