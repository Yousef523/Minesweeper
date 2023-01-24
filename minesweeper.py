import random

class Input:
    def __init__(self,g=8,b=10):
        self.g = g #initialize grid size
        self.b = b #Number of bombs
        self.minesweeper_map = self.GenerateMap()#Creates Mine map
        self.map = self.Grid_Output() #Creates player map
        self.GameStatus = True
        self.flags_left = 10  #Variable to track flags left

    
    def GenerateMap(self): # Randomly places bombs and increments bomb count 
        arr = [[0 for row in range(self.g)] for column in range(self.g)]
        for num in range(self.b):
            x = random.randint(0, self.g - 1) #random x coordinate
            y = random.randint(0, self.g - 1) # random y coordinate
            arr[y][x] = 'B' 
            
            if (x >= 0 and x <= self.g - 2) and (y >= 0 and y <= self.g - 1):
              
                if arr[y][x + 1] != 'B':
                    arr[y][x + 1] += 1  
                  
            if (x >= 1 and x <= self.g - 1) and (y >= 0 and y <= self.g - 1):
                
              if arr[y][x - 1] != 'B':
                  arr[y][x - 1] += 1  
            
            if (x >= 1 and x <= self.g - 1) and (y >= 1 and y <= self.g - 1):
                
              if arr[y - 1][x - 1] != 'B':
                    arr[y - 1][x - 1] += 1  

            if (x >= 0 and x <= self.g - 2) and (y >= 1 and y <= self.g - 1):
                
                if arr[y - 1][x + 1] != 'B':
                    arr[y - 1][x + 1] += 1  
            
            if (x >= 0 and x <= self.g - 1) and (y >= 1 and y <= self.g - 1):
                
                if arr[y - 1][x] != 'B':
                    arr[y - 1][x] += 1  

            if (x >= 0 and x <= self.g - 2) and (y >= 0 and y <= self.g - 2):
                
                if arr[y + 1][x + 1] != 'B':
                    arr[y + 1][x + 1] += 1  
            if (x >= 1 and x <= self.g - 1) and (y >= 0 and y <= self.g - 2):
                
                if arr[y + 1][x - 1] != 'B':
                    arr[y + 1][x - 1] += 1  
            
            if (x >= 0 and x <= self.g - 1) and (y >= 0 and y <= self.g - 2):
                
                if arr[y + 1][x] != 'B':
                    arr[y + 1][x] += 1  
        return arr

    def Grid_Output(self): #Creates grid out of "~" characters
        arr = [['~' for row in range(self.g)] for column in range(self.g)]
        return arr

    def OutputMap(self,map): #Outputs map passed as a parameter
        for row in map:
            print(" ".join(str(cell) for cell in row))

                           
#;)

    def Won_Check(self,map): # checks if player has won the game
      for i in range(self.g):
        for j in range(self.g):
            if self.minesweeper_map[i][j] == 'B' and map[i][j] != 'F':
                return False
            elif self.minesweeper_map[i][j] != 'B' and map[i][j] not in ['F',self.minesweeper_map[i][j]]:
                return False
      return True

      
      
    def PutFlag(self, x, y): #allows user to flag a tile
        if x>=0 and x<=self.g-1 and y>=0 and y<=self.g-1:
            if self.flags_left > 0:
                if self.map[y][x] == '~':
                    self.map[y][x] = 'F'
                    self.flags_left -= 1
                elif self.map[y][x] == 'F':
                    self.map[y][x] = '~'
                    self.flags_left += 1
            else:
                print("You cant use any more flags")
        else:
            print("Invalid Coordinates")

        

    def Reveal(self, x, y): #Checks if tile is bomb or not, if it is a bomb a loser message is output if not it will reveal number of bombs around it
      if self.minesweeper_map[y][x] == 'B':
        self.map[y][x] = 'B'
        print("Game Over, Try again later :l")
        self.GameStatus = not self.Won_Check(self.map)
      else:
        self.map[y][x] = self.minesweeper_map[y][x]




    def Game(self): # main loop and takes input from user
      self.GameStatus = True
      while self.GameStatus:
          Start = input("Enter S to start: ")
          if Start.lower() == 's':
              self.minesweeper_map = self.GenerateMap()
              self.map = self.Grid_Output()
              self.OutputMap(self.map)
              while self.GameStatus:
                  x = int(input("Enter x coordinate (0-7) : "))
                  y = int(input("Enter y coordinate(0-7) : "))
                  action = input("Enter F to place a flag, O to reveal a cell: ")
                  if action.upper() == 'F':
                      self.PutFlag(x, y)
                  elif action.upper() == 'O':
                      self.Reveal(x, y)
                      if self.minesweeper_map[y][x] == 'B':
                          self.GameStatus = not self.Won_Check(self.map)
                          break 
                  else:
                      print("Invalid input, please enter F or O")
                  self.OutputMap(self.map)
                  if self.Won_Check(self.map):
                      print("Congrats You Won!")
                      self.GameStatus = False
                  self.flags_left = 10





    def main(): 
      game = Input() 
      game.Game() #starts game by calling Game function which starts the game

if __name__ == '__main__':
    Input.main() #main program that calls main function inside class 
                  




#Refrences:
#https://www.w3schools.com/python/python_classes.asp
