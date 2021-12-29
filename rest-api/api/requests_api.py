import requests
 
from flask import Flask,request,jsonify,render_template,redirect,url_for,session 

class RequestsApi:
    url = "https://api.stagingeb.com/v1/properties" 
    headers = { 'X-Authorization':"l7u502p8v46ba3ppgvj5y2aad50lb9" }
    # querystring = {"limit":"1","page":"1"}
    
    @staticmethod
    def save_api():
        try:
             
            return "True"
        except:
            return "False"    
        
    @staticmethod
    def get_all_api():
        try:
            
              
         #  response = requests.request("GET", RequestsApi.url, headers=RequestsApi.headers, params=RequestsApi.querystring)
            response = requests.request("GET", RequestsApi.url, headers=RequestsApi.headers)

            return  response.json()
        
        except:
            return "No funcionó" 
    # @staticmethod
    # def get_one_api():
    #     try:
    #         return 'True'
            
            
    #     except:
    #         return "False"  
        
    # @staticmethod
    # def delete_api():
    #     try:
    #         return 'True'
            
            
    #     except:
    #         return "False"              