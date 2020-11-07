import os
from os.path import join, dirname
from dotenv import load_dotenv
import sys
import base64
import requests
import json
import wolframalpha

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MATHPIX_SID = os.environ.get("MATHPIX_SID")
MATHPIX_KEY = os.environ.get("MATHPIX_KEY")
WOLFRAM_APP_ID = os.environ.get("WOLFRAM_APP_ID")


class MathSolver():
    def read_math(self, file_path):
        image_uri = "data:image/jpg;base64," + \
            base64.b64encode(open(file_path, "rb").read()).decode()
        headers = {
            "content-type": "application/json",
            "app_id": MATHPIX_SID,
            "app_key": MATHPIX_KEY
        }
        r = requests.post('https://api.mathpix.com/v3/text',
                          data=json.dumps({'src': image_uri}),
                          headers=headers)

        json_objects = json.loads(r.text)
        latex_str = json_objects['latex_styled']

        return latex_str

    def solve_math(self, latex_str):
        client = wolframalpha.Client(WOLFRAM_APP_ID)
        res = client.query(latex_str)
        return next(res.results).text


if __name__ == "__main__":
    solver = MathSolver()
    equation = solver.read_math('test.jpg')
    equation = f'r"{equation}"'
    print(equation)
    print(solver.solve_math(equation))
