from random import shuffle

class Maze:
    def __init__(self, r = 10, c = 10):
        self.cell_sym = 'o'
        self.wall_sym = '*'
        self.start_sym = 'S'
        self.goal_sym = 'G'
        self.R = r
        self.C = c
        self.start = (0, 0)
        self.goal = (self.R-1, self.C-1)

        # each cell has 4 walls: left, right, up, down
        # cell: 1 -> not visited. 0 -> visited
        # wall: 0 -> wall, 1 -> path
        self.cells = [[1 for _ in range(self.C)] for _ in range(self.R)]
        self.walls = [[[0, 0, 0, 0] for _ in range(self.C)] for _ in range(self.R)]

        self.create()

    def create(self):
        def DFS(r, c):
            self.cells[r][c] = 0
            if r == self.goal[0] and c == self.goal[1]:
                return
            dirs, offsets = [0, 1, 2, 3], [(0, -1), (0, 1), (-1, 0), (1, 0)]
            shuffle(dirs)
            for d in dirs:
                new_r, new_c = r + offsets[d][0], c + offsets[d][1]
                if 0 <= new_r < self.R and 0 <= new_c < self.C and self.cells[new_r][new_c] == 1:
                    self.walls[r][c][d] = 1
                    self.walls[new_r][new_c][d+1 if d%2 == 0 else d-1] = 1
                    DFS(new_r, new_c)
        DFS(*self.start)

    def __str__(self):
        # even row of dots are paths between adjacent rows.
        # odd row of dots are paths between adjacent columns.
        # ex: 2 x 2 maze with no path
        #     * * * * *
        #     *   *   *
        #     * * * * *
        #     *   *   *
        #     * * * * *
        mat = [' '.join([self.wall_sym for _ in range(self.C*3-self.C+1)])]
        for r in range(self.R):
            lr_path, ud_path = self.wall_sym, self.wall_sym
            for c in range(self.C):
                # draw cell
                if r == self.start[0] and c == self.start[1]:
                    lr_path += ' ' + self.start_sym + ' '
                elif r == self.goal[0] and c == self.goal[1]:
                    lr_path += ' ' + self.goal_sym + ' '
                else:
                    lr_path += '   '  # space x 3
                
                # draw right path
                if self.walls[r][c][1] == 1: lr_path += ' '
                else:
                    lr_path += self.wall_sym
                
                # draw down path
                if self.walls[r][c][3] == 1:
                    ud_path += '   ' + self.wall_sym
                else:
                    ud_path += ' ' + self.wall_sym + ' ' + self.wall_sym
            mat.append(lr_path)
            mat.append(ud_path)
        return '\n'.join(mat)


if __name__ == '__main__':
    maze = Maze()
    print(maze)


