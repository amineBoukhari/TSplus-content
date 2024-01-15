from bs4 import BeautifulSoup
import requests
import json
import os

#extract_all_text : extract text of given file 
def extract_all_text(currentFile):
    id_counter = 1  
    with open(currentFile, 'r', encoding='utf-8', errors='ignore') as file , open('extracted_text.json', 'r', encoding='utf-8', errors='ignore') as json_file :
        #html_content : our current page content 
        html_content = file.read()
        #soup : our current page content => array form
        soup = BeautifulSoup(html_content, 'html.parser')

        #json_content : content of the translation JSON filee => JSON FORMAT 
        json_content =json.load(json_file)

        # extracted_data : JSON file of new text (text without data_id)
        extracted_data = {}

        for tag in soup.find_all('p') :
            if not tag.has_attr('data-id') :
                extracted_data["p_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "p_{}".format(id_counter)
                id_counter+= 1 
            elif json_content[tag['data-id']] != tag.get_text().strip() :
                json_content[tag['data-id']] = tag.get_text().strip()
                
                
        
        for tag in soup.find_all('h1') :
            if not tag.has_attr('data-id') :
                extracted_data["h1_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "h1_{}".format(id_counter)
                id_counter+= 1 
            elif json_content[tag['data-id']] != tag.get_text().strip() :
                json_content[tag['data-id']] = tag.get_text().strip()

        for tag in soup.find_all('h2') :
            if not tag.has_attr('data-id') :
                extracted_data["h2_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "h2_{}".format(id_counter)
                id_counter+= 1 
            elif json_content[tag['data-id']] != tag.get_text().strip() :
                json_content[tag['data-id']] = tag.get_text().strip()


        for tag in soup.find_all('h3') :
            if not tag.has_attr('data-id') :
                extracted_data["h3_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "h3_{}".format(id_counter)
                id_counter+= 1 
            elif json_content[tag['data-id']] != tag.get_text().strip() :
                json_content[tag['data-id']] = tag.get_text().strip()


        for tag in soup.find_all('span') :
            if not tag.has_attr('data-id') :
                extracted_data["span_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "span_{}".format(id_counter)
                id_counter+= 1 
            elif json_content[tag['data-id']] != tag.get_text().strip() :
                json_content[tag['data-id']] = tag.get_text().strip()



    # or save to a file
    with open('index.astro', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    mergedJSON = {**extracted_data, **json_content}


    with open("extracted_text.json", "w") as file:
        file.write(json.dumps(mergedJSON,indent=4)) 
        





extract_all_text("./index.astro")




