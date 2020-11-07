from twilio.rest import Client
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

body = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent blandit risus vel semper laoreet. Etiam tristique eros tortor, sit amet rutrum ipsum pulvinar at. Aenean porta in nibh vel varius. Nunc mattis vestibulum nisi non interdum. Donec porttitor massa enim, eu elementum justo tempus quis. Mauris nisi est, scelerisque at sagittis non, scelerisque lacinia quam. In aliquam, urna blandit faucibus finibus, lorem ligula auctor justo, nec porta neque odio et diam. Duis congue mattis justo, ac tincidunt ipsum finibus vel. Vestibulum consectetur non tellus at auctor. Sed condimentum tortor in libero semper, vitae accumsan urna faucibus. Integer sodales sit amet libero vitae semper. Phasellus porttitor vehicula suscipit. Proin ac viverra mauris. Nulla facilisi.

Duis dolor odio, fringilla at orci a, facilisis egestas leo. Mauris egestas id sem vitae posuere. Quisque in interdum neque, convallis lobortis velit. Donec posuere quis nisl id ultricies. Nulla fermentum vitae nunc nec lacinia. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ornare lacus eu lorem faucibus tincidunt. Donec accumsan nunc a metus tristique congue eget a neque. Nulla sed bibendum sapien, id rutrum velit. Fusce efficitur mattis magna. Sed ex lectus, hendrerit eget aliquet at, gravida quis neque. Cras aliquet at nisl eget facilisis. Mauris ac dictum ipsum, in venenatis nisl. Etiam sit amet risus nisl.

Donec et varius risus. Donec eu elit quam. 
'''

client = Client()
message = client.messages.create(
    to="+16099175688", from_="+12059272579", body=body)
