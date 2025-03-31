from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

def get_qb_stats(driver, week):
    """Extrae las estadísticas de QBs para un año específico."""
    web = f'https://www.footballdb.com/fantasy-football/index.html?yr=2024&pos=QB&wk={week}&key=b6406b7aea3872d5bb677f064673c57f'
    driver.get(web)

    # Esperar a que cargue la página
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Buscar la tabla por su clase
    table = driver.find_element(By.CLASS_NAME, "statistics")

    # Extraer las filas de la tabla
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Extraer datos de cada celda
    data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")  # Buscar columnas normales
        if not cells:
            cells = row.find_elements(By.TAG_NAME, "th")  # Si es encabezado, buscar th
        data.append([cell.text for cell in cells])

    # Guardar en un archivo CSV
    csv_filename = f"data/qb_fantasy_week_{week}.csv"
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"✅ Datos guardados en '{csv_filename}'")

# Configurar Selenium (iniciar el navegador una sola vez)
path = 'D:/Sam Contreras/Documents/Programacion/Python/ChromeDriver/chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

try:
    for week in range(1, 18):
        get_qb_stats(driver, week)
        time.sleep(3)  # Espera entre peticiones para evitar bloqueos del sitio

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()  # Cerrar el navegador al final
    print("Scraping finalizado.")