import tkinter
TIMER = 60

def stop_watch():
    global TIMER
    TIMER -= 1
    time_text.config(text=f'Time left: {TIMER}')
    window.after(1000, stop_watch)
def words_per_minute():
    pass

def generate_words():
    with open('text.txt', 'r') as file:
        words = file.read()
        return words

def clear_text(event):
    if user_type.get() == 'Type text here':
        user_type.delete(0, tkinter.END)

def compare_text():
    pass

window = tkinter.Tk()

wpm_text = tkinter.Label(text=f'WPM: 0')
wpm_text.grid(column=0, row=0, sticky='EW')

time_text = tkinter.Label(text='Time left: 60')
time_text.grid(column=1, row=0, sticky='EW')

restart_button = tkinter.Button(text='Restart')
restart_button.grid(column=2, row=0, sticky='EW')

#text display
text_diplay = tkinter.Text()
text_diplay.insert(tkinter.END, generate_words())
text_diplay.config(state='disabled')
text_diplay.grid(columnspan=3, row=1)

# user input 
user_type = tkinter.Entry(width=40)
user_type.grid(column=1,row=2)
user_type.insert(index=0, string='Type text here')
user_type.bind('<FocusIn>', clear_text)

def compare():
    print('hello')
    user_text = user_type.get()
    text_diplay_lst = text_diplay.get('1.0', tkinter.END).strip('\n')
    print(user_text)
    for i in range(len(user_text)):
        if text_diplay_lst[i] == user_text[i]:
            text_diplay.tag_add('highlight', f'')
    window.after(2000, compare)        
# maybe use yield so progress starts back where it ended

compare()
stop_watch()


window.mainloop()