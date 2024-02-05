print("Calculate The Bricks In A Wall  : ".title().center(60))
print( )
print("Developed By Muhammad Hamza Javed : ".title().center(60))
print()

#First Calculate The Volume Of The Wall

Lenght_of_wall=float(input("Enter Lenght Of The Wall in ft : "))
Hight_of_wall=float(input("Enter Hight Of The Wall in ft : "))
Thickness_of_wall=float(input("Enter Thickness Of The Wall in Ft : "))
Total_Volume_of_wall = Lenght_of_wall * Hight_of_wall * Thickness_of_wall
print("Total Volume_of_wall".title().center(60),Total_Volume_of_wall.__round__(3))
print()

#Calculate The Volume Of Brick

L=float(input("Enter Lenght Of The Brick in ft : "))
B=float(input("Enter Breadth Of The Brick in ft : "))
H=float(input("Enter Hight Of The Brick in ft : "))
V= L * B * H 
print()
print("Total Volume Of Bricks : ",V.__round__(4))
No_of_Bricks=(Total_Volume_of_wall/V)                         #No Of Blocks #Developed By M.Hamza Javed
print()
print("Number Of Bricks : ".title().center(60),No_of_Bricks.__round__(2))
