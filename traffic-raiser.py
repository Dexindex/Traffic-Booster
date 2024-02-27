#Please Install Selenium To Run This Script.


from selenium import webdriver
import time
import subprocess
import random
def generate_random_mac():
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: f'{x:02x}', mac))
def change_mac(interface):
    new_mac = generate_random_mac()
    print(f"Changing MAC address of {interface} to {new_mac}")
    # 
    subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=disable"])

    # 
    subprocess.call(["reg", "add", f"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\{interface}\\", "/v", "NetworkAddress", "/t", "REG_SZ", "/d", new_mac, "/f"])
    # 
    subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=enable"])
original_mac = "74-46-A0-91-07-63" 
url = "https://your-website.ma/"
# 
driver = webdriver.Chrome()
#
num_visits = 8624753589854785  #


for _ in range(num_visits):
    # 
    driver.get(url)
    # 
    change_mac("Ethernet")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 
    time.sleep(4)

driver.quit()
