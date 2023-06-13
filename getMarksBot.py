import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException



chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()



def clickXPATh(path):
    element = driver.find_element(By.XPATH, path)
    element.click()

def clickLink(link):
    element = driver.find_element(By.PARTIAL_LINK_TEXT, link)
    element.click()

def insert(path, data):
    element = driver.find_element(By.XPATH, path)
    element.send_keys(data)

def encontrar(numero_estudante):
    encontrado: bool
    dados = []
    detalhes = []
    try:
        xpath1 = f"//table//td[contains(text(), '{numero_estudante}')]/parent::tr"
        xpath2 = "//table//th[contains(text(), 'Número')]/parent::tr"
        linha_estudante = driver.find_element(By.XPATH, xpath1)
        linha_descricao = driver.find_element(By.XPATH, xpath2)

        # Extrair dados adicionais da linha de estudante (tr)
        dados_colunas1 = linha_estudante.find_elements(By.TAG_NAME, "td")
        for coluna in dados_colunas1:
            texto_coluna = coluna.text
          
            dados.append(texto_coluna)
        encontrado = True

        # Extrair dados adicionais da linha da descricao (tr)
        dados_colunas2 = linha_descricao.find_elements(By.TAG_NAME, "th")
        for coluna in dados_colunas2:
            texto_coluna = coluna.text
           
            detalhes.append(texto_coluna)
        encontrado = True

        return encontrado, dados, detalhes
    except NoSuchElementException:
        encontrado = False
        return encontrado, dados, detalhes
    

    


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

    encontrado, dados, detalhes = encontrar(nr)
    retorno = []
    if(encontrado):
        print("aluno encontrado")
        for i in range(0, len(dados)):
            line = detalhes[i], ': ', dados[i]
            retorno.append(line)
    else:
        print("aluno nao encontrado")

    return retorno




