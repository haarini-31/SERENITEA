import pygame
from moviepy.editor import VideoFileClip
import time
import os
import random

# Initialize Pygame
pygame.init()

# Set up the audio
def play_audio(audio_path):
    if os.path.exists(audio_path):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play(-1)  # Loop indefinitely
    else:
        print(f"Error: Audio file not found at {audio_path}")

# Set up the video
def play_video(video_path):
    if os.path.exists(video_path):
        clip = VideoFileClip(video_path)
        clip.preview()  # This will open the video player
    else:
        print(f"Error: Video file not found at {video_path}")

# Main function to run the breathing session
def breathing_session(video_paths, audio_path):
    print("Starting the breathing session...")
    
    # Play audio
    play_audio(audio_path)

    # Randomly select a video to play
    selected_video = random.choice(video_paths)
    play_video(selected_video)

    # Keep the session running for the length of the video
    if os.path.exists(selected_video):
        video_duration = VideoFileClip(selected_video).duration
        time.sleep(video_duration)

    # Stop the audio after the video ends
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    print("Breathing session ended.")

# Paths to your audio and video files
audio_file = r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\breathing\breathing-160445.mp3"  # Your audio file path

# Video file paths
video_files = [
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\breathing\5823116-hd_1920_1080_25fps.mp4",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\breathing\8534909-uhd_3840_2160_25fps.mp4",
    r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\breathing\10551611-hd_3840_2160_25fps.mp4"
]

# Start the breathing session
breathing_session(video_files, audio_file)
