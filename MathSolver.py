import os
from os.path import join, dirname
from dotenv import load_dotenv
import sys
import base64
import requests
import json
import wolframalpha
from PIL import Image
import io
import urllib.parse
from imgurpython import ImgurClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MATHPIX_SID = os.environ.get("MATHPIX_SID")
MATHPIX_KEY = os.environ.get("MATHPIX_KEY")
WOLFRAM_APP_ID = os.environ.get("WOLFRAM_APP_ID")
IMGUR_ID = os.environ.get("IMGUR_ID")
IMGUR_SECRET = ("IMGUR_SECRET")


class MathSolver():

    def __init__(self):
        self.client = wolframalpha.Client(WOLFRAM_APP_ID)

    def read_math(self, file_path):
        image_uri = "data:image/jpg;base64," + \
            base64.b64encode(open(file_path, "rb").read()).decode()
        headers = {
            "content-type": "application/json",
            "app_id": MATHPIX_SID,
            "app_key": MATHPIX_KEY
        }
        r = requests.post('https://api.mathpix.com/v3/text',
                          data=json.dumps({'src': image_uri, "formats": [
                                          "data"], "data_options": {"include_asciimath": "true"}}),
                          headers=headers)

        json_objects = json.loads(r.text)
        ascii_str = json_objects['data'][0]['value']

        return ascii_str

    def solve_math(self, ascii_str):
        res = self.client.query(ascii_str)
        print(res.keys())
        for pod in res.pods:
            for sub in pod.subpods:
                print(sub.plaintext)
        # return next(res.results).text
        # return res.text

    def solve_math2(self, ascii_str):
        query = f'http://api.wolframalpha.com/v1/simple?appid={WOLFRAM_APP_ID}&i={urllib.parse.quote(ascii_str)}'
        print(query)
        res = requests.get(query)
        i = Image.open(io.BytesIO(res.content))
        imgByteArr = io.BytesIO()
        i.save(imgByteArr, format="PNG", optimize=True, quality=95)
        imgByteArr = imgByteArr.getvalue()
        url = 'https://api.imgur.com/3/image'
        files = {
            'image': imgByteArr
        }
        headers = {"Authorization": f"Client-ID {IMGUR_ID}"}
        resp = requests.post(url, data=files, headers=headers)
        print(resp)
        return resp.json()['data']['link']


if __name__ == "__main__":
    solver = MathSolver()
    equation = solver.read_math('test1.jpg')
    print(equation)
    print(solver.solve_math2("find zeroes for: " + equation))
