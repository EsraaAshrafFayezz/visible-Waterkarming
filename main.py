from PIL import Image

def add_watermark(input_image_path, watermark_image_path, output_image_path, position=(0, 0)):
    base = Image.open('C:\watermarking\origin.png').convert('RGBA')
    watermark = Image.open('C:\watermarking\watermark.jpg').convert('RGBA')

    width, height = base.size
    w_width, w_height = watermark.size

    # Resize watermark if it's larger than the base image
    if w_width > width or w_height > height:
        watermark = watermark.resize((width // 3, height // 3), Image.ANTIALIAS)

    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(base, (0, 0))
    transparent.paste(watermark, position, mask=watermark)

    transparent.save(output_image_path, format='PNG')

if __name__ == '__main__':
    input_image_path = "input_image.jpg"
    watermark_image_path = "watermark_image.png"
    output_image_path = "output_image.png"

    add_watermark(input_image_path, watermark_image_path, output_image_path, position=(0, 0))
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
