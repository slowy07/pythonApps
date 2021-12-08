from PIL import Image


def change_contrast(img: Image, level: int) -> Image:
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def contrast(c: int) -> int:
        """
        operation in every bit
        """
        return int(128 + factor * (c - 128))

    return img.point(contrast)


if __name__ == "__main__":
    image_data = Image.open("data_image/somi.jpg")
    contrast_image = change_contrast(image_data, 50)
    contrast_image.save("image_result/somi_changed_contrast.png", format="png")
