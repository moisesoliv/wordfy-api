from flask import Flask
# from num2words import num2words
from extenso import Converter
import os

wordfy = Flask(__name__)
conv = Converter()
port = int(os.environ.get("$PORT", 5000))

@wordfy.route('/<n>')
def num2txt(n):
    try:
        number = int(n)
        assert -99999 <= number <= 99999
        words = {'extenso': conv.extenso(number)}
        return words, 200
    except:
        return (n + ' nao é um numero valido'), 404


if __name__ == '__main__':
    wordfy.run(debug=True, host='0.0.0.0', port=port)
