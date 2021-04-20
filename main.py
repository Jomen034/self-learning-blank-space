# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 22:45:47 2021

@author: jomen
"""
import glob
from pathlib import Path
import CombineJson as comb_json

json_src = r"C:\Users\jomen\Documents\self_project\self-learning-blank-space\sample data"
json_out = 'sample_full_movies.json'

files = glob.glob(json_src + "\**\*.json", recursive=True)

comb_json.combine_json(json_src, json_out, files)