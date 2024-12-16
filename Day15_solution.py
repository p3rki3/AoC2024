import AoCFramework as AoC

class Warehouse:
    def __init__(self, data, moves, part):
        self.grid = [list(line.rstrip("\n")) for line in data]
        self.moves, self.numrows, self.numcols = moves, len(self.grid), len(self.grid[0])
        self.row_robot, self.col_robot = next((r, c) for r in range(self.numrows) for c in range(self.numcols) if self.grid[r][c] == "@")
        if part == 2:
            ScaleUpTable = {".": "..", "#": "##", "@": "@.", "O": "[]"}
            self.grid = [list("".join(ScaleUpTable[x] for x in row)) for row in self.grid]
            self.numcols, self.col_robot = self.numcols * 2, self.col_robot * 2

    def move(self, move):
        MoveType = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}
        dr, dc = MoveType[move]
        to_move = [(self.row_robot, self.col_robot)]
        for r, c in to_move:
            if (r + dr, c + dc) not in to_move:
                if self.grid[r + dr][c + dc] == "#":
                    return
                elif self.grid[r + dr][c + dc] in "O[]":
                    to_move.append((r + dr, c + dc))
                    if self.grid[r + dr][c + dc] == "[":
                        to_move.append((r + dr, c + dc + 1))
                    elif self.grid[r + dr][c + dc] == "]":
                        to_move.append((r + dr, c + dc - 1))
        for r, c in reversed(to_move):
            self.grid[r + dr][c + dc] = self.grid[r][c]
            self.grid[r][c] = "."
        self.row_robot, self.col_robot = dr + self.row_robot, dc + self.col_robot

    def get_answer(self):
        for move in self.moves:
            self.move(move)
        return sum(100 * r + c for r in range(self.numrows) for c in range(self.numcols) if self.grid[r][c] in "O[")

Blocks = [block.splitlines() for block in AoC.Init("data/day15.txt", nolines=True).split("\n\n")]
Movelist = "".join(Blocks[1])
AoC.verify(1360570, 1381446)
AoC.run(Warehouse(Blocks[0], Movelist, 1).get_answer(), Warehouse(Blocks[0], Movelist, 2).get_answer())
