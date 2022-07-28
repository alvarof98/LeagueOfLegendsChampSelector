from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib  


app = Flask(__name__)
app.debug = True


class Models(object):
    
    def __init__(self):
        self.__df_campeones = pd.read_json('campeones.json')
    
    def model_top(self,lista):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_top.pkl')
        yhat = modelo.predict([lista])
        return self.df_model_top1().loc[yhat[0]]['nombre']
           
    def model_jgl(self):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_jgl.pkl')
        yhat = modelo.predict([lista])
        return self.df_model_jgl1().loc[yhat[0]]['nombre']

        
    def model_mid(self):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_mid.pkl')
        yhat = modelo.predict([lista])
        return self.df_model_mid1().loc[yhat[0]]['nombre']

    def model_adc(self):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_adc.pkl')
        yhat = modelo.predict([lista])
        return self.df_model_adc1().loc[yhat[0]]['nombre']
    
    def model_sup(self):
        aux = []
        for i in lista:
            if i == "missing":
                aux.append(999)
            else:
                aux.append(self.__df_campeones[self.__df_campeones['nombre'] == i]['id'])
        lista = aux
        for i in range(len(lista)):
            if lista[i] == 999:
                aleatorio = np.random.randint(160)
                lista[i] = self.__df_campeones.loc[aleatorio]['id']
        modelo = joblib.load('modelo_sup.pkl')
        yhat = modelo.predict([lista])
        return self.df_model_sup1().loc[yhat[0]]['nombre']
    
@app.route("/api", methods=['POST'])
def index():
        objeto = Models()
        name = request.form["name"]
        lista = request.form["lista"]
        if name == "top":
            return objeto.model_top(lista)
        elif name == "jgl":
            return objeto.model_jgl(lista)
        elif name == "mid":
            return objeto.model_mid(lista)
        elif name == "adc":
            return objeto.model_adc(lista)
        else:
            return objeto.model_sup(lista)


if __name__ == "__main__":
    app.run()
    