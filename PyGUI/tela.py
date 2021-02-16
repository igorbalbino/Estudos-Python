#IMPORTA CLASSE
import PySimpleGUI as sg;

#CRIA CLASSE TELA
class TelaPython:
    #CRIA FUNCAO CONSTRUTOR
    def __init__(self):
        #LAYOUT
        layout = [
            #CRIA ELEMENTO NA TELA COM UM INPUT PARA RECEBER DADOS
            [sg.Text('Name', size=(5, 0)), sg.Input(size=(20, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(20, 0), key='idade')],
            #COMANDO PARA CRIAR CHECKBOX
            [sg.Text('Quais provedores de Email são aceitos ?')],
            [sg.Checkbox('Gmail', key='gmail'),
             sg.Checkbox('Outlook', key='outlook'),
             sg.Checkbox('Yahoo', key='yahoo')],
            #DECLARANDO BOTOES RADIUS
            [sg.Text('Aceita cartões ?')],
            #DECLARA-SE DA SEGUINTE FORMA "sg.Radio('VALOR','GRUPO_RADIUS_A_QUE_PERTENCE')"
            [sg.Radio('Sim', 'cartoes', key='aceitaC'),sg.Radio('Não', 'cartoes', key='nAceita')],
            #CRIA SLIDER PARA CONTROLAR A VELOCIDADE QUE ALGO ACONTECE
            [sg.Slider(range=(0, 255), default_value=0, orientation='h',size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados',size=(30, 0))],
            #CRIA TELA DE OUTPUT PARA MOSTRAR OS DADOS NO LAYOUT
            [sg.Output(size=(30, 10))]
        ];
        #JANELA
        #CRIA A TELA E COLOCA OS ELEMENTOS DE LAYOUT NELA
        self.janela = sg.Window('Dados do Usuário').layout(layout);
        #EXTRAIR DADOS DA TELA
        #PEGA OS DADOS DOS INPUTS E USA O METODO READ() NA JANELA PARA GRAVAR OS DADOS
        #self.button, self.values = self.janela.Read();
        #^ ISSO FOI PASSADO PARA DENTRO DE UM "while" NA FUNCAO "Iniciar"

    #FECHA __init__

    def Iniciar(self):
        while True:
            # EXTRAIR DADOS DA TELA
            self.button, self.values = self.janela.Read();
            #IMPRIMI INFORMAÇÕES EXTRAIDAS DA TELA
            #print(self.values);
            nome = self.values['nome'];
            idade = self.values['idade'];
            aceita_gmail = self.values['gmail'];
            aceita_outlook = self.values['outlook'];
            aceita_yahoo = self.values['yahoo'];
            aceita_cartao = self.values['aceitaC'];
            #nao_aceita_cartao = self.values['nAceita'];
            slider_velocidade = self.values['sliderVelocidade'];

            print(f'Nome: {nome}');
            print(f'Idade: {idade}');
            print(f'Aceita Gmail: {aceita_gmail}');
            print(f'Aceita Outlook: {aceita_outlook}');
            print(f'Aceita Yahoo: {aceita_yahoo}');
            print(f'Velocidade: {slider_velocidade}');
            #SINTAXE IF ELSE.
            #PODE-SE USAR ELIF ENTRE OS IF E O ELSE
            #CONDICIONAIS COM TESTE BOOLEAN USAM "True" E "False", DESSA FORMA
            if aceita_cartao == True:
                print(f'Aceita cartão: Sim.');
            else:
                print(f'Aceita cartão: Não.');
        #FECHA while
    # FECHA Iniciar

#INSTANCIA CLASSE TelaPython EM tela
tela = TelaPython();
tela.Iniciar();

'''
PODEM SER FEITAS CUSTOMIZAÇÕES DESSES CAMPOS COM COMANDOS DA BIBLIOTECA BAIXADA (PySimpleGUI).
ADICIONANDO, POR EXEMPLO, O COMANDO "size=(5,0)"
SIGNIFICA QUE O ELEMENTO IRÁ OCUPAR 5 ESPAÇOS DE CARACTÉRE NAQUELA LINHA.

PODEMOS USAR TAMBEM O COMANDO "key='NOME_PARA_IDENTIFICAR'" PARA QUE, QUANDO CLICAR EM SUBMIT E PRINTAR OS DADOS,
SEJAM IDENTIFICADOS POR NOME E NÃO POR NÚMERO.
COMANDO "print(self.values);" ESTÁ RETORNANDO OS VALORES IDENTIFICADOS POR NÚMEROS, EM LISTA, INICIANDO EM 0.

PARA PEGAR OS VAORES RETORNADOS DA TELA,
BASTA CRIAR A VARIAVEL COM O NOME DESEJADO E REFERENCIAR VIA INDEX DENTRODE COLXETE:
"nome = self.values['IDENTIFICADOR'];"

ATRIBUIR AO ALGO AO ESCOPO DE "self", DE FORMA BEM GENERICA,
SIGNIFICA QUE PODE ACESSAR ISSO EM QUALQUER LUGAR ONDE SEJA COLOCADO "self.O_QUE_QUER_ACESSAR"

PROPRIEDADES sg.Slider():
range=(0, 255) - 
default_value=0 = VALOR INICIAL DO SLIDER
orientation='h' - ORIENTAÇÃO DO SLIDER (h = horizontal, v = vertical)
'''