This script automates crafting in FF14. Currently, only single macro crafts are supported.

### Set up

1. Download and install Python - https://www.python.org/downloads/
    - Remember to select the checkbox "Add Python x.x to PATH"
3. Open Command Prompt as administrator
4. Install required packages
    - pip install pyautogui
    - pip install "opencv-python-headless<4.3"
5. Replace synth_button.png in images/ folder with your own
6. Open ffcraft.py in a text editor and replace this line:
    - macro_button = "q"
        - replace "q" with whichever macro button you use

### Usage

In Command Prompt
1. Navigate to folder:
    - cd <path_to_folder> 
        - for example: `cd C:\Users\username\Downloads\ffcraft`
2. Open crafting page in game so that the 'Synthesize' button is seen
3. Run:
    - python ffcraft.py
