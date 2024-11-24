import os
import subprocess

def enhance_image(input_path, output_path):
    model_name = "RealESRGAN_x4plus"
    esrgan_path = os.path.join(os.getcwd(), "ESRGAN-master")

    command = [
        "python", os.path.join(esrgan_path, "inference_realesrgan.py"),
        "-n", model_name,
        "-i", input_path,
        "-o", output_path,
        "--fp32",
        "--denoise_strength", "0",
        "--tile", "1024", # LOWER THIS NUMBER IF YOU LAG (1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1) (do not use 0, this will process everything at once)
        "--pre_pad", "0",
        "--tile_pad", "0",
        "--face_enhance",
    ]
    
    print(f"Running command: {' '.join(command)}")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing: {e}")
        print(f"Command that failed: {' '.join(command)}")
        print(f"Return code: {e.returncode}")
        print(f"Error output: {e.output}")
    except Exception as ex:
        print(f"unexpected error: {ex}")

def main():
    input_dir = "MEDIA"
    output_dir = "OUTPUT"

    os.makedirs(output_dir, exist_ok=True)

    for media_file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, media_file)
        output_path = os.path.join(output_dir, media_file)

        if media_file.endswith(('.jpg', '.jpeg', '.png')):
            print(f"Enhancing quality: {media_file}...")
            enhance_image(input_path, output_path)
            print(f"Enhanced media saved to {output_path}")
        else:
            print(f"Skipping file (not an image): {media_file}")

if __name__ == "__main__":
    main()
