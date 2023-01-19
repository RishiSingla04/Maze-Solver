# Rishi Singla 300293076

from collections import deque

def find (str):
  start = [0,0]
  finish = [0,(len(str[0])-1)]

  for x in range (0, len(str)):
    if (str[x][0]=='p'):
      start[0] = x
  for x in range (0, len(str)):
    if (str[x][len(str[x])-1]=='p'):
      finish[0] = x
  return (start, finish)
  

def solver(str, start, finish):
  solved = False
  step = 1
  solution = deque()
  solution.append([finish[0], finish[1]])
  visited = []
  for x in range(0, len(str)):
    visited.append([0]*len(str[x]))
    
  visited[start[0]][start[1]] = step

  while(visited[finish[0]][finish[1]]==0):
    for x in range(0, len(visited)):
      for y in range(0, len(visited[x])):
        if (visited[x][y]==step):
          step += 1
          if (x<len(visited)-1 and str[x+1][y]=='p' and visited[x+1][y]==0):
            visited[x+1][y] = step

          if (x>0 and str[x-1][y]=='p' and visited[x-1][y]==0):
            visited[x-1][y] = step

          if (y<len(visited[x])-1 and str[x][y+1]=='p' and visited[x][y+1]==0):
            visited[x][y+1] = step

          if (y>0 and str[x][y-1]=='p' and visited[x][y-1]==0):
            visited[x][y-1] = step

  x, y = finish
  while (step!=1):
    step = step-1
    if (x<len(visited)-1 and visited[x+1][y]==step):
      x = x+1
      solution.appendleft((x, y))
    elif (x>0 and visited[x-1][y]==step):
      x = x-1
      solution.appendleft((x, y))        
    elif (y<len(visited[x]) - 1 and visited[x][y+1]==step):
      y = y+1
      solution.appendleft((x, y))        
    elif (y>0 and visited[x][y-1]==step):
      y = y-1
      solution.appendleft((x, y))

  for x in range(0, len(solution)):
    str[solution[x][0]][solution[x][1]] = "*"
  
  for x in range(0, len(str)):
    for y in range(0, len(str[x])):
      print(str[x][y], end='')
    print("")

  print("Solution: ", end='')
  for x in range(0, len(solution)):
    print("(", solution[x][0]+1,",", solution[x][1]+1, ")")

str = []

print("Enter the number of rows: ")
rows = int(input(""))
for x in range(0, rows):
  str.append([])
  print("Enter String", x+1, end=": ")
  str[x] = list(input(""))

start, finish = find(str)
solver(str, start, finish)