# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:26:43 2021

@author: jomen
"""

import json
from json.decoder import JSONDecodeError

def combine_json(json_src, json_out, files):
    new_json = []
    for i in range(len(files)):
        try:
                
            print("Progress: {}".format("" + str(i) + "/" + str(len(files))))
    
            data = json.load(open(files[i], encoding="utf-8"))
    
            fields = ['original_title', 'budget', 'genres', 'popularity', 'release_date', 'revenue',
                      'runtime', 'vote_average', 'vote_count', 'spoken_languages']
    
            result = dict((field, data[field]) for field in fields)
    
            genres = []
            for i in range(len(result['genres'])):
                genres.append(result['genres'][i]['name'])
            result['genres'] = ", ".join(genres)
    
            spoken_languages = []
            for i in range(len(result['spoken_languages'])):
                spoken_languages.append(result['spoken_languages'][i]['name'])
            result['spoken_languages'] = ', '.join(spoken_languages)
    
            new_json.append(result)
        
        except JSONDecodeError:
            continue

    with open(json_out, "w") as outfile:
        json.dump(new_json, outfile, indent=4)
