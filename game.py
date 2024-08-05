from tkinter import *
print("Hello! Welsome to G.A.M.E (Graphical Adventure maze Experience)! \nA fun and interesting adventure from a jungle you find yourself stranded in, to back home!")
print("Hope you'll enjoy this experience! However, before we get started, here are some rules:")
print(" 1.You will have to pass through 3 stages and make smart choices to survive. \n 2.Each stage will end with a small puzzle that you have to figure out to move on to the next stage. \n 3.You have 3 lives at the start of the game, however, whenever you make a wrong choice, your lives will decrease. \n 4.Crossing each puzzle will get you a new life. \n 5.Categories will be given to you at the beginning of each puzzle. Choose wisely a topic which you're well versed in, as all questions will pertain to it. \n 6.Each stage will have a few difficult choices to be made, but look at the clues hidden within the question to be able to make it through.")
lives=3
def myChoice():
    root=Tk()
    label1=Label(root, text="Here are some topics that you can choose from. Please choose wisely as these are the questions you'll be quizzed on.",background="blue")
    label1.pack()  
    def Movies(): 
        label1.pack_forget();but1.pack_forget();but2.pack_forget();but3.pack_forget();but4.pack_forget();but5.pack_forget();but6.pack_forget()
        lab1=Label(root, text="Enter the answer here:")
        lab1.pack()
        ent1= Entry(root, width=25, borderwidth=5)
        ent1.pack()
        can=Canvas(root, height=700, width=600, bg="#E87AA2")
        coord=10,10,580,580
        arc=can.create_oval(coord, fill="red")
        lab2=Label(root, text="Which film written, directed, and produced by James Cameron \n went on to become the highest-grossing film of its time?")
        lab2.place(x=135,y=340)
        def myClick():
            text=ent1.get().lower()
            if(text=="titanic"):
                coord1=60,60,530,530
                arc1=can.create_oval(coord1, fill="#4432B9")
                lab2.config(text="What is the current highest-grossing film of all time?")
                lab2.place(x=145,y=350)
                button1.config(command=myClick1)
            else:
                ent1.insert(END, "Try again")
        button1=Button(root, text="Check", command=myClick)
        button1.pack()
        def myClick1():
            text=ent1.get().lower()
            if(text=="avatar"):
                coord2=110,110,480,480
                arc2=can.create_oval(coord2, fill="#E6F773")
                lab2.config(text="Which movie is the first non-English language film \n to win an Oscar for Best Picture?")
                button1.config(command=myClick2)
            else:
                ent1.insert(END, "Try again")
        def myClick2():
            text=ent1.get().lower()
            if(text=="parasite"):
                coord3=160,160,430,430
                arc3=can.create_oval(coord3, fill="#73F7B1")
                lab2.config(text="1 Life increased.")
                lab2.place(x=255,y=350)
                global lives; lives+=1
            else:
                ent1.insert(END, "Try again")
        can.pack()
    def Sports():
        label1.pack_forget();but1.pack_forget();but2.pack_forget();but3.pack_forget();but4.pack_forget();but5.pack_forget();but6.pack_forget()
        lab1=Label(root, text="Enter the answer here:")
        lab1.pack()
        ent1= Entry(root, width=25, borderwidth=5)
        ent1.pack()
        can=Canvas(root, height=700, width=600, bg="#E87AA2")
        coord=10,10,580,580
        arc=can.create_oval(coord, fill="red")
        lab2=Label(root, text="The Olympics are held every how many years?(in words)")
        lab2.place(x=155,y=350)
        def myClick():
            text=ent1.get().lower()
            if(text=="four"):
                coord1=60,60,530,530
                arc1=can.create_oval(coord1, fill="#4432B9")
                lab2.config(text="What is the only sport to be played on the moon? \n Golf, tennis, or hockey?")
                button1.config(command=myClick1)
            else:
                ent1.insert(END, "Try again")
        button1=Button(root, text="Check", command=myClick)
        button1.pack()
        def myClick1():
            text=ent1.get().lower()
            if(text=="golf"):
                coord2=110,110,480,480
                arc2=can.create_oval(coord2, fill="#E6F773")
                lab2.config(text="Who won the 2019 ICC Cricket World Cup?")
                lab2.place(x=175,y=350)
                button1.config(command=myClick2)
            else:
                ent1.insert(END, "Try again")
        def myClick2():
            text=ent1.get().lower()
            if(text=="england"):
                coord3=160,160,430,430
                arc3=can.create_oval(coord3, fill="#73F7B1")
                lab2.config(text="1 Life increased.")
                lab2.place(x=255,y=350)
                global lives; lives+=1
            else:
                ent1.insert(END, "Try again")
        can.pack()
    def Music():
        label1.pack_forget();but1.pack_forget();but2.pack_forget();but3.pack_forget();but4.pack_forget();but5.pack_forget();but6.pack_forget()
        lab1=Label(root, text="Enter the answer here:")
        lab1.pack()
        ent1= Entry(root, width=25, borderwidth=5)
        ent1.pack()
        can=Canvas(root, height=700, width=600, bg="#E87AA2")
        coord=10,10,580,580
        arc=can.create_oval(coord, fill="red")
        lab2=Label(root, text="Which Marvel movie’s soundtrack won two Grammys?")
        lab2.place(x=145,y=340)
        def myClick():
            text=ent1.get().lower()
            if(text=="black panther"):
                coord1=60,60,530,530
                arc1=can.create_oval(coord1, fill="#4432B9")
                lab2.config(text="Robert Plant was the lead singer of which rock band?")
                button1.config(command=myClick1)
            else:
                ent1.insert(END, "Try again")
        button1=Button(root, text="Check", command=myClick)
        button1.pack()       
        def myClick1():
            text=ent1.get().lower()
            if(text=="led zeppelin"):
                coord2=110,110,480,480
                arc2=can.create_oval(coord2, fill="#E6F773")
                lab2.config(text="Folklore, Red and 1989 are albums by which singer?")
                lab2.place(x=155,y=340)
                button1.config(command=myClick2)
            else:
                ent1.insert(END, "Try again")
        def myClick2():
            text=ent1.get().lower()
            if(text=="taylor swift"):
                coord3=160,160,430,430
                arc3=can.create_oval(coord3, fill="#73F7B1")
                lab2.config(text="1 Life increased.")
                lab2.place(x=255,y=350)
                global lives; lives+=1
            else:
                ent1.insert(END, "Try again")
        can.pack()
    def Countries():
        label1.pack_forget();but1.pack_forget();but2.pack_forget();but3.pack_forget();but4.pack_forget();but5.pack_forget();but6.pack_forget()
        lab1=Label(root, text="Enter the answer here:")
        lab1.pack()
        ent1= Entry(root, width=25, borderwidth=5)
        ent1.pack()
        can=Canvas(root, height=700, width=600, bg="#E87AA2")
        coord=10,10,580,580
        arc=can.create_oval(coord, fill="red")
        lab2=Label(root, text="By size, what is the smallest country in the world?")
        lab2.place(x=155,y=340)
        def myClick():
            text=ent1.get().lower()
            if(text=="vatican city"):
                coord1=60,60,530,530
                arc1=can.create_oval(coord1, fill="#4432B9")
                lab2.config(text="In which country would you find Mt Etna?")
                lab2.place(x=175,y=350)
                button1.config(command=myClick1)
            else:
                ent1.insert(END, "Try again")
        button1=Button(root, text="Check", command=myClick)
        button1.pack()
        def myClick1():
            text=ent1.get().lower()
            if(text=="italy"):
                coord2=110,110,480,480
                arc2=can.create_oval(coord2, fill="#E6F773")
                lab2.config(text="What country was known as Ceylon until 1972?")
                button1.config(command=myClick2)
            else:
                ent1.insert(END, "Try again")
        def myClick2():
            text=ent1.get().lower()
            if(text=="sri lanka"):
                coord3=160,160,430,430
                arc3=can.create_oval(coord3, fill="#73F7B1")
                lab2.config(text="1 Life increased.")
                lab2.place(x=255,y=350)
                global lives; lives+=1
            else:
                ent1.insert(END, "Try again")
        can.pack()
    def SocialMedia():
        label1.pack_forget();but1.pack_forget();but2.pack_forget();but3.pack_forget();but4.pack_forget();but5.pack_forget();but6.pack_forget()
        lab1=Label(root, text="Enter the answer here:")
        lab1.pack()
        ent1= Entry(root, width=25, borderwidth=5)
        ent1.pack()
        can=Canvas(root, height=700, width=600, bg="#E87AA2")
        coord=10,10,580,580
        arc=can.create_oval(coord, fill="red")
        lab2=Label(root, text="What is the most popular social media platform?")
        lab2.place(x=165,y=350)
        def myClick():
            text=ent1.get().lower()
            if(text=="facebook"):
                coord1=60,60,530,530
                arc1=can.create_oval(coord1, fill="#4432B9")
                lab2.config(text="Which social media platform has launched two cyber safety campaigns \n named ‘Safe Stree’ and ‘My Kanoon’?")
                lab2.place(x=105,y=350)
                button1.config(command=myClick1)
            else:
                ent1.insert(END, "Try again")
        button1=Button(root, text="Check", command=myClick)
        button1.pack()
        def myClick1():
            text=ent1.get().lower()
            if(text=="instagram"):
                coord2=110,110,480,480
                arc2=can.create_oval(coord2, fill="#E6F773")
                lab2.config(text="“Super Follows” feature has been introduced by \n which social media giant?")
                lab2.place(x=165,y=350)
                button1.config(command=myClick2)
            else:
                ent1.insert(END, "Try again")
        def myClick2():
            text=ent1.get().lower()
            if(text=="twitter"):
                coord3=160,160,430,430
                arc3=can.create_oval(coord3, fill="#73F7B1")
                lab2.config(text="1 Life increased.")
                lab2.place(x=255,y=350)
                global lives; lives+=1
            else:
                ent1.insert(END, "Try again")
        can.pack()
    def GeneralKnowledge():
        label1.pack_forget();but1.pack_forget();but2.pack_forget();but3.pack_forget();but4.pack_forget();but5.pack_forget();but6.pack_forget()
        lab1=Label(root, text="Enter the answer here:")
        lab1.pack()
        ent1= Entry(root, width=25, borderwidth=5)
        ent1.pack()
        can=Canvas(root, height=700, width=600, bg="#E87AA2")
        coord=10,10,580,580
        arc=can.create_oval(coord, fill="red")
        lab2=Label(root, text="What is the only food that doesn't spoil?")
        lab2.place(x=185,y=350)
        def myClick():
            text=ent1.get().lower()
            if(text=="honey"):
                coord1=60,60,530,530
                arc1=can.create_oval(coord1, fill="#4432B9")
                lab2.config(text="Which is the only mammal on earth that cannot jump?")
                lab2.place(x=155,y=350)
                button1.config(command=myClick1)
            else:
                ent1.insert(END, "Try again")
        button1=Button(root, text="Check", command=myClick)
        button1.pack()
        def myClick1():
            text=ent1.get().lower()
            if(text=="elephant"):
                coord2=110,110,480,480
                arc2=can.create_oval(coord2, fill="#E6F773")
                lab2.config(text="Which is the deepest river in India?")
                lab2.place(x=190,y=350)
                button1.config(command=myClick2)
            else:
                ent1.insert(END, "Try again")
        def myClick2():
            text=ent1.get().lower()
            if(text=="brahmaputra"):
                coord3=160,160,430,430
                arc3=can.create_oval(coord3, fill="#73F7B1")
                lab2.config(text="1 Life increased.")
                lab2.place(x=255,y=350)
                global lives; lives+=1
            else:
                ent1.insert(END, "Try again")
        can.pack()
    but1=Button(root, text="Movies", command=Movies,bg="yellow",activebackground="#112233",fg="red")
    but1.pack()
    but2=Button(root, text="Sports", command=Sports,bg="yellow",activebackground="#112233",fg="red")
    but2.pack()
    but3=Button(root, text="Music", command=Music,bg="yellow",activebackground="#112233",fg="red")
    but3.pack()
    but4=Button(root, text="Countries", command=Countries,bg="yellow",activebackground="#112233",fg="red")
    but4.pack()
    but5=Button(root, text="Social Media", command=SocialMedia,bg="yellow",activebackground="#112233",fg="red")
    but5.pack()
    but6=Button(root, text="General Knowledge", command=GeneralKnowledge,bg="yellow",activebackground="#112233",fg="red")
    but6.pack()
    root.mainloop()
while (lives>0) :
    choice=input("Do you want to play ? (yes OR no) : ").lower()
    if(choice=="no"):
        print("No problem, hope to see you again. :)") 
        exit()     
    elif choice=='yes' :
        print("HELLO !! You are now in the jungle. We hope you can make it home. BEST OF LUCK !! ")
        j1=input("You now see a very fast moving river in front of you. But there is a far off bridge too. Do you wish to wade through the river or take the bridge ? (wade OR bridge): ").lower()
        if j1== 'river':
            print("OOPS, You have been eaten by the crocodiles. :(")
            lives-=1
        elif j1=='bridge':
            print("You have succesfully crossed the bridge !!")
            j2=input("You have two ways to keep going on. One is a firm but rocky path and the other is a slushy and slippery muddy path. Which one do you choose ? (rocky OR muddy)").lower()
            if j2=='muddy':
                print("OOPS, You have slipped down the muddy path. :(")
                lives-=1
            elif j2=='rocky':
                print("You have successfully crossed the rocky path !!")
                j3=input("You seem to be hungry. You see a plant with thorns but bright blue coloured berries. Next to it is a tall and beutiful tree with bright looking red berries. Which one do you pick ? (red OR blue)").lower()
                if j3=='blue':
                    print("OOPS, the blue berries were poisonous. You lose :(")
                    lives-=1
                elif j3=='red':
                    print("You had some tasty red berries. Now let's move on !")
                    j4=input("You seem to be feeling sleepy. There is a tall tree with little shade. You also spot a very dark cave. Where would you shoose to sleep ? (tree OR cave)").lower()
                    if j4=='cave':
                        print("OOPS, The cave was the lion's den and the lion ate you up. :(")
                        lives-=1
                    elif j4=="tree":
                        print("You are lucky the tree didn't fall. \nNow it's time for a fun puzzle.")
                        myChoice()
                        break

while (lives>0) :
    choice=input("Do you want to continue playing? (yes OR no) : ").lower()
    if(choice=="no"):
        print("No problem, hope to see you again. :)") 
        exit()     
    elif choice=='yes' :
        print("WELCOME BACK !!\nYou have now successfully reached a remote village. We hope to see you in the next round too !!")
        v1=input("You now are standing at a crossroad in the middle of the village. The road going to the right seems barren while the one going to the left has a lot of tall grass and bushes. Which way do you choose ? (right or left)").lower()
        if v1=='left' :
            print("OOPS, You are now stranded among the bushes. You lose :(")
            lives-=1
        elif v1=='right' :
            print("You took the right path !! Let's move on now")
            v2=input("You are walking on the barren road in the hot sun. You are feeling very thirsty. You see a small lake with water in it but it looks sort of red in colour. You see a pond on the other side with water in it but the water looks kinda muddy. Which one would you drink from ? (lake or pond)").lower()
            if v2=='lake':
                print("OOPS, the lake was filled with poisonous snakes and the water is now choking you. You lose :(")
                lives-=1
            elif v2=='pond':
                print("The water was a little muddy but was fresh !! We can now move on")
                v3=input("You now a see a group of tribal people singing a folk song and heading towards the hill. They are carrying horns on their heads as part of a ritual. They happily invite you to join them in this interesting ritual. Do you go with them or choose to walk away ? (tribe or walk)").lower()
                if v3=='tribe' :
                    print("OOPS, the tribals took you along to use you as a sacrifice for their lord. You lose :(")
                    lives-=1
                elif v3=='walk':
                    print("It was smart of you to choose to walk away. You are now safe !! Let's go on ..")
                    v4=input("You are now walking down a dark road. But can't seem to find your way out of the village. You see a tall and stalky man walking towards you. You also spot a dingy and dirty road leading somwhere, you can't really see where. Do you choose to ask the man for directions or simply go down the dingy road ? (man or road) ").lower()
                    if v4=='man':
                        print("OOPS, the man pulled out a dagger and he robbed all of your money. You lose :(")
                        lives-=1
                    elif v4=='road':
                        print("It was difficult walking down the road but you have finally made it out of the village !! Wohoo !!\nNow it's time for a fun puzzle.")
                        myChoice()
                        break

while (lives>0) :
    choice=input("Do you want to continue playing? (yes OR no) : ").lower()
    if(choice=="no"):
        print("No problem, hope to see you again. :)") 
        exit()     
    elif choice=='yes' :
        print("You are now moving through a big city. Just hang in there, you are very close to home !!")
        c1=input("It's 2:30 in the night and you are really tired. You have to catch some sleep. You see a dimly lit but very odd looking dusty house on your left and a completely dark park towards your right. Where do you choose to sleep ? (house or park)").lower()
        if c1=='park':
            print("OOPS, this park has been abandoned and haunted from the past 15 years. You're surrounded by tall and scary spirits. You lose :(")
            lives-=1
        elif c1=='house':
            print("Safe choice, an old lady lives in the house and welcomes you in. She offers you the room upstairs and you can finally now catch some sleep, Huff !!")
            c2=input("You wake up fresh and have to reach the train station to catch a train to the suburbs. The old lady offers you her car which is worn, But the train station is 10 km away, quite a distance. Do you choose to take the lady's car or walk to the station ? (car or walk)").lower()
            if c2=='car':
                print("OOPS, you are in for trouble, the breaks of this rusty car have jammed ! It's going out of control. Thudddd, you hit the tree. You lose :(")
                lives-=1
            elif c2=='walk':
                print("That was a tough but safe choice. You can manage walking the distance. Let's keep going")
                c3=input("You are now at the train station and notice something strange. A man in a black coat is constantly staring at you. He moves closer to you. A train arrives, but is going opposite to the direction of your destination. Do you hop on to the train to avoid the scary man or hold your breath and simply wait ? (train or wait)").lower()
                if c3=='train':
                    print("OOPS, the train has gone far far away from where you wanted to go. There's no way back. You lose :(")
                    lives-=1
                elif c3=='wait':
                    print("The man intended no harm, he only was coming to ask you which train to catch to head to Brooklyn. You're safe !")
                    c4=input("You get off the train. You are real close now !! The suburbs are hot as always. Your house is not too far away. But you are really hungry. You see an old and deserted petrol station with a small shop in it. Do you go in for a bag of chips or take the risk of walking the distance home ? (shop or walk)").lower()
                    if c4=='shop':
                        print("OOPS, the shopkeeper somewhat fancies taking the life of weary travellers such as you. He's got you. You lose :(")
                    elif c4=='walk':
                        print("You did the right thing. You are indeed tired and hungry but you have FINALLY REACHED HOME !!!\nCONGRATULATIONS ... YOU WON !!")
                        break
if(lives==0):
    print("You have lost all your lives. Sorry, your journey is over. :(")              
                                           
