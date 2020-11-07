from app import app
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

@app.route('/')
@app.route('/index')
def index():
    return "EduTools welcomes you!"

@app.route('/sms',methods=['GET','POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message("Hello World!")

    return str(resp)