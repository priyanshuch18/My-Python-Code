str1 = "Apple"

all_freq = {}

for i in str1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        
        
print("Result:"+ str(all_freq) )
