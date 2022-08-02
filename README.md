# FlaskSpaicyAPI
This is a Flask Rest API that uses spacy for detect Entities in DBPedia and start using NLP for text process.
##For making this REST API work on localhost you have to follow these steps:
1. Clone repository.
Clone or Fork these repository in your local device.
2. Create a virtual environment.
```
python3 -m venv /path/to/new/virtual/environment
path\to\venv\Scripts\activate
```
3. Then install requirements.txt with the virtualenv working.
`pip install -r requirements.txt`
4. The run the API  
```
cd FlaskSpacyApi
python main.py
```
>Note. In case you want to use `Flask run` first you have to set FLASK APP as a environment variable. 
