# Amazy
Amazy is a Python maze generator. It generates maze of various sizes.

<img src="images/5x5.PNG" width="200">  <img src="images/10x10.PNG" width="198">  <img src="images/3x10.PNG" width="200">

# Usage
```
maze = Maze()
print(maze)
```
To create a maze of different size, pass in the number of rows and columns
```
maze = Maze(r=3, c=10)  # This creates a 3x10 maze
```

By default the "Start" is at the upper left corner and "Goal" is at the lower right corner. To change their locatins, modify the "start" and "goal" variables acoordingly.
