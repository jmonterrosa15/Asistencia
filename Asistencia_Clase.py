from selenium import webdriver
def launchBrowser():
    #En esta función se abre Chrome como un webdriver y se almacena en browser
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
    chrome_driver_binary = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
    browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
    return browser

def main():
    #Esta es la funcion principal
    #Se inicializa el browser
    browser = launchBrowser()

    #En esta funcion se ejecutan los pasos para ingresar a la plataforma y marcar la asistencia

    #Se abre la plataforma, se hace click en Iniciar Sesión y luego en Iniciar con google
    browser.get('http://www.misiontic.uninorte.edu.co')
    browser.find_element_by_link_text('Iniciar sesión').click()
    browser.find_element_by_id('hinted-login-form').click()
    
    #Se ingresa sesión llenando correo electrónico, clave y haciendo click en los botones
    browser.find_element_by_id('identifierId').send_keys('@uninorte.edu.co')#Escribe aquí tu correo
    browser.find_element_by_id('identifierNext').click()
    browser.implicitly_wait(2)
    browser.find_element_by_name('password').send_keys('')#Escribe aquí tu contraseña
    browser.find_element_by_id('passwordNext').click()

    #Se selecciona la clase de inglés
    browser.implicitly_wait(5)
    browser.find_element_by_link_text('Ciclo 1: Basic english reading skills for programming').click()

    #Se hace click en la sesión del día. Se identifica como el último objeto de clase vertical-title
    browser.implicitly_wait(2)
    lista_links = browser.find_elements_by_class_name('vertical-title')
    lista_links[len(lista_links)-1].click()

    #Se marca el checkbox y se hace click en enviar
    try:
        browser.find_element_by_id('input_2b5c1aa9ff764926b79dbfd7e06f61bf_2_1_choice_0').click()
    except:
        while True:
            pass

    try:
        browser.find_element_by_class_name('submit-label').click()
    except:
        while True:
            pass
    
    browser.implicitly_wait(5)
    while True:
        pass

main ()