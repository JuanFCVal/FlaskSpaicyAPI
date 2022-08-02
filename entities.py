import spacy
from spacy.lang.es.examples import sentences 
from flask_restful import Resource
from spacy.language import Language
import spacy_dbpedia_spotlight
from spacy_langdetect import LanguageDetector
class Entity(Resource):
    data = ''
    nlpes = None
    nlp = None
    sentences = []
    idiomDict = {}
    totalDict = {}
    def __init__(self):
        self.nlpes= spacy.load("es_core_news_sm")
        self.nlp = spacy.load('en_core_web_sm')
        self.nlp.add_pipe('dbpedia_spotlight')
        self.data = ''
        self.sentences  = []
        self.idiomDict = {}

    
    def remove_stopwords(self, doc):
        return [token for token in doc if not token.is_stop]

    def remove_empty_elements(self, list):
        newlist = []
        for element in list:
            if str(element) == "," or str(element) == " " or str(element) == ""  or str(element) == "." or str(element) =="  ":
                continue
            else:
                newlist.append(element)
        return newlist
    
    def ArrayToString(self, list):
        sentence = ""
        for element in list:
            sentence += str(element) + " "
        return sentence
     
    def getSentences(self):
        about_doc = self.nlp(self.data)
        self.sentences = list((about_doc.sents))
        result= map(self.turnString, self.sentences)
        self.sentences = list(result)


        
        

    def turnString(self, string):
        return str(string)
        
    def getEntities(self,language, sentence):
        newDict = {}
        entities = []
        values = []
        doc = self.nlp(sentence)
        entities = ([(ent.text, ent.label_, ent.kb_id_) for ent in doc.ents])
        newDict['entities'] = entities

        for element in doc.ents:
            if element._.dbpedia_raw_result != None:
                values.append(element._.dbpedia_raw_result)
        newDict ['values'] = values
        return newDict
    
    def sortLanguage(self,):
        def get_lang_detector(nlp, name):
            return LanguageDetector()
        Language.factory("language_detector", func=get_lang_detector)
        self.nlp.add_pipe('language_detector', last=True)
        removedStopWordsen = []
        removedStopWordses = []
        en = []
        es = []
        for sentence in self.sentences:
            doc = self.nlp(sentence)
            doces = self.nlpes(sentence)
            if(doc._.language['language'] == 'en'):
                stopwords = self.remove_stopwords(doc)
                stopwords = self.remove_empty_elements(stopwords)
                removedStopWordsen.append(self.ArrayToString(stopwords))
                en.append(sentence)   #list(filter(None, list2))
            else:
                stopwordses = self.remove_stopwords(doces)
                stopwordses = self.remove_empty_elements(stopwordses)
                removedStopWordses.append(self.ArrayToString(stopwordses))
                es.append(sentence)
        self.idiomDict['en'] = en
        self.idiomDict['es'] = es
        self.idiomDict['removedStopWordsEN'] = removedStopWordsen
        self.idiomDict['removedStopWordsES'] = removedStopWordses
        self.idiomDict
        
        
    def callEntities(self):
        esDict = {}
        enDict = {}
        for element in self.idiomDict['removedStopWordsES']:
            esDict[element] = self.getEntities("es", element)
        for element in self.idiomDict['removedStopWordsEN']:
            enDict[element] = self.getEntities("es", element)
        self.totalDict['idiomResult'] = self.idiomDict
        self.totalDict['esEntities'] = esDict
        self.totalDict['enEntities'] = enDict
                

        
    def get(self, text):
        self.data = text
        self.getSentences()
        self.sortLanguage()
        self.callEntities()
        return {'result': self.totalDict}
        