non_trivial_answers = []

for i in range(1,50):
    for j in range(10,100):
        for k in range(1,10):
            if i == j:
                continue
            tempi=i
            tempj=j
            tempfraction = i/j
            if (str(tempi).find(str(k)) != -1 and str(tempj).find(str(k)) != -1):
                #print(tempi,tempj,tempfraction,k)
                tempi = str(tempi).replace(str(k),"",1)
                tempj = str(tempj).replace(str(k),"",1)
                if tempi == "" or tempj == "":
                    #print("nothing in tempi or tempj",tempi,tempj)
                    continue
                tempi = float(tempi)
                tempj = float(tempj)

                if tempi == 0 or tempj == 0:
                    #print("0 in tempi or tempj",tempi,tempj)
                    continue

                tempfraction = tempi/tempj
                if tempi/tempj == i/j:#str(tempfraction).replace(str(k),""):
                    print(f"found something: {tempi}/{tempj}={tempfraction}")
                    non_trivial_answers.append([tempi,tempj])
                    break
