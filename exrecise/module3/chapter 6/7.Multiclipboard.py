import pyperclip
import shelve

def save_to_clipboard_history(text):
    with shelve.open('clipboard_history')as db:
        history = db.get('history',[])
        history.append(text)
        db['history'] = history

def show_history():
    with shelve.open('clipboard_history')as db:
        history = db.get('history',[])
        for index, item in enumerate(history):
            print(f"{index + 1}: {item}")
