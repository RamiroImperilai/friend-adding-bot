from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import pyautogui
from bs4 import BeautifulSoup
import time
import pyautogui

import nltk
nltk.download('names')
import gender_guesser.detector as gender
from selenium.webdriver.common.action_chains import ActionChains

# Configuración para abrir una ventana de Chrome en modo incógnito
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Inicializar el controlador del navegador
driver = webdriver.Chrome(options=chrome_options)

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir Facebook
driver.get('https://www.fb.com/')

# Esperar 3 segundos
time.sleep(3)

# Buscar el campo de correo electrónico y escribir en él
email_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
email_input.send_keys('username')

# Buscar el campo de contraseña y escribir en él
password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]')
password_field.send_keys('password')

# Hacer clic en el botón de inicio de sesión
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()

# Esperar 3 segundos
time.sleep(3)

# Redirigir a la página de sugerencias de amigos después de iniciar sesión
driver.get('https://www.facebook.com/friends/suggestions')

# Esperar 3 segundos
time.sleep(3)

# hacer clic en la posición (x, y)
pyautogui.click(350, 650)

# Esperar 3 segundos
time.sleep(3)

# Obtener el contenido HTML de la página actual
html = driver.page_source

# Crear objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html, 'html.parser')

bloques = soup.find_all('span', {'class': 'x193iq5w'})

combinaciones_impresas = set()

d = gender.Detector()
actions = ActionChains(driver)

nombres_agregados = []
lista = driver.find_element(By.XPATH, "//div[contains(@class, 'x2bj2ny') and contains (@class, 'x1afcbsf')]")
actions.move_to_element(lista)


SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight", lista)
scroll = 0
while scroll < 15:
    # Scroll down to bottom
    actions.send_keys(Keys.PAGE_DOWN).perform()
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    scroll +=1

    

#bloques = soup.find_all('span', {'class': 'x193iq5w'})
bloques = driver.find_elements(By.XPATH, "//div[contains(@class, 'x193iq5w')]")# and contains (@class, 'x1q0q8m5') and contains (@class, 'x1qhh985') and contains (@class, 'xu3j5b3') and contains (@class, 'xcfux6l') and contains (@class, 'x26u7qi')]")

for bloque in bloques:

    try:
        boton_agregar = bloque.find_element(By.XPATH, ".//*[contains(text(), 'Agregar')]")
        #actions.scroll_to_element(boton_agregar).perform()
        # Hacer clic en el botón
        boton_agregar.click()
        print("se agrego")
        time.sleep(3) # Esperar 3 segundos
    except:
        pass

driver.quit()
