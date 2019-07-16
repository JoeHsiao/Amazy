from random import shuffle


class Maze:
    def __init__(self, r=10, c=10):
        if r <= 0 or c <= 0:
            raise AssertionError("Row and column must be greater than zero.")

        self.wall_sym = '*'
        self.start_sym = 'S'
        self.goal_sym = 'G'
        self.R = r
        self.C = c
        self.start = (0, 0)
        self.goal = (r - 1, c - 1)

        # each cell has 4 walls: left, right, up, down
        # cell: 1 -> not visited. 0 -> visited
        # wall: 0 -> wall, 1 -> path
        self.cells = [[1 for _ in range(self.C)] for _ in range(self.R)]
        self.walls = [[[0, 0, 0, 0] for _ in range(self.C)] for _ in range(self.R)]

        self.create()

    # Searching from "goal" to "start" would make the maze more difficult.
    # This creates multiple reasonable looking routes near "start" because of backtracking.
    # If searching from "start" to "goal", there would be very few branches near "start",
    # thus making the maze very straightforward.
    def create(self):
        def dfs(r, c):
            self.cells[r][c] = 0
            if r == self.start[0] and c == self.start[1]:
                return
            dirs, offsets = [0, 1, 2, 3], [(0, -1), (0, 1), (-1, 0), (1, 0)]
            shuffle(dirs)
            for d in dirs:
                new_r, new_c = r + offsets[d][0], c + offsets[d][1]
                if 0 <= new_r < self.R and 0 <= new_c < self.C and self.cells[new_r][new_c] == 1:
                    self.walls[r][c][d] = 1
                    self.walls[new_r][new_c][d + 1 if d % 2 == 0 else d - 1] = 1
                    dfs(new_r, new_c)

        dfs(*self.goal)

    def __str__(self):
        # even row of dots are paths between adjacent rows.
        # odd row of dots are paths between adjacent columns.
        # ex: 2 x 2 maze with no available path
        #     * * * * *
        #     *   *   *
        #     * * * * *
        #     *   *   *
        #     * * * * *
        def get_cell(r, c):
            ret = [' ', ' ', ' ']  # space x 3
            if r == self.start[0] and c == self.start[1]:
                ret[1] = self.start_sym
            elif r == self.goal[0] and c == self.goal[1]:
                ret[1] = self.goal_sym
            return ''.join(ret)

        def get_right_wall(r, c):
            return ' ' if self.walls[r][c][1] == 1 else self.wall_sym

        def get_down_wall(r, c):
            empty = '   ' + self.wall_sym
            block = self.wall_sym * 4
            return empty if self.walls[r][c][3] == 1 else block

        mat = [' '.join([self.wall_sym for _ in range(self.C * 3 - self.C + 1)])]
        for r in range(self.R):
            lr_path, ud_path = self.wall_sym, self.wall_sym
            for c in range(self.C):
                lr_path += get_cell(r, c)
                lr_path += get_right_wall(r, c)
                ud_path += get_down_wall(r, c)
            mat.append(lr_path)
            mat.append(ud_path)
        return '\n'.join(mat)


if __name__ == "__main__":
    m = Maze()
    print(m)
