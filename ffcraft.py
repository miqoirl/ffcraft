from pyautogui import *
import pyautogui
import random
import time

macro_button = "q"
fail_count = 0
synth_path = 'images/synth_button.png'
CONFIDENCE = 0.95

def click(x_loc,y_loc):
    pyautogui.click(clicks=2, interval=0.25, x=x_loc, y=y_loc)

def synthesize(position):
  global fail_count
  time.sleep(1)
  click(position[0], position[1]) # Click synthesize button
  time.sleep(random.randint(2,3))
  if not find_synth():
    fail_count = 0 # Reset fail count
    t = time.localtime()
    print('[{}] Synthesizing...'.format(time.strftime("%H:%M:%S", t)))
    pyautogui.press(macro_button) # Start macro
  else:
    fail_count +=1

# Check if synthesis button is on screen
def find_synth():
  synth_button_pos = pyautogui.locateOnScreen(synth_path, confidence=CONFIDENCE)
  return False if synth_button_pos is None else True

# Ends script when synthesis fails 10 times
while fail_count < 3:
  try:
    synth_button_pos = pyautogui.locateOnScreen(synth_path, confidence=CONFIDENCE)
    synth_button = pyautogui.center(synth_button_pos)
    
    synthesize(synth_button)
  except TypeError: # Synthesize button not found on screen
    time.sleep(2)

print("Fail limit exceeded, ending script.")