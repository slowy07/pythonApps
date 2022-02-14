from __future__ import annotations

from typing import List

from PIL import Image

GLIDER = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

BLINKER = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


def new_generation(cells: List[List[int]]) -> List[List[int]]:
    next_generation = []
    for i in range(len(cells)):
        next_generation_row = []
        for j in range(len(cells[i])):
            neighbour_count = 0
            if i > 0 and j > 0:
                neighbour_count += cells[i - 1][j - 1]
            if i > 0:
                neighbour_count += cells[i - 1][j]
            if i > 0 and j < len(cells[i]) - 1:
                neighbour_count += cells[i - 1][j + 1]
            if j > 0:
                neighbour_count += cells[i][j - 1]
            if j < len(cells[i]) - 1:
                neighbour_count += cells[i][j + 1]
            if i < len(cells) - 1 and j > 0:
                neighbour_count += cells[i + 1][j - 1]
            if i < len(cells) - 1:
                neighbour_count += cells[i + 1][j]
            if i < len(cells) - 1 and j < len(cells[i]) - 1:
                neighbour_count += cells[i + 1][j + 1]

            alive = cells[i][j] == 1
            if (
                (alive and 2 <= neighbour_count <= 3)
                or not alive
                and neighbour_count == 3
            ):
                next_generation_row.append(1)
            else:
                next_generation_row.append(0)

        next_generation.append(next_generation_row)

    return next_generation


def generate_image(cells: list[list[int]], frames) -> list[Image.Image]:
    images = []
    for _ in range(frames):
        img = Image.new("RGB", (len(cells[0]), len(cells)))
        pixels = img.load()

        for x in range(len(cells)):
            for y in range(len(cells[0])):
                colour = 255 - cells[x][y] * 255
                pixels[x, y] = (colour, colour, colour)

        images.append(img)
        cells = new_generation(cells)

    return images


if __name__ == "__main__":
    images = generate_image(GLIDER, 16)
    images[0].save("out.gif", save_all=True, append_images=images[1:])
