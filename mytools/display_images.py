# display_images.py
# used to display .jpg files in a directory to see if they were captured correctly or are not corrupted 

import Image 
import os

get_file_list = os.walk('.')
f=[files for files in get_file_list] 
curr_dir,_,files = f[0]

for f in files:
	if 'jpg' in f: 
		image = Image.open(f)
		f.show()

