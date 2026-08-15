class Game2048:
  def __init__(self):
    self.broad=self.begin()
#-----------------------------------------------
  def begin(self):#4*4的空格
    self.tf=False#讓遊戲持續執行
    a=[]
    b=[]
    for i in range(0,4):
      b=[]

      for j in range(0,4):
        b.append(0)
      a.append(b)
    return a
#----------------------------------------------
  def ran(self):#加隨機數
  #自動讀入self.broad
    import random
    zero=[]
    for i in range(4):
      for j in range(4):
        if self.broad[i][j]==0:
          zero.append((i,j))

    if len(zero)>=1:
      ch=random.choice(zero)#ch是為零的隨機座標
      chx=ch[0]
      chy=ch[1]
      prob=random.random()

      if prob <0.8:
        self.broad[chx][chy]=2
      else:
        self.broad[chx][chy]=4
#--------------------------------------------------
  def print_broad(self):#格式化輸出
    for i in range(0,4):

      rowstr= ""
      for j in range(0,4):
        rowstr += f"{str(self.broad[i][j]):3}"+ " "
      print(rowstr)
#--------------------------------------------------------------
  def left(self,line):
#a[i]為單位，把數字抓出來

    new_line=[]
    for i in range(0,4):
      if line[i] != 0:
        new_line.append(line[i])
      else:
        continue

    while len(new_line)< 4:
      new_line.append(0)#把0放回去
    for j in range(0,3):
      if new_line[j]==new_line[j+1]:
        new_line[j]=new_line[j]*2
        new_line[j+1]=0
      else:
        continue

    new_line_2=[]
    for i in range(0,4):
      if new_line[i] != 0:
        new_line_2.append(new_line[i])
    while len(new_line_2)< 4:
      new_line_2.append(0)#把0放回去

    return new_line_2
  def move_left(self):
    for i in range(0,4):

      self.broad[i]=self.left(self.broad[i])#向左合併
  def move_right(self):
    for i in range(0,4):
      self.broad[i].reverse()#把list反轉

      self.broad[i]=self.left(self.broad[i])#向右合併
      self.broad[i].reverse()#反轉回來
#-------------------------------------------------------------
  def change_line(self,a):#行列互換
    rotated_case = []
    for i in range(0, 4):
      line = []
      for j in range(0, 4):
          line.append(a[j][i])
      rotated_case.append(line)
    return rotated_case
#---------------------------------------------------------------
  def move_up (self):

  #複製矩陣
    rotated_case = []
    for i in range(0, 4):
        line = []
        for j in range(0, 4):
            line.append(self.broad[j][i])
        rotated_case.append(line)


    for i in range(4):
      rotated_case[i]=self.left(rotated_case[i])
    self.broad=self.change_line(rotated_case)

#-------------------------------------------------------------
  def move_down (self):
  # 輸入4*4 棋盤a

  #複製矩陣
    rotated_case = self.change_line(self.broad)

    for i in range(4):
      rotated_case[i].reverse()
      rotated_case[i]=self.left(rotated_case[i])
      rotated_case[i].reverse()
    self.broad=self.change_line(rotated_case)

#------------------------------------------------------------
  def is_game_over(self):
     for i in range(4):#是否有0的存在
      for j in range(4):
        if self.broad[i][j]==0:
          return False
     for i in range(0,4):#檢查橫列是否還能合併
      for j in range(0,3):
        if self.broad[i][j]==self.broad[i][j+1]:d
          return False
     for i in range(0,3):#檢查橫列是否還能合併
      for j in range(0,4):
        if self.broad[i][j]==self.broad[i+1][j]:
          return False
 
     return True 
#---------------------------------------------------------------
  def play(self):
    self.broad=self.begin()
    self.ran()
    self.ran()
    self.print_broad()
    while self.tf==False:
      b=input()
      if b=="a":

        self.move_left()

      elif b=="d":
        self.move_right()
      elif b=="w":
        self.move_up()


      elif b=="s":
        self.move_down()


        #print(a)

      self.ran()
      self.tf=self.is_game_over()

      self.print_broad()
    print("Game over")
game=Game2048()
game.play()