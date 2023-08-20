import pyautogui as pg
import time


print("program will run after 5 second")
time.sleep(5)
print("running")

for i in range(5):
    pg.write("Hii.")
    time.sleep(0.5)
    # Sending the messages by pressing enter
    pg.press("Enter")