READ ALL OF THIS, IT IS IMPORTANT FOR YOUR SYSTEMS HEALTH WHILE RUNNING THIS SCRIPT

BEFORE YOU DO ANYTHING, RUN THE "Build" FILE, THIS SETS UP ESRGAN FOR UPSCALING

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

IN LINE 45, THE NUMBER IN BRACKETS "512", LOWER THIS NUMBER IF THE COMMAND PROMPT STARTS TO LAG, OR IF YOU HAVE LESS THAN 0.5GB GPU MEMORY AVALABLE WHILE RUNNING THE SCRIPT

RECOMMENDED TILE SIZES: 1024, 512, 256, 128, 64 (THE LOWER THE NUMBER IS, THE LONGER IT WILL TAKE TO COMPLETE THE UPSCALE PROCESS)

HOW TO CHECK IF IT IS USING TOO MUCH MEMORY

1) Put a 1080p 60fps video into the MEDIA folder, the more complicated the visuals in the video, the better for this test

2) Open Task Manager, go to the Performance tab, then click on your GPU

3) Run the script

4) Once the script starts processing the media, make sure you have more than 1GB of "Dedicated GPU memory" available while the script runs

5) If you have less than 0.5GB not being used, or the command prompt console lags when you try to move the window, then you need to close the command prompt window, and lower the number in line 45 in the script | Line 45 looks like this ("--tile", "512",)

ADITIONAL) Lowering the number for the tiles does not change how good the quality is in the output, it only makes the script run slower for weaker systems

RECOMENDED TILE VALUES: 1024, 512, 256, 128, 64, (32, 16, 8, 4, 2, 1 only if you really have to)

WARNING) if you set the tile value to 0 ("--tile", "0",), then this will make the script use as much memory as it wants, and can potentially damage your system!

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

PYTHON DOWNLOAD: Brings you to the Official Python Download Page (YOU NEED PYTHON FOR THIS TO WORK)
FFMPEG DOWNLOAD: Brings you to the Official FFMPEG Download Page (YOU NEED FFMPEG FOR THIS TO WORK)

YOU CAN USE THE DOWNSCALER TO DOWNSCALE THE FILE BACK TO ITS ORIGINAL SIZE< WHILE KEEPING ALL THE ENHANCEMENTS

Put your files in the "MEDIA" folder

Run the "Start" file, and wait until it finishes downloading all dependencies and loading the frames

When the command prompt console closes, your enhanced file will be in the "OUTPUT" folder

The other folders are just there because the script needs those to work properly