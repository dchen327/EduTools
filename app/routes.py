from app import app
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests
import SendSMS
from SMSParser import SMSParser

@app.route('/')
@app.route('/index')
def index():
    return "EduTools welcomes you!"

@app.route('/sms',methods=['GET','POST'])
def sms():
    incoming_msg = request.values.get('Body','').lower()
    resp = MessagingResponse()
    msg = resp.message()
    sms_parser = SMSParser()
    if 'start' in incoming_msg:
        msg.body(sms_parser.commands())
    msg.body(sms_parser.parse(incoming_msg))
    
    return str(resp)