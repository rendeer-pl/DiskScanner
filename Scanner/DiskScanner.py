import os.path
import shutil
from datetime import datetime

def folder_size(path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
                print('Folders so far: ', total_folders, ' Size so far: ', human_readable_size(total_size, 3))
    return total_size

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0 or unit == 'PB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f},{unit}"

name = input('What is the drive name?\n')
letter = input ('What is the drive letter?\n')

#open text file
now = datetime.now()
datetime_string = now.strftime("_%y%m%d_%H%M%S")
output_file_name = letter + ":/"+ name + datetime_string + ".csv";
text_file = open(output_file_name, "w", encoding='utf-8')

total, used, free = shutil.disk_usage(letter + ":\\")
output = name + "," + human_readable_size(free, 3) + "\n"

# path to check
file_path = letter + ":\\"
total_folders = 0

for dirpath, dirnames, filenames in os.walk(file_path):
	for d in dirnames:
		dpath = os.path.join (dirpath, d)
		output += dpath[2:] + "," + human_readable_size(folder_size(dpath), 3)
		output += "\n"
		total_folders = total_folders + 1
 
#write string to file
text_file.write(output)

print ("Scan complete! Results saved to " + output_file_name)

#close file
text_file.close()
