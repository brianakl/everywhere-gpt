from openai import OpenAI
from pynput import keyboard

client = OpenAI()
kb = keyboard.Controller()
recording = False

# default key to toggle key recording and stop key tracking to send api request
TOGGLE = keyboard.Key.f9
# TOGGLE = keyboard.Key.esc
ERASE = keyboard.Key.f2 # default erase button for when key recording is enabled
MAX_TOKENS = 800        # max tokens to generate for openai
TEMP = 0.6
MAX_QUERY_LEN = 1000    # max query len to send 

def press_keys(txt):
    kb.press(keyboard.Key.enter)
    kb.release(keyboard.Key.enter)
    for c in txt:
        kb.press(c)
        kb.release(c)


def openai_call(prompt: str):

    response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system", 
                    "content": "Please predict most accurately what the next words should be."
                 },
                {
                    "role": "user", 
                    "content":prompt
                 }
                ],
            max_tokens=MAX_TOKENS,
            temperature=TEMP,
            )

    press_keys(response.choices[0].message.content)
    


# The event listener will be running in this block
msg = ''
def on_press(key):
    global recording
    if not recording:
        return

    global msg, KEY

    try:
        msg += key.char
        if len(msg) >= MAX_QUERY_LEN:
            msg = msg[1:]
    except AttributeError:
        if key == keyboard.Key.space:
            msg += ' '
        elif key == keyboard.Key.enter:
            msg += '\n'
        elif key == keyboard.Key.backspace:
            msg = msg[:-1]
        # erase current msg
        elif key == ERASE:
            msg = ''


def on_release(key):
    global recording
    if key == TOGGLE:
        if recording:
            openai_call(msg)
            recording = False
        else:
            recording = True
        return False

# Collect events until released
while True:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    msg=''
    
