import sqlite3
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
sql = 'INSERT INTO noticias (categoria, titulo, data, descricao) VALUES (?, ?, ?, ?)'

navegador = Chrome(service=Service(ChromeDriverManager().install()))
navegador.get('https://raspagem.herokuapp.com/noticias/')

elementos = navegador.find_elements(By.XPATH, "//a[contains(@href, '/noticias/secoes')]")

for i in elementos:
    i.click()
    time.sleep(3)
    for noticia in navegador.find_elements(By.CSS_SELECTOR, 'div.position-relative'):
        categoria = noticia.find_element(By.CSS_SELECTOR, 'strong.text-primary').text
        titulo = noticia.find_element(By.TAG_NAME, 'h3').text
        data = noticia.find_element(By.CSS_SELECTOR, 'div.text-muted').text
        descricao = noticia.find_element(By.TAG_NAME, 'p').text
        valores = [categoria, titulo, data, descricao]
        cursor.execute(sql, valores)
    navegador.back()

navegador.close()
conexao.commit()
conexao.close()

