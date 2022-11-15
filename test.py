import re


s='Archaea;Euryarchaeota;Methanobacteria;Methanobacteriales;Methanobacteriaceae;Methanobrevibacter;Methanobrevibacter smithii'

answer = re.findall('\w+', s)
print(answer)


i=0
for i in range (0,len(answer)-2):
    print('\t')

print(answer[i],answer[i+1],answer[i+2])

word_count=0
while(word_count < len(answer)-2): 
    word_count+=1

print(answer[word_count-1], answer[word_count],answer[word_count+1])
