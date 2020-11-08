from app import app
from flask import Flask, request, redirect, render_template
from twilio.twiml.messaging_response import MessagingResponse
import requests
from SendSMS import SendSMS
from SMSParser import SMSParser
from forms import AnnouncementForm
import sys


@app.route('/')
@app.route('/index')
def index():
    return render_template('ui.html')
@app.route('/announcements', methods=['GET', 'POST'])
def announcements():
    form = AnnouncementForm()
    sms_sender = SendSMS()
    if form.validate_on_submit():
        text = form.message.data
        recipient = form.recipient.data
        
        phonebook = {
            'Daniel Li': '6099377475',
            'David Chen': '6099175688'
        }

        if recipient == 'All Students':
            for number in phonebook.values():
                success = sms_sender.send_sms(number,text)
        else:
            success = sms_sender.send_sms(phonebook[recipient],text)
        return render_template('index.html', success=success, form=form)
    else:
        return render_template('index.html', success=False, form=form, debug="hello")

@app.route('/sms',methods=['GET','POST'])
def sms():
    incoming_msg = request.values.get('Body','').lower()
    resp = MessagingResponse()
    msg = resp.message()
    sms_parser = SMSParser()
    result = sms_parser.parse(incoming_msg)
    if 'i.imgur.com' not in result:
        msg.body(result)
    else:
        msg.media(result)
    
    return str(resp)

@app.route('/about')
def about():
    return render_template('about.html')