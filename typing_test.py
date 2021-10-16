import tkinter as tk
import random
import time

root = tk.Tk()
root.title('Typing Speed Test')
root.geometry('1200x420+150+100')
root.resizable(False, False)
root.config(bg='#B5DAF9')

title_app = tk.Label(master=root, text='Typing Speed Test', bg='#B5DAF9', fg='#3e5263',
                     font=('Arial', 20, 'bold'))
title_app.pack(pady=10, anchor='center')

start_time = 0

with open('sentences.txt', encoding='utf-8') as f:
    sentences = f.read().splitlines()
    sentence = random.choice(sentences)


# function for start the timer by clicking on the field for entry
def start_input(event):
    global start_time
    text_entry.config(state='normal')
    start_time = time.time()


# reset all settings
def reset_text():
    global sentences, sentence, start_time

    # text updates
    new_text = random.choice(sentences)
    random_sentence.config(text=new_text)
    sentence = new_text

    text_entry.delete(0, tk.END)
    text_entry.config(state='disabled')
    start_time = 0

    result_time.config(text='')
    result_accuracy.config(text='')
    result_wpm.config(text='')
    info.config(text='Please input words what are seeing on the display. After entering, press "Enter" '
                     'to display your result.', font=('Arial', 14, 'bold'))
    info.place(x=112, y=290)


def result_test(event):
    total_time = time.time() - start_time

    text = input_text.get()

    # counting correctly entered symbols
    count = 0
    error = 0
    try:
        for i, s in enumerate(text):
            if sentence[i + error] == s:
                count += 1
            else:
                error += 1
    except Exception:
        print('Please try again!')

    if text == '':
        text_entry.config(state='disabled')
        info.config(text='Please,click the "Reset" button, and than double press "Left Click Mouse" on the field for '
                         'entry and input the text.')
        info.place(x=80, y=295)
    else:
        accuracy = (count / len(sentence)) * 100

        if accuracy > 10:
            wpm = (len(text) / 6) / (round(total_time) / 60)
        else:
            wpm = 0

        result_time.config(text='Time: ' + str(round(total_time)) + 'sec.')
        result_accuracy.config(text='Accuracy: ' + str(round(accuracy)) + '%')
        result_wpm.config(text='WPM: ' + str(round(wpm)))
        info.config(text='< 24wpm - slow typing speed, ' 
                         '\n24-32wpm - speed an average person, '
                         '\n32-52wpm - medium typing speed, '
                         '\n52-70wpm - good typing speed, ' 
                         '\n70-80wpm - professional level of keyboard skills (touch-typing),'
                         '\n> 80wpm - high speed what close to the speed of speech', font=('Arial', 12, 'bold'))
        info.place(x=350, y=295)


# creating app components
random_sentence = tk.Label(master=root, text=sentence, height=2,
                           bg='white', fg='black', font=('Arial', 18))
random_sentence.pack(pady=30, anchor='center')

input_text = tk.StringVar()
text_entry = tk.Entry(master=root, bg='white', fg='black', font=('Arial', 20), width=50,
                      textvariable=input_text, state='readonly')
text_entry.place(x=160, y=200)
text_entry.bind('<Double-Button-1>', start_input)

button_reset = tk.Button(master=root, text='\u2B6F', font=('Arial', 12, 'bold'), width=5, bg='#3e5263',
                         fg='white', command=reset_text)
button_reset.place(x=930, y=200)

result_time = tk.Label(master=root, bg='#B5DAF9', fg='#3e5263', font=('Arial', 14, 'underline', 'bold'))
result_time.place(x=300, y=260)

result_accuracy = tk.Label(master=root, bg='#B5DAF9', fg='#3e5263',
                           font=('Arial', 14, 'underline', 'bold'))
result_accuracy.place(x=520, y=260)

result_wpm = tk.Label(master=root, bg='#B5DAF9', fg='#3e5263',
                      font=('Arial', 14, 'underline', 'bold'))
result_wpm.place(x=770, y=260)

info = tk.Label(master=root, text='Please input words what are seeing on the display. After entering, press "Enter" '
                                  'to display your result.', bg='#B5DAF9', fg='#3e5263', font=('Arial', 14, 'bold'))
info.place(x=112, y=290)

root.bind('<Return>', result_test)

if __name__ == '__main__':
    root.mainloop()
