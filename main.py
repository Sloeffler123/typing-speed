import tkinter
import time
TIMER = 60

# def stop_watch():
#     global TIMER
#     TIMER -= 1
#     time.sleep(1)
#     print(TIMER)
#     return TIMER
    # window.after()
def words_per_minute():
    pass

def generate_words():
    with open('text.txt', 'r') as file:
        pass

def clear_text(event):
    if user_type.get() == 'Type text here':
        user_type.delete(0, tkinter.END)

window = tkinter.Tk()
window.geometry('1000x800')

wpm_text = tkinter.Label(text=f'WPM:')
wpm_text.grid(column=0, row=0, sticky='EW')

time_text = tkinter.Label(text='Time:')
time_text.grid(column=1, row=0, sticky='EW')

restart_button = tkinter.Button(text='Restart')
restart_button.grid(column=2, row=0, sticky='EW')

#text display



# user input 
user_type = tkinter.Entry(width=40)
user_type.grid(column=1,row=1)
user_type.insert(index=0, string='Type text here')
user_type.bind('<FocusIn>', clear_text)


window.mainloop()