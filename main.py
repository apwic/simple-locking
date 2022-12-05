class Transaction:
  def __init__(self, t):
    # Transaction Type
    # Example : W1X (W: type, 1: num, X: var)
    self.content = t
    # Lock Type
    # Example : XL1X(XL: lock, 1: lock num, X: var)
    self.locks = []

  def setLocks(self):
    # Check if current elmt is commited
    num = self.getNum()
    if (not self.isCommit()):
      # Check if current elmt is locked
      if (self.getType() != 'C'):
        var = self.getVar()
        if (not self.isLocked(num, var)):
          self.locks.append("XL" + num + var)
          temp  = (self.locks[0], self.content[0])
          self.popContent()
          # return the locks and transaction
          return temp
      
      self.postpone()
      return
    else:
      self.unLock()
      temp = (self.content[0], "UL" + num)
      self.popContent()
      return temp

  def popContent(self):
    self.content.pop(0)

  def postpone(self):
    self.content.append(self.content.pop(0))

  def unLock(self):
    return self.locks.pop(0)

  def getType(self):
    return self.content[0][0]

  def getNum(self):
    return self.content[0][1]

  def getVar(self):
    return self.content[0][2]

  def isLocked(self, num, var):
    if (len(self.locks) == 0):
      return False
    else:
      if (num == self.locks[0][2] and var != self.locks[0][3]):
        self.unLock()
        return False
    
      return True

  def isCommit(self):
    if (len(self.locks) != 0):
      if (self.locks[0][2] == self.getNum()):
        return self.getType() == 'C'
    
    return False

  def isEmpty(self):
    return len(self.content) == 0

def printTransaction(t):
  for i in range(len(t)):
    if (i == len(t)-1):
      print(t[i])
    else:
      print(t[i], end="; ")
  print()

if __name__ == '__main__':

  t = []
  filename = input("Input your file: ")

  try:
    with open(filename, "r") as f:
      lines = f.read().split(";")
      for i in lines:
        t.append(i)

  except OSError as e:
    print("File not found!")
    exit()

  transaction = Transaction(t)
  final = []

  print("Input: ")
  printTransaction(transaction.content)

  while (not transaction.isEmpty()):
    current = transaction.setLocks()
    if (not current == None):
      final.append(current[0])
      final.append(current[1])

  print("Output: ")
  printTransaction(final)