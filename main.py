class Node:
    def __init__(self,position,g,h,parent):
        self.position=position
        self.g=g
        self.h=h
        self.f=g+h
        self.parent=parent
def heuristic(a:tuple,b:tuple):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
def Astar(start:tuple,goal:tuple,grid:list[list]):
    start_node = Node(start,0,heuristic(start,goal),None)
    open_list=[]
    closed_list=[]
    open_list.append(start_node)
    while len(open_list)>0:
        current=open_list[0]
        for n in open_list:
            if current.f>n.f:
                current=n
        if current.position == goal:
            path=[]
            while current:
                path.append(current.position)
                current=current.parent
            return path[::-1]
        open_list.remove(current)
        closed_list.append(current)
        x=current.position[0]
        y=current.position[1]
        neighbours=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
    
        for pos in neighbours:
            if pos[0]<0 or pos[1]<0 or pos[0]>=len(grid) or pos[1]>=len(grid[0]):
                continue
            if grid[pos[0]][pos[1]]==1:
                continue
            skip=False
            for c in closed_list:
                if c.position == pos:
                    skip=True
            if skip:
                continue
            new_node = Node(pos,current.g+1,heuristic(start,pos),current)
            open_list.append(new_node)
    return None
grid=[
    [0,1,0],
    [0,1,0],
    [0,0,0],
    [1,1,0]
]
print(Astar((0,0),(3,2),grid))
            
