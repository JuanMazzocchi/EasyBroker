from flask import Flask,request,jsonify,render_template,redirect,url_for,session 
import requests
from api.requests_api import RequestsApi
import http.client
import json
app= Flask (__name__)
app.secret_key='cualquiera'


@app.route('/', methods=["GET"])  
def mostrar():    
    res = RequestsApi.get_all_api()
    titulos=[]
    print(len(res['content']))
    i=0
    while len(res['content']) > i:
        print(res['content'][i]['title'])
        
        titulos.append(res['content'][i]['title'])
        i+=1
        print("-----------------------------")
        
  
    return render_template('propiedades.html', titulos=titulos )


 



if __name__=='__main__':
    app.run(debug=True)