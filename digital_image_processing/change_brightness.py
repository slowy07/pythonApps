from PIL import Image


def change_brightness(img: Image, level: float) -> Image:
    
    def brightness(c : int) -> float:
        return 128 + level + (c - 128)

    if not -255.0 <= level <= 255.0:
        raise ValueError("level value must between -255.0 (black) and 255.0 (white)")
    return img.point(brightness)

if __name__ == "__main__":
    image_data = Image.open("data_image/somi.jpg")
    bright_image = change_brightness(image_data, 100)
    bright_image.save("image_result/somi_changed_brightness.png", format = "png")