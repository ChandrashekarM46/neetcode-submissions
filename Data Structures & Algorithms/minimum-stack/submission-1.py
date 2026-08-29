class MinStack:
    # st=[]
    # minst=[]

    def __init__(self):
     self.st=[]
     self.minst=[]

    def push(self, val: int) -> None:
      self.st.append(val)
      if self.minst:
        if val<=self.minst[-1]:
            self.minst.append(val)
      else:
        self.minst.append(val)

    def pop(self) -> None:
        if self.st[-1]==self.minst[-1]:
            self.minst.pop() 
        if self.st:
            self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
        
