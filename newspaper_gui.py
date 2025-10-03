import tkinter
from PIL import Image, ImageTk
root = tkinter.Tk()
root.geometry("1500x2000")
root.title("Newspaper GUI")

# Title and date
tkinter.Label(text="Times of Pokemon",font="Impact 50 bold").pack(fill=tkinter.X)
tkinter.Canvas(root,width=300,height=1,bg="red").pack()
tkinter.Label(text="March  28  2025",fg="red").pack()

# Top bar
tkinter.Canvas(root,width=2000,height=2,bg="Black").pack()
tkinter.Label(text="                            Jhoto X                 Hoenn X                 Sinnoh X                    Unova X                 Kalos X                 Alola X                 Galar X                 Paldea X",font="arial 15 bold").pack()
tkinter.Label(root,text="Kanto X",font="arial 14 bold",fg="red").place(x=5,y=120)
tkinter.Canvas(root,width=2000,height=2,bg="Black").pack()

# Headline1 (Charmender)
image1 = Image.open("charmender.jpg")
image = image1.resize((300,200))
photo = ImageTk.PhotoImage(image)
tkinter.Label(image=photo).place(x=50,y=170)
tkinter.Label(text="A Trainer Forgets \n His Charmender \n On The Stone",font="Helvetica 25 bold").place(x=60,y=380)
tkinter.Label(text='''Our researchers have found a adandant charmender
                      on the stone clif in forest of verminlion city,
                      some says that thischarmender belong to a trainer 
                     and he left him alone. he said he will came back and 
                    he left him on the stone alone in the forest to suffer 
                    and he was saved by some pokemon trainers ash,brok 
                   and misty while they were moving forward in their jurney.
                    they saved the poor charmender in the heavy rain and he
                   got adoped by one of them the trainer that adandent the 
                  charmender his name is richie.He said the charmender is 
                  too weak to fight in campare to other of other of his pokemons.
                  Very bulshit reason by the way.That trainer is captured the officer 
                  jennie in the vermilion city while he was staying in the pokemon 
                 centere.He cought red handed while unfare trading of pokemon''',font="Georgia 9 ").place(x=-30,y=500)

# Headline2 (Team Rocket)
image2 = Image.open("teamrocket.jpg")
photo2 = ImageTk.PhotoImage(image2.resize((600,400)))
tkinter.Label(image=photo2).pack()
tkinter.Label(text="Team Rocket Has Again Failed \n In One Of Thier Missions In Attempt \n To Stole A Huge Ammount Of Pokemons \n From Pokemon Centre",
              font="Helvetica 25 bold").pack()
tkinter.Label(text='''Our researcher have recently conducted a interview with the head of team rocket (Giogani).In between of the conversation
              he mentions that team rocket in which (Jessie,james and meoth) works have fail a lot of their mission and recently they have
              failed a lot of their mission and recenlty they have failed on more of their mission in which they went in the pokemon centre 
              to rob a huge ammount of pokemon from the pokemon centres.They cutted the light of the pokemon and centre and trying to fill 
              of the injerd pokemon in their bellon but in time three pokemon trainer arrives and stoped they right away.An intence pokemon
              Battle was going on the point but after a while. team rocket losses like always and three of the pokemon trainers sacced in 
              saving a lot of pokemons.There is no imformation about what happen to team rocket after the match as they got blown up high
              in the air and went somewhere so far.But according to leader of team rocket giogani it is their last mission in the team rocker.''' ,font="georgia 9 ").pack()

# Headline 3 (Meowtwo)
image3 = Image.open("mewtow.jpg")
photo3 = ImageTk.PhotoImage(image3.resize((320,500)))
tkinter.Label(image=photo3).place(x=1150,y=160)
tkinter.Label(text="A Mysterious Pokemon's Presence \n Is Said To Be Feeled \nIn Viridion City Cave",font="Helvatica 17 bold").place(x=1100,y=650)
tkinter.Label(text='''Some of the pokemon trainers in viridion 
              city has reported a unknow or we can say unidentfied 
              pokemon in viridion cave.Our research team tried to
              go there but it their equipments stop working at the 
              very first moment they entered in the cave and hance 
              they got afread and leave.The case is handed over to
              officer jennie in the viridion city to investigate.
              even when the police team went in the cave it is so 
              hard for them to find the entity but even when they 
              found it his eyes start glowing and it start attacking
              them.The police team has to evade and seal the area 
              for now.It is said by professos oke that this pokemon 
              is not a natural pokmon it is artificial and created 
              in some sort of lab by some unknown organisation.The 
              unidentified pokemon is said to be a copy or inspiration 
              or a lagendery pokemon"mew" so for now people named it "mewtwo".''').place(x=1080,y=740)

# Photo 4
image4 = Image.open("squartle.jpg")
photo4 = ImageTk.PhotoImage(image4.resize((320,500)))
tkinter.Label(image=photo4).place(x=50,y=730)


root.mainloop()