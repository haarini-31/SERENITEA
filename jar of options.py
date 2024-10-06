import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Activities for each jar
activities = {
    "Stress Relief": [
        "Deep breathing exercises",
        "Go for a nature walk",
        "Practice mindfulness meditation",
        "Try yoga or stretching",
        "Listen to calming music"
    ],
    "Combatting Boredom": [
        "Start a new hobby (painting, knitting, etc.)",
        "Try a cooking or baking recipe",
        "Explore a new podcast",
        "Watch a documentary",
        "Organize your space"
    ],
    "Improving Mood": [
        "Go for a run or exercise",
        "Watch a funny movie or show",
        "Talk to a friend or family member",
        "Practice gratitude",
        "Engage in a creative activity"
    ],
    "Fostering Connection": [
        "Reach out to a friend for a chat",
        "Join an online community or forum",
        "Volunteer in your community",
        "Attend local events or meetups",
        "Write letters to friends or family"
    ],
    "Self-Discovery and Growth": [
        "Take an online class",
        "Create a vision board",
        "Experiment with new art techniques",
        "Make a list of goals and dreams",
        "Try a new workout or fitness class"
    ]
}

def show_activity(jar):
    activity = random.choice(activities[jar])  # Select a random activity
    fancy_popup(activity, jar)

def fancy_popup(activity, jar):
    popup = tk.Toplevel(root)
    popup.title(jar)
    popup.geometry("300x150")  # Adjust size as needed
    popup.configure(bg="lightblue")

    title_label = tk.Label(popup, text=jar, font=("Arial", 16, "bold"), bg="lightblue", fg="darkblue")
    title_label.pack(pady=10)

    activity_label = tk.Label(popup, text=activity, font=("Arial", 12), bg="lightblue", fg="black", wraplength=250, justify="center")
    activity_label.pack(pady=10)

    close_button = tk.Button(popup, text="Close", command=popup.destroy, bg="yellow")
    close_button.pack(pady=10)

# Set up the main window
root = tk.Tk()
root.title("Activity Jars")

# Load jar image
jar_image_path = r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\pngtree-simple-cartoon-bottle-jar-clipart-png-image_5851838.jpg"
jar_image = Image.open(jar_image_path)
jar_image = jar_image.resize((100, 150), Image.LANCZOS)  # Resize as needed
jar_photo = ImageTk.PhotoImage(jar_image)

# Create buttons for each jar with the image
for jar in activities.keys():
    button = tk.Button(root, image=jar_photo, text=jar, compound="top", command=lambda j=jar: show_activity(j))
    button.pack(pady=10)

# Run the application
root.mainloop()
