import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
#1


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options)
wait = WebDriverWait(driver, 10)  # Ajuste o tempo



def clickXPATh(path):
    b = True
    while b == True:
        try:
            element = driver.find_element(By.XPATH, path)
            element.click()
            b=False
        except:
            pass

def clickLink(link):
    b = True
    while b == True:
        try:
            element = driver.find_element(By.PARTIAL_LINK_TEXT, link)
            element.click()
            b=False
        except:
            pass
    
    

def insert(path, data):
    b = True
    while b == True:
        try:
            element = driver.find_element(By.XPATH, path)
            element.send_keys(data)
            b=False
        except:
            pass

def  find_dados(numero_estudante):
    b = True
    while b == True:
        try:
            xpath1 = f"//table//td[contains(text(), '{numero_estudante}')]/parent::tr"
            linha_estudante = driver.find_element(By.XPATH, xpath1)
            b = False
            return linha_estudante
        except:
            pass

def find_descricao():
    b = True
    while b == True:
        try:
            xpath2 = "//table//th[contains(text(), 'Número')]/parent::tr"
            linha_descricao = driver.find_element(By.XPATH, xpath2)
            b = False
            return linha_descricao
        except:
            pass

def find_maximos():
    b = True
    while b == True:
        try:
            xpath3 = "//table//td[b[contains(text(), 'Máxima')]]/parent::tr"
            linha_detalhes = driver.find_element(By.XPATH, xpath3)
            b = False
            return linha_detalhes
        except:
            pass



def encontrar(numero_estudante):
    
    encontrado: bool
    dados = []
    descricao = []
    maximos = []
    try:
        time.sleep(5)
        
        
        
        # Extrair dados adicionais da linha de estudante (tr)
        linha_estudante = find_dados(numero_estudante)
        dados_colunas1 = linha_estudante.find_elements(By.TAG_NAME, "td")
        for coluna in dados_colunas1:
            texto_coluna = coluna.text
          
            dados.append(texto_coluna)
        encontrado = True

        # Extrair dados adicionais da linha da descricao (tr)
        linha_descricao = find_descricao()
        dados_colunas2 = linha_descricao.find_elements(By.TAG_NAME, "th")
        for coluna in dados_colunas2:
            texto_coluna = coluna.text
           
            descricao.append(texto_coluna)
        
        # Extrair dados adicionais da linha dos valores maximos (tr)
        linha_maximos = find_maximos()
        dados_colunas3 = linha_maximos.find_elements(By.TAG_NAME, "td")
        for coluna in dados_colunas3:
            texto_coluna = coluna.text
           
            maximos.append(texto_coluna)

        encontrado = True

        return encontrado, dados, descricao, maximos
    except NoSuchElementException:
        encontrado = False
        return encontrado, dados, descricao, maximos
    

    


def getNotas(curso, cadeira, nr):
    print('==BOT STARTED==')
    driver.get('https://fenix.isutc.ac.mz/isutc/fenixEduIndex.do')
    clickXPATh('//*[@id="logout"]/a')
    insert('//*[@id="username"]', 'yannick.matimbe')
    insert('//*[@id="password"]', 'Y@nnick2003')

    clickXPATh('//*[@id="fm1"]/div[4]/input[4]')
    clickXPATh('//*[@id="content"]/div/center/a[2]')
    clickLink(curso)
    clickXPATh('//*[@id="latnav"]/ul/li[5]/a/span')
    clickLink(cadeira)
    clickXPATh('//*[@id="latnav"]/ul[1]/li[4]/a')
    clickLink('Rendimento académico')

    encontrado, dados, descricao, maximos = encontrar(nr)
    print(len(dados))
    retorno = []
    if(encontrado):
        print("aluno encontrado")
        print(len(descricao))
        print(len(maximos))
        
        for i in range(0, len(dados)):
            if i >=3:
                line = descricao[i]+ ': '+ dados[i]+'/'+maximos[i-1]
                retorno.append(line)
            else:
                line = descricao[i]+ ': '+ dados[i]
                retorno.append(line)

    else:
        print("aluno nao encontrado")

    return retorno




