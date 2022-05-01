import math
class Queen:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def coincide(self,xx,yy):
    xd=math.fabs(xx-self.x)
    yd=math.fabs(yy-self.y)
    if xd==yd: return True
    if self.x==xx or self.y==yy: return True
    return False
class Board:
  def __init__(self) -> None:
    self.queens=[]
    pass
  def addQueen(self,x,y):
    newQ=Queen(x,y)
    for olderQ in self.queens:
      if newQ.coincide(olderQ.x,olderQ.y):
        return False
    self.queens.append(newQ)
    return True
  def pickItUp(self):
    self.queens.pop(len(self.queens)-1)
    pass
  def toString(self):
    for i in range(len(self.queens)):
      print("["+str(self.queens[i].x)+","+str(self.queens[i].y)+"] ",end=" ")
    pass
myBoard = Board()
def putQueenOnBoard(col):
  put = False
  for i in range(1,9):
    if myBoard.addQueen(col,i):
      put=True
      if col==8:
        myBoard.toString()
        print("")
        print("******************************************************")
      else:
        putQueenOnBoard(col+1)
    if put:
      myBoard.pickItUp()
      put=False
pass
putQueenOnBoard(1)