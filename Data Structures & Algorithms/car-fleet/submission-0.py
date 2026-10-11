class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
     pair=sorted(zip(position,speed),reverse=True)
     fleet=[] 
     for pos,sp in pair:
        time = (target-pos)/sp
        if not fleet or time>fleet[-1]:
             fleet.append(time)
     return len(fleet)