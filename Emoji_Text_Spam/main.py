import pyautogui
import time

print("Copy text or emoji to clipboard")

while True:
	selection = input("Have you copied yet(Y/n)")
	if selection == "y" or selection == "Y":
		break;
	time.sleep(5)
	
while True:
    try:
        count = int(input("Enter the amount of times you would like to spam: "))
        if count >= 1:
            break
        else:
            print("You can't spam 0 or less than that, try again")
            continue
    except ValueError:
        print("Not an integer, try again")
        continue

print("Put cursor where you would like to spam. You have 5 seconds")
time.sleep(5)
for i in range(count):
	pyautogui.hotkey("ctrl", "v")
	pyautogui.press("enter")

print("Spammed Successfully")
