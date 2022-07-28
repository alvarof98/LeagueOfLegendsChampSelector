import pandas as pd
import numpy as np
import joblib  
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://alvarof98.github.io/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Models(object):
    
    def __init__(self):
        self.__df_campeones = pd.read_json('campeones.json')

    def getDf(self):
        return self.__df_campeones
    
    def model_top(self,lista):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'].values[0])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_top.pkl')
        yhat = modelo.predict([lista])
        df_c = self.__df_campeones[self.__df_campeones['rol'] == 'top'].reset_index(drop = True)
        return df_c.loc[yhat[0]]['nombre']

           
    def model_jgl(self,lista):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'].values[0])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_jgl.pkl')
        yhat = modelo.predict([lista])
        df_c = self.__df_campeones[self.__df_campeones['rol'] == 'jgl'].reset_index(drop = True)
        return df_c.loc[yhat[0]]['nombre']

        
    def model_mid(self,lista):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'].values[0])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_mid.pkl')
        yhat = modelo.predict([lista])
        df_c = self.__df_campeones[self.__df_campeones['rol'] == 'mid'].reset_index(drop = True)
        return df_c.loc[yhat[0]]['nombre']

    def model_adc(self,lista):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'].values[0])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_adc.pkl')
        yhat = modelo.predict([lista])
        df_c = self.__df_campeones[self.__df_campeones['rol'] == 'adc'].reset_index(drop = True)
        return df_c.loc[yhat[0]]['nombre']
    
    def model_sup(self,lista):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'].values[0])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_sup.pkl')
        yhat = modelo.predict([lista])
        df_c = self.__df_campeones[self.__df_campeones['rol'] == 'sup'].reset_index(drop = True)
        return df_c.loc[yhat[0]]['nombre']


class Book(BaseModel):
    name: str
    lista: list



@app.get("/")
def read_root():
    return {"Init": "App"}


@app.post("/pred/")
async def create_pred(book : Book):
    objeto = Models()
    booksito = []
    for i in book:
        booksito.append(i)
    if booksito[0][1] == "top":
        prueba = objeto.model_top(booksito[1][1])
    elif booksito[0][1] == "jgl":
        prueba = objeto.model_jgl(booksito[1][1])
    elif booksito[0][1] == "mid":
        prueba = objeto.model_mid(booksito[1][1])
    elif booksito[0][1] == "adc":
        prueba = objeto.model_adc(booksito[1][1])
    else:
        prueba = objeto.model_sup(booksito[1][1])
    return prueba