import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")







def getNotas():
    print('==BOT STARTED==')
    driver = webdriver.Chrome(options=chrome_options)
    def click(path):
        driver.find_element(By.XPATH, path).click()

    def insert(path, content):
        driver.find_element(By.XPATH, path).send_keys(content)
    
    driver.get('https://fenix.isutc.ac.mz/isutc/fenixEduIndex.do')

    driver.find_element(By.XPATH, '//*[@id="logout"]/a').click()
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('yannick.matimbe')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Y@nnick2003')
    driver.find_element(By.XPATH, '//*[@id="fm1"]/div[4]/input[4]').click()

    click('//*[@id="content"]/div/center/a[2]')
    click('//*[@id="container"]/table/tbody/tr[4]/td[1]')
    click('//*[@id="latnav"]/ul/li[5]/a')
    driver.find_element(By.LINK_TEXT, 'Inteligência Artificial').click()
    click('//*[@id="latnav"]/ul[1]/li[4]/a')
    driver.find_element(By.LINK_TEXT, 'Rendimento académico').click()

    
    tabela = driver.find_element(By.XPATH, '//*[@id="main"]/table')
    screenshot = tabela.screenshot_as_base64

    # Salve a captura de tela em um arquivo
    with open("screenshot.png", "wb") as arquivo:
        arquivo.write(base64.b64decode(screenshot))
    

    html = tabela.get_attribute('outerHTML')

    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table')

    tabela = [[]]
    for i in table.find_all('tr'):
        linha = []
        for j in i.find_all('td'):
            linha.append((j.text).strip())
        tabela.append(linha)

    
    
    return tabela


