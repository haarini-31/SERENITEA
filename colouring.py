import tkinter as tk
from tkinter.colorchooser import askcolor
import random
from PIL import Image, ImageTk
import pygame
import os

# Initialize pygame for Zen Mode (music feature)
pygame.mixer.init()

root = tk.Tk()
root.title("Relaxing Painting Game")
root.attributes('-fullscreen', True)  # Set to full screen

# Global variables for drawing
current_color = "#000000"
brush_size = 5
drawing_active = False
current_shape = "oval"
mood_palettes = {
    "Calm": ["#A7BED3", "#C6E2E9", "#F1FFC4", "#FFCCAC", "#FFE4C4"],
    "Happy": ["#FFD700", "#FF69B4", "#87CEEB", "#FF8C00", "#32CD32"],
    "Energy Boost": ["#FF4500", "#FF6347", "#FFD700", "#ADFF2F", "#00FF7F"]
}
emotion_brushes = {
    "Calm": {"size": 5, "color": "#A7BED3"},
    "Happy": {"size": 8, "color": "#FFD700"},
    "Sad": {"size": 3, "color": "#708090"}
}
flow_mode = False
random_brush_timer = None

quotes = [
    "You are enough just as you are.",
    "Breathe in, breathe out, and relax.",
    "Let go of what you can't control.",
    "Your mind is a peaceful place."
]

# Paths to images
image_paths = [
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\alliswell.png",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\bike.png",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\butterfly.jpg",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\chosehappy.webp",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\flower.png",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\flower2.png",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\just breath.jpeg",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\keepcalm.jpg",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\keepgoing.jpg",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\makegreatoday.webp",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\colouring book\sun.jpg"
]

current_image = None

# Display canvas for drawing
canvas = tk.Canvas(root, bg="white", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

def choose_color():
    global current_color
    color = askcolor()[1]
    current_color = color

def change_brush_size(size):
    global brush_size
    brush_size = size

def set_shape(shape):
    global current_shape
    current_shape = shape

def paint(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    
    if current_shape == "oval":
        canvas.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)
    elif current_shape == "rectangle":
        canvas.create_rectangle(x1, y1, x2, y2, fill=current_color, outline=current_color)
    elif current_shape == "line":
        canvas.create_line(event.x, event.y, event.x + brush_size * 2, event.y + brush_size * 2, fill=current_color, width=brush_size)

canvas.bind("<B1-Motion>", paint)

def apply_mood_palette(mood):
    global current_color
    current_palette = mood_palettes[mood]
    current_color = random.choice(current_palette)

def apply_emotion_brush(emotion):
    global brush_size, current_color
    brush = emotion_brushes[emotion]
    brush_size = brush["size"]
    current_color = brush["color"]

def zen_mode(duration):
    music_file = r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\nature\plasterbrain__loop-by-the-sea(chosic.com).mp3"
    if os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)
    else:
        print("Music file not found!")
    root.after(duration * 60000, end_zen_mode)

def end_zen_mode():
    pygame.mixer.music.stop()

def show_quote():
    quote = random.choice(quotes)
    quote_label.config(text=quote)
    root.after(5000, show_quote)  # Change quote every 5 seconds

# Display images on the canvas
def display_image(image_path):
    global current_image
    img = Image.open(image_path)
    img = img.resize((1200, 800))  # Resize the image to fit the canvas
    current_image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=current_image, anchor=tk.NW)

# Create UI elements for selecting features
color_button = tk.Button(root, text="Choose Color", command=choose_color, bg="lightblue")
color_button.pack(side=tk.LEFT)

brush_size_slider = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, command=lambda size: change_brush_size(int(size)), bg="lightyellow")
brush_size_slider.pack(side=tk.LEFT)

mood_var = tk.StringVar()
mood_dropdown = tk.OptionMenu(root, mood_var, *mood_palettes.keys(), command=apply_mood_palette)
mood_dropdown.pack(side=tk.LEFT)

emotion_var = tk.StringVar()
emotion_dropdown = tk.OptionMenu(root, emotion_var, *emotion_brushes.keys(), command=apply_emotion_brush)
emotion_dropdown.pack(side=tk.LEFT)

zen_time_entry = tk.Entry(root, width=5)
zen_time_entry.insert(0, "5")  # Default time in minutes
zen_time_entry.pack(side=tk.LEFT)

zen_button = tk.Button(root, text="Start Zen Mode", command=lambda: zen_mode(int(zen_time_entry.get())), bg="lightgreen")
zen_button.pack(side=tk.LEFT)

quote_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#FFFDD0")
quote_label.pack(pady=10)
show_quote()  # Start showing mindfulness quotes periodically

# Dropdown for selecting and displaying images
image_var = tk.StringVar()
image_dropdown = tk.OptionMenu(root, image_var, *image_paths, command=display_image)
image_dropdown.pack(side=tk.LEFT)

# Shape selection dropdown
shape_var = tk.StringVar()
shape_var.set("oval")  # Default shape
shape_dropdown = tk.OptionMenu(root, shape_var, ["oval", "rectangle", "line"], set_shape)
shape_dropdown.pack(side=tk.LEFT)

root.mainloop()
