import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GameOfLife:
    def __init__(self, dimension: int, rate: float):
        self.dimension = dimension
        self.grid = np.random.choice(
            [255, 0], dimension * dimension, p=[rate, 1 - rate]
        ).reshape(dimension, dimension)

    def iterate(self) -> None:
        next_generation = self.grid.copy()
        for i in range(self.dimension):
            for j in range(self.dimension):
                neighbours = int(
                    (
                        self.grid[(i - 1) % self.dimension, (j - 1) % self.dimension]
                        + self.grid[(i - 1) % self.dimension, j]
                        + self.grid[(i - 1) % self.dimension, (j + 1) % self.dimension]
                        + self.grid[i, (j - 1) % self.dimension]
                        + self.grid[i, (j + 1) % self.dimension]
                        + self.grid[(i + 1) % self.dimension, (j - 1) % self.dimension]
                        + self.grid[(i + 1) % self.dimension, j]
                        + self.grid[(i + 1) % self.dimension, (j + 1) % self.dimension]
                    )
                    / 255
                )
                if next_generation[i, j] == 255:
                    if (neighbours < 2) or (neighbours > 3):
                        next_generation[i, j] = 0
                else:
                    if neighbours == 3:
                        next_generation[i, j] = 255
        self.grid[:] = next_generation[:]


def main():
    dimension = 100
    rate = 0.5
    gol = GameOfLife(dimension, rate)

    def tick(_, img, grid, dimension):
        gol.iterate()
        img.set_data(gol.grid)
        return (img,)

    fig, ax = plt.subplots()
    img = ax.imshow(gol.grid, interpolation="nearest")
    ani = animation.FuncAnimation(
        fig,
        tick,
        fargs=(img, gol.grid, dimension),
        frames=10,
        interval=50,
        save_count=50,
    )

    plt.show()


if __name__ == "__main__":
    main()
