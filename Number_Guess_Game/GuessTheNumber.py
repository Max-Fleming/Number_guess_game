from tkinter import *
from tkinter import ttk
import random

window = Tk()
window.title('Guess The Number')
window.geometry('250x195')
window.iconbitmap('image.ico')

answer = 0
count = 0
feedback = StringVar()
guess = StringVar()
counter = StringVar()


def reset_game():
    """The purpose of this function is to initialize all data for the game resetting all variables. """
    global answer, count, feedback, guess, counter
    guess.set('')
    answer = random.randint(1, 10)
    feedback.set('Enter Guess 1')
    count = 0
    counter.set(f'Guess {count} / 4')
    submit_button['state'] = NORMAL
    progress['value'] = 0


def check_answer():
    """The purpose of this function is to check weather or not the user has entered the correct answer"""
    global answer, count, feedback, guess, counter
    count += 1
    counter.set(f'Guess {count} / 4')
    progress.step(100)

    try:
        g = int(guess.get())
    except (AttributeError, ValueError):
        g = 0
        guess.set('0')

    if g == answer:
        feedback.set(f'{g} was correct! You win!')
        submit_button.config(state=DISABLED)
    elif g > answer:
        feedback.set(f'{g} was too high')
    else:
        feedback.set(f'{g} was too low')

    guess.set('')
    guess_textBox.focus()

    if count == 4:
        feedback.set(f'Answer was {answer}. Nice try!')
        submit_button['state'] = DISABLED


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Reset', command=reset_game)
file_menu.add_command(label='Exit', command=window.quit)

feedback_label = Label(window, textvariable=feedback, justify=LEFT)
feedback_label.pack()

guess_textBox = Entry(window, textvariable=guess, justify=CENTER)
guess_textBox.pack(pady=5)

progress = ttk.Progressbar(window, orient='horizontal', length='124', maximum=401, mode='determinate')
progress.pack(pady=20)

counter_label = Label(window, textvariable=counter, justify=CENTER)
counter_label.pack()

submit_button = Button(window, text='Submit', command=check_answer)
submit_button.pack()

reset_game()
window.mainloop()
