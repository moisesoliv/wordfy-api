from flask import Flask
from num2words import num2words


wordfy = Flask(__name__)

@wordfy.route('/<n>')
def num2txt(n):
    return {'extenso': num2words(n,lang='pt_BR').replace(',','')}, 200

if __name__ == '__main__':
    wordfy.run(port=3000)