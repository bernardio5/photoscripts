# photoscripts
Python scripts that automate image processing for online/PDF photo albums

Often, there's an "inputs" directory: the scripts load each image in that, 
fiddle with the image (usually reducing the resolution and insetting 
the image onto a 1080p background), save it, and, usually, generate
a line of HTML that refers to it. Usually, also, make a thumbnail image. 
Sometimes, bump contrast, convert to grayscale, and paste into a PDF.

Given a directory of 100s of photos, makes a tidy web page of the images
in a few seconds/minutes. 

Yeah, there are alll sorts of JS libraries to do this, but vanilla HTML will Just Work 9 months from now, and in 2070, too. If we're still allowed to use HTML. 

Uses the Python OpenCV for a lot of it. 
