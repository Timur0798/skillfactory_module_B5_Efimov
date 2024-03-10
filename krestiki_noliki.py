def title():
    print("     -----------------------    ")
    print("      Игра КРЕСТИКИ-НОЛИКИ      ")
    print("   Необходимо поочередно вводить")
    print("      2 координаты: x и y       ")
    print("x-номер строки, y-номер столбца ")
    print("     -----------------------    ")
    print()
    
#создание игрового поля
battle_field= [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]
   
#графический вывод игрового поля
def matrix():
    print("  0   1   2")
    print("-------------")
    for i in range(3):
        print(f"{i} {battle_field[i][0]} ! {battle_field[i][1]} ! {battle_field[i][2]} !")
        print("-------------")


#функция для ввода координат с необходимыми проверками
def coordinate():
    while True:
        cords=input("Ваш ход:").split()
        
        #проверка на количество введенных координат
        if len(cords)!=2:
            print("Координат должно быть 2!")
            continue
        
        x,y=cords
        #проверка введенных координат на числовой формат
        if not(x.isdigit()) or not(y.isdigit()):
            print("Вводите только числа!")
            continue
        
        x,y=int(x),int(y)
        #проверка на вхождение координат в область игры   
        if 0 <= x <= 2 and 0 <= y <= 2:
            #проверка на незанятость ячейки
            if battle_field[x][y]==" ":
                return x,y
            else:
                print("Эта ячейка занята")
        else:
            print("Некорректные координаты")


#условия победы
def win():
    lines=[((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(0,1),(0,2)),
    ((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,2),(1,1),(2,0)),((0,0),(1,1),(2,2))]
    for combs in lines:
        win_line=[]
        for a in combs:
            win_line.append(battle_field[a[0]][a[1]])
        if win_line == ["X","X","X"]:
            matrix()
            print("Победил игрок Х")
            return True
        if win_line == ["O","O","O"]:
            matrix()
            print("Победил игрок O")
            return True
    return False

title()
count=0
while True:
    #очередность ходов
    count+=1
    matrix()
    if count%2!=0:
        print("Ходит игрок Х")
    else:
        print("Ходит игрок O")
    x,y=coordinate()
    #внесение данных "Х" и "О" в поле игры
    if count%2!=0:
        battle_field[x][y]="X"
    else:
        battle_field[x][y]="O"
    if win():
        break
    if count==9:
        print("Ничья")
        break