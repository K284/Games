l = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
for row in l:
        print(row[0],"\t",row[1],"\t",row[2])
count = 0
while True:
    print("\nX's turn")    
    r = int(input("Enter the row: "))
    c = int(input("Enter the column: ")) 
    l[r-1][c-1] = "X"
    for row in l:
        print(row[0],"\t",row[1],"\t",row[2])
    count+=1
    if l[0][0] == "X" and l[1][1] == "X" and l[2][2] == "X":
        print("X won")
        break
    elif l[0][2] == "X" and l[1][1] == "X" and l[2][0] == "X":
        print("X won")
        break        
    elif l[0][0]  == "X" and l[1][0] == "X" and l[2][0] == "X":
        print("X won")
        break
    elif l[0][1]  == "X" and l[1][1] == "X" and l[2][1] == "X":
        print("X won")
        break
    elif l[0][2]  == "X" and l[1][2] == "X" and l[2][2] == "X":
        print("X won")
        break  
    elif count == 9:
        print("Tie")
        break
    
    print("\nO's turn")
    r = int(input("Enter the row: "))
    c = int(input("Enter the column: "))
    l[r-1][c-1] = "O"
    for row in l:
        print(row[0],"\t",row[1],"\t",row[2])
    count+=1
    if l[0][0] == "O" and l[1][1] == "O" and l[2][2] == "O":
        print("O won")
        break
    elif l[0][2] == "O" and l[1][1] == "O" and l[2][0] == "O":
        print("O won")
        break        
    elif l[0][0]  == "O" and l[1][0] == "O" and l[2][0] == "O":
        print("O won")
        break
    elif l[0][1]  == "O" and l[1][1] == "O" and l[2][1] == "O":
        print("O won")
        break
    elif l[0][2]  == "O" and l[1][2] == "O" and l[2][2] == "O":
        print("O won")
        break  
    


