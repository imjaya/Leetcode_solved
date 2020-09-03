import glob
with open('merge.txt') as fh:
    for line in fh:

        # reading each word
        a=line.split()

        for word in a:

            if(word=='"GET'):
                p=a[a.index(word)-len(a)+1]
                if(".txt" in p):
                    print(a[a.index(word)-len(a)+3])