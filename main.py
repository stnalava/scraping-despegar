from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from MONGO import MongoConnection
db_client = MongoConnection().client
db = db_client.get_database('masmusika')
col = db.get_collection('guitar')


driver = webdriver.Chrome()
driver.get("https://masmusika.com/categoria/instrumentos-musicales/")
guitar = driver.find_elements(By.CLASS_NAME, "product-inner")

for f in guitar:
    descr = f.find_element(by=By.CLASS_NAME, value="product-loop-title").text
    price = f.find_element(by=By.CLASS_NAME, value="price").text
    button = f.find_element(by=By.CLASS_NAME, value="add-links-wrap").text  # boton de comprar

    document = {
        "descr": descr,
        "price": price,
        "button": button,
    }

    col.insert_one(document=document)

    print(descr)
    print(price)
    print(button)
    print('=' * 40)
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
driver.close()