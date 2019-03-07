
###############################################################
### To measure the execution time of the program
### Script taken from : https://stackoverflow.com/a/12344609/10890752
import atexit
from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(s, elapsed=None):
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()

def endlog():
    end = time()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

start = time()
atexit.register(endlog)
log("Start Program")
###############################################################


### reading the WOS file
### enter the WOS file name from which you want to extract the data
wos_file_name = ""
wos_file_name = str(input("Enter your Wed of Science file name (converted to ANSI encoding and including the file extension) : "))


def WOS_info_extraction(filename, output_file):
	fin = open(filename, "r")
	num_lines = sum(1 for line in open(filename))
	
	start = ""
	parsing_authors = False
	title = ""
	parsing_title = False
	author_names = ""
	publisher = ""
	language = ""
	doc_type = ""
	parsing_auth_keywords = False
	auth_keywords = ""
	parsing_keywords_plus = False
	keywords_plus = ""
	parsing_abstract = False
	abstract = ""
	reprint_author_address = ""
	publication_year = ""
	DOI = ""
	parsing_research_areas = False
	research_areas = ""
	accession_number = ""
	
	### This loop reads a Web of Science (WOS) .txt export file line by line.
	### Every time a given "keyword" is met in the first 3 characters of a line,
	### the associated information is stored in an object.
	### When the keywords "PT " or "EFP" are met again, the WOS reference is written in the output file.
	### No conditions are tested here, so every reference in the input file will figure in the output table.
	line_count = 0
	for line in fin:
		line_count += 1
		keyword = line[:3]
		if keyword == "PT " or keyword == "EFP":
			if start:
				ref_infos = doc_type+','+language+','+publisher+','+publication_year+','+DOI+','+accession_number+','+research_areas+','+author_names+','+title+','+auth_keywords+','+keywords_plus+','+abstract+','+reprint_author_address
				output_file.write('\n'+ref_infos)
				
				title = ""
				author_names = ""
				publisher = ""
				language = ""
				doc_type = ""
				auth_keywords = ""
				keywords_plus = ""
				abstract = ""
				reprint_author_address = ""
				publication_year = ""
				DOI = ""
				research_areas = ""
				accession_number = ""
				parsing_authors = False
				parsing_title = False
				parsing_auth_keywords = False
				parsing_keywords_plus = False
				parsing_abstract = False
				parsing_research_areas = False
			start = line[3:].strip()
		if keyword == "AF ":
			author_names = line[3:].replace('\n',';').strip() # to keep the separation between the names of the authors
			author_names = author_names.replace(',',' ')
			parsing_authors = True
			continue
		if keyword != "   ":
			parsing_authors = False
		if parsing_authors:
			author_names = author_names + ' ' + line.replace('\n',';').strip()
			author_names = author_names.replace(',',' ')
			continue
		if keyword == "TI ":
			title = line[3:].replace(',',' ').strip()
			parsing_title = True
			continue
		if keyword != "   ":
			parsing_title = False
		if parsing_title:
			title = title + ' ' + line.strip()
			title = title.replace(',',' ')
			continue
		if keyword == "SO ":
			publisher = line[3:].replace(',',' ').strip()
			continue
		if keyword == "LA ":
			language = line[3:].replace(',',' ').strip()
			continue
		if keyword == "DT ":
			doc_type = line[3:].replace(',',' ').strip()
			continue
		if keyword == "DE ":
			parsing_auth_keywords = True
			auth_keywords = line[3:].replace(',',' ').strip()
			continue
		if keyword != "   ":
			parsing_auth_keywords = False
		if parsing_auth_keywords:
			auth_keywords = auth_keywords + ' ' + line.strip()
			auth_keywords = auth_keywords.replace(',',' ')
			continue
		if keyword == "ID ":
			parsing_keywords_plus = True
			keywords_plus = line[3:].replace(',',' ').strip()
			continue
		if keyword != "   ":
			parsing_keywords_plus = False
		if parsing_keywords_plus:
			keywords_plus = keywords_plus + ' ' + line.strip()
			keywords_plus = keywords_plus.replace(',',' ')
			continue
		if keyword == "AB ":
			parsing_abstract = True
			abstract = line[3:].replace(',',' ').strip()
			continue
		if keyword != "   ":
			parsing_abstract = False
		if parsing_abstract:
			abstract = abstract + ' ' + line.strip()
			abstract = abstract.replace(',',' ')
			continue
		if keyword == "RP ":
			reprint_author_address = line[3:].replace(',',' ').strip()
			continue
		if  keyword == "PY ":
			publication_year = line[3:].replace(',',' ').strip()
			continue
		if keyword == "DI ":
			DOI = line[3:].replace(',',' ').strip()
			continue
		if keyword == "D2 ":
			DOI = line[3:].replace(',',' ').strip()
			continue
		if keyword == "SC ":
			parsing_research_areas = True
			research_areas = line[3:].replace(',',' ').strip()
			continue
		if keyword != "   ":
			parsing_research_areas = False
		if parsing_research_areas:
			research_areas = research_areas + ' ' + line.strip()
			research_areas = research_areas.replace(',',' ')
			continue
		if keyword == "UT ":
			accession_number = line[3:].replace(',',' ').strip()
			continue
		if line_count == num_lines: # to write the infos from the last reference when the end of the file is reached
			ref_infos = doc_type+','+language+','+publisher+','+publication_year+','+DOI+','+accession_number+','+research_areas+','+author_names+','+title+','+auth_keywords+','+keywords_plus+','+abstract+','+reprint_author_address
			output_file.write('\n'+ref_infos)

	fin.close()


output_file = open('RESULT_'+wos_file_name,'w') # opening a file to write the output
# to write the output headers
output_file.write("doc_type"+','+"language"+','+"publisher"+','+"publication_year"+','+"DOI"+','+"accession_number"+','+"research_areas"+','+"author_names"+','+"title"+','+"auth_keywords"+','+"keywords_plus"+','+"abstract"+','+"reprint_author_address")
WOS_info_extraction(wos_file_name, output_file)
output_file.close()
print("Done !")


### to print the execution time of the program
def endlog():
    end = time()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))
endlog()
