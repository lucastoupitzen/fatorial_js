#!/usr/local/bin/python3
import csv
import PySimpleGUI as sg


def calcula_entalpia(lis, ti, tf):

    delta = 0
    for i in range(len(lis)):
        delta += lis[i]*(tf**(i+1)-ti**(i+1))/(i+1)

    return delta


def ajusta_nome(nome):

    palavra = nome.upper()
    return palavra.replace(' ', '')


def pega_parametros(nome):

    nome = ajusta_nome(nome)
    with open("dados_cp_sistema2.csv") as arquivo:
        dados = arquivo.read()
        lista_nomes_quim = []
        lista_nomes = []
        lista_a = []
        lista_b = []
        lista_c = []
        lista_d = []
        lista_e = []
        a, b, c, d, e = 0, 0, 0, 0, 0
        for registro in csv.reader(dados.splitlines()):
            lista_nomes_quim.append(registro[1])
            lista_nomes.append(registro[2])
            lista_a.append(registro[3])
            lista_b.append(registro[4])
            lista_c.append(registro[5])
            lista_d.append(registro[6])
            lista_e.append(registro[7])
        for i in range(len(lista_nomes)):
            if lista_nomes[i][1:] == nome or lista_nomes_quim[i][1:] == nome:
                a = float(lista_a[i])
                b = float(lista_b[i])
                c = float(lista_c[i])
                d = float(lista_d[i])
                e = float(lista_e[i])
                lista_final = [a, b, c, d, e]
            else:
                lista_final = [a, b, c, d, e]
    return lista_final


class TelaPython():

    def __init__(self):
        sg.change_look_and_feel('Darkred1')

        # Layout
        layout = [
            [sg.Text('Qual é o nome ou fórmula da substância?',
                     size=(20, 1), font=('consolas', 20)),
             sg.Input(size=(5, 1), key='nome', font=('consolas', 17))],
            [sg.Text('Qual é a temperatura inicial (em Kelvin)?',
                     size=(40, 1), font=('consolas', 20)),
             sg.Input(size=(5, 1), key=('temperatura_i'), font=('consolas', 17))],
            [sg.Text('Qual é a temperatura final (em Kelvin)?',
                     size=(40, 1), font=('consolas', 20)),
             sg.Input(size=(5, 1), key=('temperatura_f'), font=('consolas', 17))],
            [sg.Button('Calcular')],
            [sg.Output(size=(50, 2), font=('consolas', 17))]
        ]

        # janela
        self.janela = sg.Window("Cálculo de entalpia",
                                resizable=True).layout(layout)
        self.janela.read(timeout=1)
        for g in range(5):
            for i in layout[g]:
                i.expand(expand_x=True, expand_y=True)

        # Extrair os dados
    def Iniciar(self):

        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            temperatura_i = float(self.values['temperatura_i'])
            temperatura_f = float(self.values['temperatura_f'])
            nome = ajusta_nome(nome)
            resultado = calcula_entalpia(pega_parametros(
                nome), temperatura_i, temperatura_f)
            if temperatura_i < 0 or temperatura_f < 0:
                print('A temperatura não pode ser negativa!')
            elif resultado != 0:
                print('A variação de entalpia foi de %.2f J/mol' % resultado)
            else:
                if temperatura_f != temperatura_i:
                    print('A substância não foi encontrada')
                elif pega_parametros(nome) != [0, 0, 0, 0, 0]:
                    print('Não há variação de entalpia')
                else:
                    print('A substância não foi encontrada')


tela = TelaPython()
tela.Iniciar()
