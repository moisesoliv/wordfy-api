from flask import Flask
from num2words import num2words


wordfy = Flask(__name__)

@wordfy.route('/<n>')
def num2txt(n):
    try:
        # Foi utilizada a biblioteca num2words disponivel em
        # https://pypi.org/project/num2words/
        words = {'extenso': num2words(n,lang='pt_BR').replace(',',' e')}
        return words, 200
    except:
        return (n + ' nao é um numero valido'), 404


if __name__ == '__main__':
    wordfy.run(debug=True, host='0.0.0.0',port=3000)
