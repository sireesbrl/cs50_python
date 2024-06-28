import sys
import os
from PIL import Image, ImageOps

def check_command_line():
    #valid extensions
    extensions = (".jpg", ".jpeg", ".png")

    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    #split argument to get image extensions
    image1 = os.path.splitext(sys.argv[1])
    image2 = os.path.splitext(sys.argv[2])

    if not image1[1] in extensions or not image2[1] in extensions:
        print("Invalid input")
        sys.exit(1)

    elif image1[1] in extensions and image2[1] in extensions:
        if image1[1] != image2[1]:
            print("Input and output have different extensions")
            sys.exit(1)
        else:
            return True


def generate_image():
    try:
        with Image.open("shirt.png") as shirt:
            shirt_size = shirt.size
            try:
                with Image.open(sys.argv[1]) as photo:
                    muppet = ImageOps.fit(photo, shirt_size)
                    muppet.paste(shirt, shirt)
                    muppet.save(sys.argv[2])
            except FileNotFoundError:
                print(f"{sys.argv[1]} not found")
    except FileNotFoundError:
        print("shirt.png not found")



def main():
    if check_command_line():
        generate_image()


if __name__ == "__main__":
    main()
