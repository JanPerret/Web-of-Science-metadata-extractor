
### /!\ All the files downloaded from WOS are in UTF-8 encoding. They need to be converted to ANSI encoding first.
### for example use CpConverter : https://github.com/mrexodia/CpConverter

### creating a list of every file finishing with ".txt" in the folder where the script is located
import glob
file_list=glob.glob('*.txt')

# loop to supress the first 2 lines of every listed file
for i in range(len(file_list)) :
	file=file_list[i]
	with open(file, 'r') as myfile:
		data = myfile.read()
	if data[0:3] != "PT " : # condition : if the first 3 characters of the file are "PT ", the file is not shortened
		print(file)
		with open(file, 'r') as fin:
			data = fin.read().splitlines(True)
		with open('WOS_files_merged.txt', 'a') as output_file: # creating output file and adding the file without the 2 first lines at the end of the file at each iteration of the loop
			output_file.writelines(data[2:])
	else :
		print(file, 'has already been shortened')

print("Done !")