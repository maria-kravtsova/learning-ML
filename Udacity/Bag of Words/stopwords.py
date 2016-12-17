from nltk.corpus import stopwords

# count all stopwords
sw = stopwords.words('english')
count = 0
for w in sw:
    count = count + 1

print(count)
