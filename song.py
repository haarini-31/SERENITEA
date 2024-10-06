import pygame
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu
from PIL import Image, ImageTk

# Initialize pygame mixer
pygame.mixer.init()

# Load the MP3 sound files
podcasts = [
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\pod\Jay Shetty - Brian Grazer ON How to Become A Confident Communicator & Connect With Anyone Genuinely.mp3",
   r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\pod\Arnold Schwarzenegger On Life.mp3",
  r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\pod\Denzel Washington Motivational Speech.mp3"
]

nature_sounds = [
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\nature\plasterbrain__loop-by-the-sea(chosic.com).mp3",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\nature\Rain(chosic.com).mp3",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\nature\smand__nightingale-song(chosic.com).mp3",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\nature\the-beat-of-nature-122841.mp3",
]

motivational_songs = [
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\pop\Kelly_Clarkson_-_Stronger_What_Doesnt_Kill_You__CeeNaija.com_.mp3",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\pop\Alessia_Cara_-_Scars_To_Your_Beautiful_CeeNaija.com_.mp3",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\sounds\pop\Pharrell_Williams_-_Happy_CeeNaija.com_.mp3"
]

# Function to play the selected sound
def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)  # Loop indefinitely

# Function to stop the sound
def stop_sound():
    pygame.mixer.music.stop()

# Function to show a message
def show_info():
    messagebox.showinfo("Nature Sound Simulator", "Enjoy the relaxing nature sounds, motivational music, or your favorite podcast!")

# Function to handle dropdown selection
def select_sound(selected_sound):
    if selected_sound:
        play_sound(selected_sound)

# Create the main window
root = tk.Tk()
root.title("Nature Sound Simulator")
root.geometry("600x500")
root.resizable(False, False)

# Load background image
background_image = Image.open(r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\bg3.jpg")
background_image = background_image.resize((600, 500))  # Remove ANTIALIAS
background_photo = ImageTk.PhotoImage(background_image)

# Background Label
bg_label = tk.Label(root, image=background_photo)
bg_label.place(relwidth=1, relheight=1)

# Create a happy vibe label
label = tk.Label(root, text="Welcome to the Nature Sound Simulator!", bg="#87CEEB", fg="#FF6347", font=("Arial", 20, "bold"))
label.pack(pady=20)

# Create a frame for dropdown menus
menu_frame = tk.Frame(root, bg="#87CEEB")
menu_frame.pack(pady=20)

# Dropdown for Podcasts
podcast_var = StringVar(root)
podcast_var.set("Select a Podcast")  # Default value
podcast_menu = OptionMenu(menu_frame, podcast_var, *podcasts, command=select_sound)
podcast_menu.config(bg="#32CD32", fg="white", font=("Arial", 14))
podcast_menu.pack(pady=5)

# Dropdown for Nature Sounds
nature_var = StringVar(root)
nature_var.set("Select a Nature Sound")  # Default value
nature_menu = OptionMenu(menu_frame, nature_var, *nature_sounds, command=select_sound)
nature_menu.config(bg="#32CD32", fg="white", font=("Arial", 14))
nature_menu.pack(pady=5)

# Dropdown for Motivational Songs
motivational_var = StringVar(root)
motivational_var.set("Select a Motivational Song")  # Default value
motivational_menu = OptionMenu(menu_frame, motivational_var, *motivational_songs, command=select_sound)
motivational_menu.config(bg="#32CD32", fg="white", font=("Arial", 14))
motivational_menu.pack(pady=5)

# Control Buttons
control_frame = tk.Frame(root, bg="#87CEEB")
control_frame.pack(pady=20)

play_button = tk.Button(control_frame, text="Play", command=lambda: select_sound(podcast_var.get() if podcast_var.get() != "Select a Podcast" else nature_var.get() if nature_var.get() != "Select a Nature Sound" else motivational_var.get()), bg="#32CD32", fg="white", font=("Arial", 14, "bold"))
play_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(control_frame, text="Stop", command=stop_sound, bg="#FF6347", fg="white", font=("Arial", 14, "bold"))
stop_button.grid(row=0, column=1, padx=10)

info_button = tk.Button(control_frame, text="Info", command=show_info, bg="#FFD700", fg="black", font=("Arial", 14, "bold"))
info_button.grid(row=0, column=2, padx=10)

# Run the GUI main loop
root.mainloop()

# Quit pygame mixer when done
pygame.mixer.quit()
