#!/usr/bin/python

from __future__ import division
from __future__ import print_function

# Tyler McCraney

# 2. Write a Python script that parses those HTML files for names and dates. EcoEvoPub speakers only!
#   -Download the HTML files to your Vagrant instance like so:
#    curl -L https://www.dropbox.com/s/u70dtrdr35p5tgk/seminars.tar.gz | tar zxv

import glob
import re

from bs4 import BeautifulSoup

# See my unsuccesful attempt to use regular expressions on the html text.  It didn't work because there is different formatting for some of the html files 
#html_files = glob.glob("/home/vagrant/Homework-assignment-7/seminars/*.html")
#print("There are " + str((len(html_files))) + " pages on the EEB seminar website.")

#output = open("EEPspeakers.txt", "a")

# Parsing the HTML files
#for html_file in html_files:
#    with open(html_file, "r") as open_file:
#        soup = BeautifulSoup(open_file)
#        section_div = soup.find("div", class_="section")
#        output.write(str(section_div))
#output.close()

# Use grep in TextWrangler
#<h3>Seminars</h3>\r<h4>(.+)</h4>\r.+\r<p><strong>EcoEvoPub Series</strong> <br/>\r.+\r.+\r.+\r<p>([A-z]+ [A-z]+ [A-z]*) ... argh!

## I'm just going to run your code.
all_html = glob.glob("seminars/*.html")
print(len(all_html))

def is_ecoevopub(element):
    strongs = element.find_all("strong")
    for strong in strongs:
        if re.search("EcoEvoPub", str(strong)):
            return strong
            
def extract_date(element):
    date = element.find("h4")
    if (date):
        return date.string
        
def get_summary_text(element):
    header = element.find("h4", text="Summary")
    if header and header.string == "Summary":
            return header.find_next("p")
            
for html_file in all_html:
    with open(html_file, "r") as rfile:
        soup = BeautifulSoup(rfile)
        section_div = soup.find("div", class_="section")
        if is_ecoevopub(section_div):
            eep_date = extract_date(section_div)
            print("Found an EcoEvoPub on", eep_date)
            summary_text = get_summary_text(section_div)
            for line in summary_text.strings:
                search_name = re.search(r"([A-Z-]{3,}) ([A-Z-]{3,})", line)
                if search_name and search_name.group(0) != "BIOMEDICAL SCIENCES":
                    print(search_name.group(0))
                
