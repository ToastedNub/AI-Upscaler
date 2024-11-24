import os
import subprocess
import shutil


def enhance_video_quality(input_path, output_path):
    """
    Enhance video quality using Real-ESRGAN, interpolating frames to 60 FPS if needed.
    """
    model_name = "RealESRGAN_x4plus"
    esrgan_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ESRGAN-master")

    command_fps = [
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=r_frame_rate", "-of", "default=noprint_wrappers=1:nokey=1", input_path
    ]

    try:
        result = subprocess.run(command_fps, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        fps_values = result.stdout.strip().split('/')
        fps = 60
        if len(fps_values) == 2:
            fps = int(fps_values[0]) / int(fps_values[1])
    except Exception as e:
        print(f"Error determining FPS: {e}")
        fps = 60

    temp_interpolated_video = None

    if fps != 60:
        print(f"Original FPS: {fps}. Interpolating frames to 60 FPS.")
        temp_interpolated_video = "temp_interpolated_video.mp4"
        interpolation_command = [
            "ffmpeg", "-i", input_path, "-filter:v", 
            "minterpolate='fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1'", "-y", temp_interpolated_video
        ]
        try:
            subprocess.run(interpolation_command, check=True)
            input_path = temp_interpolated_video
        except subprocess.CalledProcessError as e:
            print(f"Interpolation error: {e}")
            return

    command = [
        "python", os.path.join(esrgan_path, "inference_realesrgan_video.py"),
        "-n", model_name,
        "-i", input_path,
        "-o", output_path,
        "--fps", "60",
        "--face_enhance",
        "--tile", "1024", # LOWER THIS NUMBER IF YOU LAG (1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1) (do not use 0, this will process everything at once)
        "--denoise_strength", "0.3",
        "--outscale", "4",
        "--pre_pad", "20",
        "--tile_pad", "5",
    ]

    print(f"Running command: {' '.join(command)}")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing video: {e}")
    finally:
        if temp_interpolated_video and os.path.exists(temp_interpolated_video):
            os.remove(temp_interpolated_video)


def main():
    """
    Main function to enhance all video files in the input directory.
    """
    input_dir = "MEDIA"
    output_dir = "OUTPUT"

    os.makedirs(output_dir, exist_ok=True)

    for media_file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, media_file)
        output_path = os.path.join(output_dir, media_file)

        if media_file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
            print(f"Enhancing video quality: {media_file}...")
            enhance_video_quality(input_path, output_path)

        print(f"Enhanced video saved to {output_path}")


if __name__ == "__main__":
    main()
