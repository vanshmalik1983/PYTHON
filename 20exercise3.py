ques = [

    ["which is national language?","hindi","english","marathi","urdu",1],
    ["which is national language?","hindi","english","marathi","urdu",1],
    ["which is national language?","hindi","english","marathi","urdu",1],
    ["which is national language?","hindi","english","marathi","urdu",1],
    ["which is national language?","hindi","english","marathi","urdu",1],
    ["which is national language?","hindi","english","marathi","urdu",1],
    ["which is national language?","hindi","english","marathi","urdu",1],
]
levels = [1000 , 2000 , 3000 , 5000 ,10000 , 20000 ,40000 , 80000 , 160000 ,320000 ,640000 , 1250000, 2500000 ,5000000 ,100000000, 70000000 ]
money = 0
for i in range(0,len(ques)):
    ques = ques[i]
    print(f"ques for RS.{levels[i]}")
    print(f"a.{ques[1]}              b.{ques[2]}")
    print(f"c.{ques[3]}              d.{ques[4]}")
    reply = int(input("Enter your answer(1-4)"))
    if(reply == ques[-1]):
        print(f"Correct answer , you won RS. {levels[i]}")
        if(i==4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer!!")
        break


print("your winning amount {money}")