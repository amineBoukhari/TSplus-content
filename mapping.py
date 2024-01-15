from bs4 import BeautifulSoup
import requests
import json
import os


# Example usage:
source_file = 'index.astro'  # Replace with the path to your source file
destination_file = 'index2.astro'  # Replace with the desired destination path





#extract_all_text : extract text of given file 
def extract_all_text(currentFile):
    with open(currentFile, 'r', encoding='utf-8', errors='ignore') as file , open('extracted_text.json', 'r', encoding='utf-8', errors='ignore') as json_file :
        #html_content : our current page content 
        html_content = file.read()
        #soup : our current page content => array form
        soup = BeautifulSoup(html_content, 'html.parser')
        #json_content : content of the translation JSON filee => JSON FORMAT 
        json_content =json.load(json_file)

    for key in json_content : 
        element =  soup.find( attrs={'data-id': key})
        if(element is not None) :
          element.string = f"{{t('{key}')}}"

    des = "./duplicate/{}".format(currentFile)

    with open(des, 'w', encoding='utf-8') as file:
      file.write(soup.prettify())

        





extract_all_text("index.astro")




