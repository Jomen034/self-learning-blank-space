# self-learning-blank-space
# Fetching Data from Large JSON File
When dealing with large JSON file, it is common that the JSON may be as a normal JSON or the Nested JSON. This code function is to extract and clean data from JSON files with huge JSON files. <br>

![image](https://user-images.githubusercontent.com/71366136/115444868-535a5380-a23f-11eb-9f15-75d6ea10cc2a.png)

This code function allows us to fetch the data from JSON file with some specific fields requirements as needed. For this JSON file, expected results will contain the following information:<br>

```
{
        "original_title": "Lock, Stock and Two Smoking Barrels",
        "budget": 1350000,
        "genres": "Comedy, Crime",
        "popularity": 7.119,
        "release_date": "1998-03-05",
        "revenue": 28356188,
        "runtime": 105,
        "vote_average": 8.2,
        "vote_count": 4048,
        "spoken_languages": "English"
    },
    {
        "original_title": "La estrategia del caracol",
        "budget": 0,
        "genres": "Comedy, Drama",
        "popularity": 2.968,
        "release_date": "1993-12-25",
        "revenue": 0,
        "runtime": 116,
        "vote_average": 7.1,
        "vote_count": 35,
        "spoken_languages": "Espa\u00f1ol"
    },
    {
        "original_title": "DevilDolls",
        "budget": 0,
        "genres": "Horror",
        "popularity": 2.065,
        "release_date": "2012-01-01",
        "revenue": 0,
        "runtime": 90,
        "vote_average": 3.6,
        "vote_count": 5,
        "spoken_languages": "English"
    },
```

# Installation
Use git to clone this repository

```
git clone https://github.com/Jomen034/self-learning-blank-space.git
```

## Prerequisite
To run the code funtion, make sure your environment has the following prerequisite library 

`json`, `Path from pathlib`, `glob`

If you don't, you can install them by run this command in your command prompt:

```
pip install jsonlib
pip install glob2
pip install pathlib
```

## Usage
You can run the code funtion program by executing `main.py` file. But before it, you can specify the `json_src` as the directory file of your JSON file and `json_out` as the output file.

```
json_src = 'path/to/dir'
json_out = 'file_name.json'
```

Run the program by execute the `main.py` file

# Notes
* As the JSON file consist +500k file, it took long time for the process. In this repository, I only used `sample data`
* This huge JSON file consist Nested JSON, especially in `genres` and `spoken_languages` key that to be returned. 

# Contact
For further information like to get the real data for the usage in this code function, contact me on <jomenpardede@gmail.com>
