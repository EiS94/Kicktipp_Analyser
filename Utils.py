def create_image_from_text(text, filename="summary.png"):
    from PIL import Image, ImageDraw, ImageFont

    image_width = 1500
    image_height = 500
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("cour.ttf", 12)

    x, y = 10, 10
    line_height = 15

    for line in text.split('\n'):
        draw.text((x, y), line, font=font, fill=text_color)
        y += line_height

    image.save(filename)