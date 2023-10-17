import os
from pygame import mixer

# Set up the mixer
mixer.init()

# Set the path to your music directory

music_directory = "#"    #link your  music_directory

# Get a list of all music files in the directory
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

# Display the list of available songs
print("Available songs:")
for index, song in enumerate(music_files):
    print(f"{index + 1}. {song}")

# Choose a song to play
try:
    choice = int(input("Enter the song number to play: "))
    if choice < 1 or choice > len(music_files):
        raise ValueError("Invalid choice")
except ValueError:
    print("Invalid input. Exiting.")
    mixer.quit()
    exit()

# Load and play the selected song
selected_song = os.path.join(music_directory, music_files[choice - 1])
print(f"Now playing: {selected_song}")
mixer.music.load(selected_song)
mixer.music.play()

# Keep the program running while the music is playing
while mixer.music.get_busy():
    pass

# Clean up after playback
mixer.quit()
print("Playback finished.")
