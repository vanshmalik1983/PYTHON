st = input("Enter message : ")
words = st.split(" ")
coding = True
if(coding):
    nwords = []
    for word in words:
     if(len(st)>=3):
        r1 = "dsb"
        r2 = "hjk"
        stnew = r1+word[1:] +word[0]+r2
        nwords.append(stnew)
    print(" ".join(nwords))

else:
    nwords.append(words[::-1])
    print(" ".join(nwords))
    