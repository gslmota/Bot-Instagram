# Importando bibliotecas para criação do bot

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from PySimpleGUI import PySimpleGUI as sg

# Foi Usado o conceito de orientação a objeto para criar este bot.

class BotInstagram:
    def __init__(self, username, password, url, coments):
        self.username = username
        self.password = password
        self.url = url
        self.coments = coments.split(',')
        self.driver = webdriver.Firefox(executable_path="C:\Users\gabri\OneDrive\Documentos\MeusRepositorios\Bot-Instagram\geckodriver-v0.27.0-win64\geckodriver.exe") # Coloque aqui o caminho para o seu geckdriver.
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        user_camp = driver.find_element_by_xpath("//input[@name='username']")
        user_camp.click()
        user_camp.clear()
        user_camp.send_keys(self.username)
        user_password = driver.find_element_by_xpath("//input[@name='password']")
        user_password.click()
        user_password.clear()
        user_password.send_keys(self.password)
        user_password.send_keys(Keys.RETURN) # key ENTER
        time.sleep(5)
        while True:
            self.coment_picture()
            time.sleep(random.randint(240, 300))
        
    @staticmethod
    def write_people(coment, place):
        for letter in coment:
            place.send_keys(letter)
            time.sleep(random.randint(1,5)/30)

    def coment_picture(self):
        driver = self.driver
        driver.get(self.url)
        time.sleep(5)
        cont = 1
        while cont <= 8:
            try:
                coment_list = self.coments
                driver.find_element_by_class_name('Ypffh').click()
                coment_camp = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2,5))
                self.write_people(random.choice(coment_list), coment_camp)
                time.sleep(random.randint(10,20))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(random.randint(3,6))
            except Exception as e:
                print(e)
                time.sleep(4)
            cont += 1



#layout

sg.theme('DarkTanBlue')
sg.popup('Bem vindo ao Instagram Bot!')
sg.popup('Separe os comentários com vírgulas!')
layout = [
    [sg.Text('Usuário', size=(9, 1), justification='left'), sg.Input(key='username')],
    [sg.Text('Senha', size=(9, 1), justification='left'), sg.Input(key='password', password_char='*')],
    [sg.Text('URL da Foto', justification='left'), sg.Input(key='url')],
    [sg.Text('Comentários', justification='left'), sg.Input(key='coment')],
    [sg.Button('Login')]
]

#Janela

window = sg.Window('Instagram Bot', layout)

#Ler os eventos

while True:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Login':
        bot = BotInstagram(value['username'], value['password'], value['url'], value['coment'])
        time.sleep(3)
        window.close()
        bot.login()

# FIM!!!