from PIL import Image, ImageDraw, ImageFont
import os 

ASCII_CHARS = "@#S%?*+;:,. "

def image_to_ascii_color(input_path, output_path="ascii_colored.png", width=120, font_path=None, font_size=12):
    # Load image
    img = Image.open(input_path).convert("RGB")
    W, H = img.size
    aspect_ratio = H / W
    new_height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, new_height))

    # Choose font
    if font_path is None:
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, font_size)

    # Get character dimensions (cross-compatible)
    try:
        bbox = font.getbbox("A")
        char_width, char_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    except AttributeError:
        # fallback for older versions
        temp_img = Image.new("RGB", (10, 10))
        draw = ImageDraw.Draw(temp_img)
        char_width, char_height = draw.textsize("A", font=font)

    # Create output canvas
    out_img = Image.new("RGB", (width * char_width, new_height * char_height))
    draw = ImageDraw.Draw(out_img)

    # Draw each pixel as ASCII char
    pixels = img.load()
    for y in range(new_height):
        for x in range(width):
            r, g, b = pixels[x, y]
            brightness = int((r + g + b) / 3)
            char = ASCII_CHARS[brightness * (len(ASCII_CHARS) - 1) // 255]
            draw.text((x * char_width, y * char_height), char, fill=(r, g, b), font=font)

    out_img.save(output_path)
    print(f"Saved colored ASCII art as {output_path}")

# Example usage:


input_dir = 'images/'
output_dir = 'ascii/'
input_files = os.listdir(input_dir)

for file in input_files:
    file_name = file 
    img_path = os.path.join(input_dir, file)
    out_path = os.path.join(output_dir, file)
    image_to_ascii_color(img_path, out_path, width=250, font_path="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", font_size=6)
print('DONE!!!!!!!!!1')

# image_to_ascii_color( "images/347.jpg", "ascii_colored.png", width=250, font_path="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", font_size=6)
