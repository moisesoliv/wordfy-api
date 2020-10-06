class Converter:
    milhar = {   
        0: 'zero',              
        1: 'um',     11: 'onze',      10: 'dez',       100: 'cem',
        2: 'dois',   12: 'doze',      20: 'vinte',     200: 'duzentos',
        3: 'três',   13: 'treze',     30: 'trinta',    300: 'trezentos',
        4: 'quatro', 14: 'quatorze',  40: 'quarenta',  400: 'quatrocentos',
        5: 'cinco',  15: 'quinze',    50: 'cinquenta', 500: 'quinhentos',
        6: 'seis',   16: 'dezesseis', 60: 'sessenta',  600: 'seiscentos',
        7: 'sete',   17: 'dezessete', 70: 'setenta',   700: 'setecentos',
        8: 'oito',   18: 'dezoito',   80: 'oitenta',   800: 'oitocentos',
        9: 'nove',   19: 'dezenove',  90: 'noventa',   900: 'novecentos',
    }

    def ate999(self, n):
        ''' Se o numero está na lista dos numeros conhecidos retorna o numero.
        caso contrario quebramos o numero em partes menores que estão listados
        '''

        assert 0 <= n < 1000
        if n in self.milhar:
            return self.milhar[n]
        else:
            pot10 = len(str(n))-1
            cabeca, corpo = divmod(n, 10**pot10)
            redondo = cabeca * 10**pot10
            if redondo == 100:
                prefixo = 'cento'
            else:
                prefixo = self.milhar[redondo]
            return prefixo + ' e ' + self.ate999(corpo)

    def extenso(self, n):
        ''' divide as potencias de 1000 em partes
        e traduz o nome em partes menores e conhecidas
        '''
        if n < 0:
            sinal = 'menos '
            return sinal + self.extenso(abs(n))
        if n < 1000:
            return self.ate999(n)
        else:
            pot1000 = (len(str(n))-1)//3
            cabeca, corpo = divmod(n, 1000**pot1000)
            if pot1000 == 1 and cabeca == 1:
                prefixo = 'mil'
            else:
                prefixo = (self.ate999(cabeca) + ' mil')
            if corpo:
                if prefixo == 'mil':
                    conector = ' '
                else:
                    conector = ' e '
                return prefixo + conector + self.extenso(corpo)
            else:
                return prefixo
