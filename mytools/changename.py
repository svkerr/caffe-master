# changes names of files in directory where changename.py is located

import glob

fnames = glob.glob('*.jpg')
fcount = 1

for fname in fnames:
	rename(fname, fname.replace(fname,'truck_pos_'+str(fcount)+'.jpg'))
	fcount += 1

 

