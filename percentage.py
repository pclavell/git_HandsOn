myseq=input("Introduce your sequence:")
total=len(myseq)
factor= 100/total
count = {}

for i in myseq: #loop to count each letter
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for key in count:
    print(key, count[key]*factor)

