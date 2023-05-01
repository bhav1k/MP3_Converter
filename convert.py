import os
import sys
import subprocess

if len(sys.argv) != 3:
    print("Usage: python convert.py input_folder output_folder")
    sys.exit(1)

input_folder = sys.argv[1]
output_folder = sys.argv[2]

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through each file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".mp3"):
        # Create the output file name by replacing the extension with .wav
        wav_file = os.path.join(output_folder, os.path.splitext(file_name)[0] + ".wav")

        # Run ffmpeg to convert the file to WAV format
        subprocess.call(["ffmpeg", "-i", os.path.join(input_folder, file_name), wav_file])

        print(f"{file_name} converted to {wav_file}")
