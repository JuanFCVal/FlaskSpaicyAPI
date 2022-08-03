# APPPEDIA BACKEND
## Universidad Técnica Particular de Loja.
## Knowledge-based systems  
### ProJect Title : APPPEDIA ->  API REST for get entities and information from DBPEDIA using python and flask.
> Student: Juan Francisco Cevallos Valdivieso. April- August 2022. Professor: Nelson Piedra.
# FlaskSpaicyAPI
This is a Flask Rest API that uses spacy for detect Entities in DBPedia and start using NLP for text process.
#### For making this REST API work on localhost you have to follow these steps:
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
5. Test API.
For Test the API you have to go into your localhost direction and use 'entity/{YOUR TEXT HERE}' 
>Note. In case you want to use `Flask run` first you have to set FLASK APP as a environment variable. 

Feel free to use, change, reply this API in your personal or comercial projects, I would be glad you to. 
You can find wokring API on  [API] (https://flask-sbc.herokuapp.com/).
For getting entities and text process (Detect language en or es, remove stopwords) use `/entity/YOUR TEXT HERE`
