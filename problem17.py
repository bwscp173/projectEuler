import inflect #pip install inflect


engine=inflect.engine()
total = 0
for i in range(1,1001):
    sentense = engine.number_to_words(i).replace(",","").replace("-","").replace(" ","")
    total += len(sentense)

print(total)