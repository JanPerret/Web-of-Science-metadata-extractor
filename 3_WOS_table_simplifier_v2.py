
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


### reading the table resulting from the WOS_file_parser_v2
table_file_name = ""
table_file_name = str(input("Enter your comma-separated table file name (including the file extension) : "))


def Simple_WOS_table_maker(table_file_name, output_table):
	fin = open(table_file_name, "r")
	
	# loading the country name list
	country_index = open("WOS_country_v3.txt", "r")
	country_names = []
	country_finals = []
	country_line_list = []
	for line in country_index:
		country_line_list = line.split(",",1)
		country_names.append(" " + country_line_list[0].lower().replace('\n','') + " ") # makes a list of the possible country names with a space before and after each name
		country_finals.append(country_line_list[1].replace('\n','')) # makes a list of the 'final' country names I choose associated with the country names of the precedent list
	length = len(country_names)
	address_search = ""
	name_final = ""

	# loading the mediterranean country name list
	fw_country_index = open("WOS_mediterranean_country_v4.txt", "r")
	fw_country_names = []
	fw_country_finals = []
	fw_country_line_list = []
	for line in fw_country_index:
		fw_country_line_list = line.split(",",1)
		fw_country_names.append(" " + fw_country_line_list[0].lower().replace('\n','') + " ")
		fw_country_finals.append(fw_country_line_list[1].replace('\n',''))
	fw_length = len(fw_country_names)
	fw_country_search = ""
	fw_country_final = ""
	
	# loading the amphibian species name list
	amphibian_index = open("ref_taxo_amphibian_med_Geniez.txt", "r")
	amphibian_names = []
	amphibian_finals = []
	amphibian_line_list = []
	for line in amphibian_index:
		amphibian_line_list = line.split(",",1)
		amphibian_names.append(" " + amphibian_line_list[0].lower().replace('\n','') + " ") # list of the possible amphibian species names with a space before and after each name
		amphibian_finals.append(amphibian_line_list[1].replace('\n',''))
	amphibian_length = len(amphibian_names)
	amphibian_search = ""
	amphibian_final = ""
	
	# loading the reptile species name list
	reptile_index = open("ref_taxo_reptiles_med_Geniez.txt", "r")
	reptile_names = []
	reptile_finals = []
	reptile_line_list = []
	for line in reptile_index:
		reptile_line_list = line.split(",",1)
		reptile_names.append(" " + reptile_line_list[0].lower().replace('\n','') + " ") # list of the possible reptile species names with a space before and after each name
		reptile_finals.append(reptile_line_list[1].replace('\n',''))
	reptile_length = len(reptile_names)
	reptile_search = ""
	reptile_final = ""
	
	# loading the bird species name list
	bird_index = open("ref_taxo_bird_world_IOC_names.txt", "r")
	bird_names = []
	bird_finals = []
	bird_line_list = []
	for line in bird_index:
		bird_line_list = line.split(",",1)
		bird_names.append(" " + bird_line_list[0].lower().replace('\n','') + " ") # list of the possible bird species names with a space before and after each name
		bird_finals.append(bird_line_list[1].replace('\n',''))
	bird_length = len(bird_names)
	bird_search = ""
	bird_final = ""
	
	# initialising the objects used in the loop
	doc_type = ""
	language = ""
	publisher = ""
	year = ""
	DOI = ""
	access_num = ""
	research_areas = ""
	author_names = ""
	title = ""
	auth_keywords = ""
	keywords_plus = ""
	abstract = ""
	address = ""
	name = ""
	author_nationality = ""
	author_nationality_tot = ""
	line_list = []
	search_mix = ""
	fw_country = ""
	fw_country_tot = ""
	amphibian = ""
	reptile = ""
	bird = ""
	mammal = ""
	insect = ""
	fish = ""
	plant = ""
	fungi = ""
	coleoptera = ""
	papilionoidea = ""
	lumbricina = ""
	ref_infos = ""
	line_cnt = 1;

	### This loop reads a comma-separated table file line by line.
	### For each line, only a certain amount of data is transcribed in the output file :
	### the document type, the language, the publisher, the year of publication, the DOI,
	### the WOS accession number, the research areas, the author names, the title of the publication,
	### the author keywords, the keywords plus (defined by WOS), the abstract
	### and the address of the corresponding author(s).
	### To extract the nationality of the corresponding author(s) from their address,
	### a research of the country names contained in the "WOS_country_v3.txt" is made.
	### In addition it performs for each line a research of some keywords associated with
	### specific taxa to affiliate the publications to the taxa their talking about.
	### For amphibians, reptiles and birds, a species name list (which could not be communicated)
	### is loaded, and for the other taxa the used keywords are shown in the script below.
	first_line = fin.readline() # to not take into account the first line with the columns headers
	for line in fin:
		line_cnt += 1
		line_list = line.split(",")
		if len(line_list) != 13:
			print("Error in line " + str(line_cnt) + ": " + str(line_list))
			continue
		doc_type = str(line_list[0])
		language = str(line_list[1])
		publisher = str(line_list[2])
		year = str(line_list[3])
		DOI = str(line_list[4])
		access_num = str(line_list[5])
		research_areas = str(line_list[6])
		author_names = str(line_list[7])
		title = str(line_list[8])
		auth_keywords = str(line_list[9])
		keywords_plus = str(line_list[10])
		abstract = str(line_list[11])
		address = str(line_list[12])

		if address:
			address_list = address.split("(reprint author)")
			nlist = len(address_list)
										# species = species.split(".",1)[0]
			for i in range(0,nlist):
				address_search = address_list[i].lower()
				address_search = address_search.replace("."," ").replace(","," ").replace(";"," ").replace(":"," ").replace("'"," ").replace("("," ").replace(")"," ").replace("-"," ").replace("	"," ")
				address_search = " " + address_search + " "
				for n in range(0,length):
					name = country_names[n]
					name_final = country_finals[n]
					if name in address_search: # assignation of each country name found in the address to the "author_nationality" object
						author_nationality += ' ' + name_final
						author_nationality = author_nationality.strip()
					if author_nationality:
						if not author_nationality in author_nationality_tot: # so we don't get multiple assignations in case the multiple reprint authors are from the same country
							author_nationality_tot += author_nationality + " // " 
					author_nationality = ""
			author_nationality_tot = author_nationality_tot.strip()
			author_nationality_tot = author_nationality_tot[:-3]
			# if author_nationality_tot == "" and len(address_list[i]) > 2:
				# print("Assignation error in line "+str(line_cnt)+" : an address is present but no country was found. Address : "+address)
		
		if language == "English":
			search_mix = research_areas+" "+title+" "+auth_keywords+" "+keywords_plus+" "+abstract
			search_mix = search_mix.replace("."," ").replace(","," ").replace(";"," ").replace(":"," ").replace("'"," ").replace("("," ").replace(")"," ").replace("-"," ").replace("_"," ")
			search_mix = search_mix.replace("	"," ")
			search_mix = " "+search_mix.lower()+" "
			for n in range(0,fw_length):
				name = fw_country_names[n]
				name_final = fw_country_finals[n]
				if name in search_mix: # assignation of each country name found in the search_mix object to the "fieldwork_country" object
					fw_country += ' ' + name_final
					fw_country = fw_country.strip()
				if fw_country:
					if not fw_country in fw_country_tot: # so we don't get multiple assignations in case the same country is found multiple times
						fw_country_tot += fw_country + " // "
				fw_country = ""
			fw_country_tot = fw_country_tot.strip()
			fw_country_tot = fw_country_tot[:-3]
			
			for n in range(0,amphibian_length):
				name = amphibian_names[n]
				name_final = "Amphibian"
				if name in search_mix:
					if not name_final in amphibian:
						amphibian += ' ' + name_final
						amphibian = amphibian.strip()
						
			for n in range(0,reptile_length):
				name = reptile_names[n]
				name_final = "Reptile"
				if name in search_mix:
					if not name_final in reptile:
						reptile += ' ' + name_final
						reptile = reptile.strip()

			for n in range(0,bird_length):
				name = bird_names[n]
				name_final = "Bird"
				if name in search_mix:
					if not name_final in bird:
						bird += ' ' + name_final
						bird = bird.strip()

			insect_names = [" insect "," insects "," entomology "," entomological "]
			insect_length = len(insect_names)
			for n in range(0,insect_length):
				name = insect_names[n]
				name_final = "Insect"
				if name in search_mix:
					if not name_final in insect:
						insect += ' ' + name_final
						insect = insect.strip()
			
			mammal_names = [" mammal "," mammals "," mammalian "," mammalia "," rodent "," rodents "," rodentia "," chiroptera "]
			mammal_length = len(mammal_names)
			for n in range(0,mammal_length):
				name = mammal_names[n]
				name_final = "Mammal"
				if name in search_mix:
					if not name_final in mammal:
						mammal += ' ' + name_final
						mammal = mammal.strip()
			
			fish_names = [" fish "," fishes "," ichthyology "]
			fish_length = len(fish_names)
			for n in range(0,fish_length):
				name = fish_names[n]
				name_final = "Fish"
				if name in search_mix:
					if not name_final in fish:
						fish += ' ' + name_final
						fish = fish.strip()

			plant_names = [" plant "," plants "," botany "," botanical "," tracheophytes "," angiosperm "," angiosperms "," angiospermae "," gymnosperm "," gymnosperms "," gymnospermae "," pteridophyte "," pteridophytes "," spermatophytes "]
			plant_length = len(plant_names)
			for n in range(0,plant_length):
				name = plant_names[n]
				name_final = "Vascular plant"
				if name in search_mix:
					if not name_final in plant:
						plant += ' ' + name_final
						plant = plant.strip()
			
			fungi_names = [" fungi "," fungis "," fungal "," fungus "," funguses "," mushroom "," mushroom "," mycology "," mycological "," eumycetes "," mycelium "]
			fungi_length = len(fungi_names)
			for n in range(0,fungi_length):
				name = fungi_names[n]
				name_final = "Fungi"
				if name in search_mix:
					if not name_final in fungi:
						fungi += ' ' + name_final
						fungi = fungi.strip()
						
			coleoptera_names = [" coleoptera "," beetle "," beetles "," carabidae "]
			coleoptera_length = len(coleoptera_names)
			for n in range(0,coleoptera_length):
				name = coleoptera_names[n]
				name_final = "Coleoptera"
				if name in search_mix:
					if not name_final in coleoptera:
						coleoptera += ' ' + name_final
						coleoptera = coleoptera.strip()

			papilionoidea_names = [" papilionoidea "," rhopalocera "," butterfly "," butterflies "]
			papilionoidea_length = len(papilionoidea_names)
			for n in range(0,papilionoidea_length):
				name = papilionoidea_names[n]
				name_final = "Papilionoidea"
				if name in search_mix:
					if not name_final in papilionoidea:
						papilionoidea += ' ' + name_final
						papilionoidea = papilionoidea.strip()
			
			lumbricina_names = [" lumbricina "," earthworm "," earthworms "]
			lumbricina_length = len(lumbricina_names)
			for n in range(0,lumbricina_length):
				name = lumbricina_names[n]
				name_final = "Lumbricina"
				if name in search_mix:
					if not name_final in lumbricina:
						lumbricina += ' ' + name_final
						lumbricina = lumbricina.strip()

		ref_infos = access_num+','+language+','+doc_type+','+year+','+author_nationality_tot+','+fw_country_tot+','+plant+','+fungi+','+amphibian+','+reptile+','+bird+','+mammal+','+insect+','+fish+','+coleoptera+','+papilionoidea+','+lumbricina

		doc_type = ""
		language = ""
		publisher = ""
		year = ""
		DOI = ""
		access_num = ""
		research_areas = ""
		author_names = ""
		title = ""
		auth_keywords = ""
		keywords_plus = ""
		abstract = ""
		address = ""
		name = ""
		name_final = ""
		author_nationality = ""
		author_nationality_tot = ""
		search_mix = ""
		fw_country = ""
		fw_country_tot = ""
		amphibian = ""
		reptile = ""
		bird = ""
		mammal = ""
		insect = ""
		fish = ""
		plant = ""
		fungi = ""
		coleoptera = ""
		papilionoidea = ""
		lumbricina = ""
		
		output_table.write('\n'+ref_infos)


output_table = open('SIMPLE_v2_'+table_file_name,'w') # opening a file to write the output
# write the column headers
output_table.write('access_num'+','+'language'+','+'doc_type'+','+'year'+','+'author_nationality'+','+'fieldwork_country'+','+'plant'+','+'fungi'+','+'amphibian'+','+'reptile'+','+'bird'+','+'mammal'+','+'insect'+','+'fish'+','+'coleoptera'+','+'papilionoidea'+','+'lumbricina')
Simple_WOS_table_maker(table_file_name, output_table)
output_table.close()


### to print the execution time of the program
def endlog():
	end = time()
	elapsed = end-start
	log("End Program", secondsToStr(elapsed))
endlog()
