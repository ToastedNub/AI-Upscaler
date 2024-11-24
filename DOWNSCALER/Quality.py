import os
from moviepy.editor import VideoFileClip, ImageClip
from PIL import Image

script_dir = os.path.dirname(os.path.realpath(__file__))
media_folder = os.path.join(script_dir, 'MEDIA')  # Folder for videos, gifs, and images
output_folder = os.path.join(script_dir, 'OUTPUT')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

media_files = [f for f in os.listdir(media_folder) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.gif', '.jpg', '.jpeg', '.png'))]

for media_file in media_files:
    media_path = os.path.join(media_folder, media_file)
    output_path = os.path.join(output_folder, f"lowered_{media_file}")
    
    if media_file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        with VideoFileClip(media_path) as video:
            width, height = video.size
            new_width = width // 4
            new_height = height // 4
            
            resized_video = video.resize(newsize=(new_width, new_height))
            resized_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

        print(f"Video saved to {output_path}")
    
    elif media_file.lower().endswith('.gif'):
        with VideoFileClip(media_path) as gif:
            width, height = gif.size
            new_width = width // 4
            new_height = height // 4
            
            resized_gif = gif.resize(newsize=(new_width, new_height))
            resized_gif.write_gif(output_path)

        print(f"GIF saved to {output_path}")
    
    elif media_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        with Image.open(media_path) as img:
            new_width = img.width // 4
            new_height = img.height // 4
            
            resized_img = img.resize((new_width, new_height))
            resized_img.save(output_path)

        print(f"Image saved to {output_path}")
