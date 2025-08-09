import pyautogui
import time

print("🔁 Within 5 seconds, move your mouse over the captcha box...")
time.sleep(5)

# collect mouse POSITION
x, y = pyautogui.position()
color = pyautogui.screenshot().getpixel((x, y))

print(f"📍 Current coordinates: ({x}, {y})")
print(f"🎨 Color under the cursor: {color}")
