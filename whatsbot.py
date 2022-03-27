# Automatização do WhatsApp Web

from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')

while len(driver.find_elements_by_id("side")) < 1:
    time.sleep(1)
    
contatos = ['Osvaldo Filho']
mensagem = 'Teste do Zap'

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath("//div[contains(@class,'copyable-text selectable-text')]")
    time.sleep(8)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath("//div[contains(@class,'copyable-text selectable-text')]")      
    campo_mensagem[1].click()
    time.sleep(4)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(8)
    campo_mensagem[1].send_keys(Keys.ENTER)   
    
for contato in contatos:
    buscar_contato(contato) 
    enviar_mensagem(mensagem)   
