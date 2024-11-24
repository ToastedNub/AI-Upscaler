# AI-Upscaler

Its easy to read and edit the code in [VS CODE](https://code.visualstudio.com)

You need [Python](https://www.python.org/downloads/) installed to PATH for this

You need [FFMPEG](https://ffmpeg.org/download.html) installed to PATH for this | [Installation Guide](https://youtu.be/JR36oH35Fgg)

Doanload these
 - [ESRGAN](https://github.com/xinntao/ESRGAN)
 - [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

Extract both

Drag the "Real-ESRGAN-master" folder into the "ESRGAN-master" folder

Then drag the "ESRGAN-master folder" into the folder into the same folder where you extracted "Quality Enhancer"

Go into the "Real-ESRGAN-master" folder, click the address bar (top bar that shows where you are in the file explorer), type "cmd" to get to the console for that folder

 - DOWNLOAD THE DEPENDENCIES & SETUP ESRGAN
 - Normal Method

Type "pip install -r requirements.txt"

Then type "python setup.py"

Close the console window when that is finished

 - Noob Method

Go to [this repository](https://github.com/ToastedNub/Upscaler-Noob-Thing), download it as a zip

Extract the zip

Put the "Build" file into the "Real-ESRGAN-master" folder, which you should have dragged into the "ESRGAN-master" folder

Run the "Build" file once you place it in there

 - HOW IT WORKS

Place an Image or Video into the "MEDIA" folder

FOR A GIF: (If you want to use a Gif, you need to turn it into a video, use the script on it, then turn it back into a Gif)

Run the "Image" file for Images

Run the "Video" file for Videos

Run the "AcidVideo" file on a low fps video, to give it a trippy effect

When the console closes, your new files will be in the "OUTPUT" folder

 - DOWNSCALER

There is a Downscaler included in the "DOWNSCALER" folder


This should work for Images, Videos, and Gifs

Your files go in the "MEDIA" folder

run the "Start" file

When the console closes, your Downscaled files will be in the "OUTPUT" folder

 - IF YOU LAG RUNNING THE SCRIPT

You need to edit a line in the script you are using

They are in the "SCRIPTS" folder

Line in ImageQuality script: 15

Line in AcidVideo script: 51

Line in VideoQuality script: 51

Lower this number if you lag while running the script, it can be one of the values below for best processing

"1024" "512" "256" "128" "64" "32" "16" "8" "4" "2" "1"

DO NOT USE "0" THIS WILL PROCESS EVERYTHING AT ONCE
