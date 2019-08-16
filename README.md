# Amazy
Amazy is a maze generator written in Python, which generates maze of different sizes.

<img src="images/5x5.PNG" width="200">  <img src="images/10x10.PNG" width="198">  <img src="images/3x10.PNG" width="200">

# Usage
```
maze = Maze()
print(maze)
```
To create a maze of certain dimensions, pass in the rows and columns:
```
maze = Maze(r=3, c=10)  # This creates a 3x10 maze
```

By default _Start_ is on the upper left corner and _Goal_ is on the lower right corner. Those can be changed by changing the **start** and **goal** variables in the code.
