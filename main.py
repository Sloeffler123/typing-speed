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

# def clear_text(event):
#     if user_type.get() == 'Type text here':
#         user_type.delete(0, tkinter.END)

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
# user_type.insert(index=0, string='Type text here')
# user_type.bind('<FocusIn>', clear_text)

def compare():
    user_text = user_type.get()
    text_diplay_lst = text_diplay.get('1.0', tkinter.END).lstrip('\n')
    # print(user_text)
    line = 1
    char = 0
    for i in range(len(user_text)):
        if text_diplay_lst[i] == '\n':
            line += 1
            char += 1
        if text_diplay_lst[i] == user_text[i]:
            text_diplay.tag_add('highlight_green', f'{line}.{char}', f'{line}.{char + 1}')
            text_diplay.tag_config(tagName='highlight_green', foreground='green')
        elif text_diplay_lst[i] != user_text[i]:
            text_diplay.tag_add('highlight_red', f'{line}.{char}', f'{line}.{char + 1}')   
            text_diplay.tag_config(tagName='highlight_red', foreground='red') 
        char += 1    
    window.after(1000, compare)        
# # maybe use yield so progress starts back where it ended

compare()
stop_watch()
window.mainloop()