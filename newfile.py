from PIL import Image, ImageDraw, ImageFont

# Create a blank image
width, height = 300, 200
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Draw a circle
draw.ellipse([(50, 50), (250, 150)], fill="blue", outline="black")

# Add text
font = ImageFont.load_default()
draw.text((100, 80), "Logo", font=font, fill="white")

# Save or display the image
image.save("logo.png")
image.show()
