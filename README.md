# photoscripts
Python scripts that automate image processing for online photo albums

Often, there's an "inputs" directory: load each image in that, 
fiddle with the image (usually reducing the resolution and insetting 
the image into a 1080p background), save it, and, usually, generate
a line of HTML that refers to it. Usually, also, make a thumbnail image.

Given a directory of 100s of photos, makes a tidy web page of the images
in a few seconds/minutes. 

Yeah, there are alll sorts of JS libraries to do this: this will work in 2050.
Well, the page will, anyway. 

Uses the Python OpenCV for a lot of it. 
