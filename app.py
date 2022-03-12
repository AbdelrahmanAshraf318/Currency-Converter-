from flask import Flask, jsonify, render_template, request, url_for, redirect, send_file, session
import os
import requests
from flask import *  

app = Flask(__name__)

def get_result(amount , dist , to):
    url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

    querystring = {"have":dist,"want":to,"amount":amount}

    headers = {
        'x-rapidapi-host': "currency-converter-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "7fd28c8244msh192131f69ff095ep140a0ajsn0a5f135310eb"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()    

    return data["new_amount"]


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    amount = request.form['Amount']
    dist = request.form['From']
    to = request.form['To']
    
    return render_template('index.html' , x = get_result(amount , dist , to))


