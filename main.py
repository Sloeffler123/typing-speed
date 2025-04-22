import tkinter
import random
import sys
TIMER = 30

def stop_watch():
    global TIMER
    TIMER -= 1
    time_text.config(text=f'Time left: {TIMER}')
    window.after(1000, stop_watch)
def words_per_minute(red_chars):

    total = len(user_type.get()) // 5 - len(red_chars)
    wpm_text.config(text=f'WPM: {total}')
    
def generate_words():
    with open('text.txt', 'r') as file:
        words = file.read().splitlines()
        return random.choice(words)

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
    text_diplay_lst = text_diplay.get('1.0', tkinter.END)
    line = 1
    char = 0

    text_diplay.tag_config(tagName='highlight_red', foreground='red')
    text_diplay.tag_config(tagName='highlight_green', foreground='green')
    text_diplay.tag_config(tagName='highlight_black', foreground='black')

    text_diplay.tag_remove(tagName='highlight_red', index1='1.0', index2=tkinter.END)
    text_diplay.tag_remove(tagName='highlight_green', index1='1.0', index2=tkinter.END)
    text_diplay.tag_remove(tagName='highlight_black', index1='1.0', index2=tkinter.END)
    red_char = []
    for i in range(len(user_text)):
        if text_diplay_lst[i] == '\n':
            line += 1
            char = 0
        if text_diplay_lst[i] == user_text[i]:
            text_diplay.tag_add('highlight_green', f'{line}.{char}', f'{line}.{char + 1}')
        elif text_diplay_lst[i] != user_text[i]:  
            text_diplay.tag_add('highlight_red', f'{line}.{char}', f'{line}.{char + 1}') 
            red_char.append('i')
        char += 1  
    print(len(red_char))      
    text_diplay.tag_add('highlight_black', f'{line}.{len(user_text) + 1}', tkinter.END)
    words_per_minute(red_char)  
    window.after(100, compare)   
        
# # maybe use yield so progress starts back where it ended
# text_diplay.tag_add('highlight_black', f'{line}.{len(user_text)}', tkinter.END)

def main():
    compare()
    stop_watch()
    window.mainloop()

main()