import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# List of employees to add



employees = [
    {"firstName": "Veda","lastName":"Patil","Employee Id":1234},
    {"firstName": "Kiran","lastName":"Raj","Employee Id":12345},
    {"firstName": "Manita","lastName":"Rao","Employee Id":12346},
    {"firstName": "Raki","lastName":"Bai","Employee Id":12347}
]

# Initialize the WebDriver
driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# --- LOGIN ---
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# --- NAVIGATE TO PIM ---
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))).click()


# --- ADD EMPLOYEES ---

for emp in employees:
    firstName=emp["firstName"]
    lastName=emp["lastName"]
    EmployeeId=emp["Employee Id"]

    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a"))).click()
    time.sleep(10)

    wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys(emp["firstName"])
    driver.find_element(By.NAME, "lastName").send_keys(emp["lastName"])
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys(emp["Employee Id"])
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(10)  # Allow for save and return

# --- VERIFY EMPLOYEES ---
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Employee List']"))).click()
time.sleep(2)

try:
    Employee_Name = wait.until(EC.presence_of_element_located((
        By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input")))
    Employee_Name.clear()
    Employee_Name.send_keys(f"{firstName} {lastName}")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
except Exception as e:
    print("Search failed:", e)


# --- LOGOUT ---
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))).click()

# Close browser
driver.quit()
