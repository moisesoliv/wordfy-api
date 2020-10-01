from flask import Flask
from num2words import num2words


wordfy = Flask(__name__)

@wordfy.route('/<n>')
def num2txt(n):
    try:
        return {'extenso': num2words(n,lang='pt_BR').replace(',','')}, 200
    except:
        return '', 404

if __name__ == '__main__':
    wordfy.run(debug=True, host='0.0.0.0',port=3000)
