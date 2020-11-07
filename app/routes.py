from app import app
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests
import SendSMS

@app.route('/')
@app.route('/index')
def index():
    return "EduTools welcomes you!"

@app.route('/sms',methods=['GET','POST'])
def sms():
    incoming_msg = request.values.get('Body','').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if '1' in incoming_msg:
        msg.body('Math Solver')
        responded = True
    elif '2' in incoming_msg:
        msg.body('Wikipedia')
        responded = True
    elif '3' in incoming_msg:
        msg.body('Due Dates')
        responded = True
    elif '4' in incoming_msg:
        msg.body('GoodBye!')
        responded = True
        running = False
    if not responded:
        msg.body('You had some invalid input')

    return str(resp)