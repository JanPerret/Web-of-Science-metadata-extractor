# Web-of-Science-metadata-extractor

### General purpose

This suite of programs extracts some metadata from the .txt export files of Web of Science (WOS),
with a final output being a table with one line per WOS reference and the following columns :
WOS accession number, language, document type, publication year, corresponding author(s) nationality(ies) and the country(ies) where the fieldwork was done.

It was made with the export files of the research criteria "mediterran*" in the Topic field of Web of Science, and has not been tested for other resarch criteria. Thus, it may need some modification in order to be used for other files.

The only import needed is the "glob" module that permit to list the files name in a folder. In addition different modules are needed if you choose to use the same way to measure the execution time but it is not necessary.


### Description of each script

1_supp_2_first_lines_all_WOS_txt_files_and_merge_them.py

This program deletes the first 2 lines of every file ending with ".txt" that is located in the folder where the script is, and merge them into a single plain text file.
The first 2 lines correspond to WOS export information and could enter in conflict with the following programs so I chose to get rid of them.

2_WOS_file_parser_v2.py

This program opens the plain text file whose name is given by the user at the beginning of the execution of the program (typically the output file of the precedent program,
or a unique WOS export file in plain text format).
The file is scanned line by line and some information are stored in objects and written into a .txt output file (a comma-separated table).
The information extracted in this version are : document type, language, publisher, publication year, DOI, WOS accession number, research areas, 
author names, title, author keywords, keywords plus, abstract, address of the reprint author.

3_WOS_table_simplifier_v2.py

This program is meant to be used on the output file of the WOS_file_parser_v2.py (it splits every line of the input file by commas, so it has to be a comma-separated table).
For each line of the table in input, it keeps only the following fields : WOS accession number, language, document type, publication year, and the country(ies) where the fieldwork was done.
In addition it performs a country name search in the address of the corresponding author(s) in order to add a column with the "nationality of the author", and a search of the mediterranean countries names
in the following fields to affiliate the reference to different studied countries : title, abstract, author keywords, keywords plus, research areas.
It also performs a research of certain keywords associated with different taxa to affiliate each reference to the studied taxa. For some taxa an external species keywords and name list which can not be communicated was used,
but for other taxa a simple short list of keywords was used. These keywords are present in the script.
The possible country names are taken from the "WOS_mediterranean_country_v4.txt" file.

WOS_country_v3.txt

A list of the possible country names met in the address field of WOS export files. 
I added to the list some of the common typing/filling errors that I found (for example "U.K" instead of "UK", or "Belgique" instead of "Belgium").
Each country name is associated to the "final" chosen country name.

WOS_mediterranean_country_v4.txt

Same list as "WOS_country_v3.txt" but only with the mediterranean countries.


### Program Requirements
- python 3.7
- import glob module


### To download WOS files
Go to the following address : https://apps.webofknowledge.com/

Make a research following your own criteria. Clic on the dropt-down menue located on the top of the results of the research, and choose "Save to Other File Formats".
On the resulting window, choose the number of records you want to save (/!\ Only 500 records at a time can be output /!\), choose "Full Record and Cited References" for the Record Content, and "Plain Text" for the File Format.


### Funding
These programs were written during a work at the Center for Functional and Evolutionary Ecology (or "Centre d'Ecologie Fonctionnelle et Evolutive") in Montpellier, France : https://www.cefe.cnrs.fr/fr/
And funded by the Biodivmex program : http://biodivmex.imbe.fr/


### License
	Web-of-Science-metadata-extractor is a program made to extract 
	some metadata from WOS export files in plain text format.
    Copyright (C) 2019 Jan Perret

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
	along with this program. If not, see <https://www.gnu.org/licenses/>.
