# pygame - cProfile - > pProfile
from cProfile import label
import tkinter as tk
import fnmatch
import os
from pygame import mixer
import pygame

canvas = tk.Tk()

# Create a Music canvas
canvas.title("Music")
canvas.geometry("600x800")
canvas.config(bg = 'black')


# Sets the rootpath for the ditosimone.
rootpath = "/Users/divitosimone/Desktop/Symphony_X"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file="prev_img.png")
pause_img = tk.PhotoImage(file="pause_img.png")
next_img = tk.PhotoImage(file="next_img.png")
play_img = tk.PhotoImage(file="play_img.png")
stop_img = tk.PhotoImage(file="stop_img.png")

# Play the music.
def play():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "//" + listBox.get("anchor"))
    mixer.music.play()
    

# Stop the music.
def stop():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "//" + listBox.get("anchor"))
    mixer.music.stop()
    
    # Load the next song from the list box.
def next():
     next_song = listBox.curselection() # The next song in the list box
     next_song = next_song[0] + 1
     next_song_name = listBox.get(next_song)
     label.config(text = next_song_name) # Creates a label for the next song.
     mixer.music.load(rootpath + "//" + next_song_name)
     mixer.music.play()
     listBox.select_clear(0,'end') # Clears the end of the list box
     listBox.activate(next_song) # Activate the next song.
     listBox.select_set(next_song)  # Select the next song in the list box
     

# Show the previous song.
def prev():
     prev_song = listBox.curselection()
     prev_song = prev_song[0] - 1
     prev_song_name = listBox.get(prev_song)
     label.config(text = prev_song_name)
     mixer.music.load(rootpath + "//" + prev_song_name)
     mixer.music.play()
     listBox.select_clear(0,'end')
     listBox.activate(prev_song)
     listBox.select_set(prev_song)


# Pause the music.
def pause():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"


# Create a tk. Listbox
listBox = tk.Listbox(canvas, fg= "cyan", bg = "black", width=100,font=('poppins',14))
listBox.pack(padx = 15, pady = 15)

# Create a poppin label.

label = tk.Label(canvas,'',bg = 'black', fg='yellow', font=('poppin',14))
label.pack(pady=15)

# Create a tk. Frame from a canvas.

top = tk.Frame(canvas, bg = 'black',highlightthickness=0)
top.pack(padx = 10, pady= 5, anchor= 'center')

# Add a prev button
prevButton = tk.Button(canvas, text = 'prev', image = prev_img, bg = 'black', borderwidth = 0,command = prev)
prevButton.pack(pady=15, in_= top, side= 'left')


# Create a pause button
pauseButton = tk.Button(canvas, text =  "pause",image = pause_img, bg = 'black', borderwidth = 0, command = pause)
pauseButton.pack(pady=15,in_= top, side= 'left')

# Creates a button for the next command
nextButton = tk.Button(canvas, text =  "next",image = next_img, bg = 'black', borderwidth = 0, command = next)
nextButton.pack(pady=15,in_= top, side= 'left')

# Create a play button
playButton = tk.Button(canvas, text =  "play",image = play_img, bg = 'black', borderwidth = 0, command = play)
playButton.pack(pady=15,in_= top, side= 'left')

# Creates a stop button
stopButton = tk.Button(canvas, text =  "stop",image = stop_img, bg = 'black', borderwidth = 0, command = stop)
stopButton.pack(pady=15,in_= top, side= 'left')



# recursively walk a directory tree and create a list box for each file.
for root, dirs, files in os.walk(rootpath):
    
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end',filename)
        


# mainloop.
canvas.mainloop()


# Definitions:


# fnmatch.filter(names, pattern)
# Construct a list from those elements of the iterable names that match pattern. 
# It is the same as [n for n in names if fnmatch(n, pattern)], but implemented more efficiently.


# Frame is very important for the process of grouping and organizing other widgets in a somehow friendly way.
# It works like a container, which is responsible for arranging the position of other widgets.
# It uses rectangular areas in the screen to organize the layout and to provide padding of these widgets.
# A frame can also be used as a foundation class to implement complex widgets.

# Label implements a display box where you can place text or images.
# The text displayed by this widget can be updated at any time you want.

#Listbox widget is used to display a list of items from which a user can select a number of items.