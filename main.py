import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import asksaveasfile

import configparser
import os



if __name__ == "__main__":
    config = configparser.ConfigParser()                                     
    config.read('config.ini')
    if config['BASE']['SAVE_GAME_PATH'] == 'PATH':
        try:
            os.makedirs('Saved_Games')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        config.set('BASE', 'save_game_path', os.getcwd())
            
def Save_Game():
    #Copy save from noita path
    #Save save files to 'SAVE_GAME_PATH'
    return()
    
def Load_Game():
    #Copy save from 'SAVE_GAME_PATH
    return()

def Set_game_path():
    filename = askdirectory()
    config.set(section, 'Saved', filename)
    
def Set_game_save_path():
    filename = askdirectory()
    
root = tk.Tk()

save_selection = tk.IntVar()

canvas1 = tk.Canvas(root, width = 400, height = 300)

save_1 = tk.Radiobutton(root, 
                        text="Save 1",
                        indicatoron = 0,
                        width = 20,
                        padx = 20, 
                        variable=save_selection, 
                        value=1).pack(anchor=tk.W)
save_2 = tk.Radiobutton(root, 
                        text="Save 2",
                        indicatoron = 0,
                        width = 20,
                        padx = 20, 
                        variable=save_selection, 
                        value=2).pack(anchor=tk.W)
save_3 = tk.Radiobutton(root, 
                        text="Save 3",
                        indicatoron = 0,
                        width = 20,
                        padx = 20, 
                        variable=save_selection, 
                        value=3).pack(anchor=tk.W)

Save_Button = tk.Button(root, text='Save Game', command=Save_Game)
Load_Button = tk.Button(root, text='Load Game', command=Load_Game)

canvas1.create_window(200, 50, window=Save_Button)
canvas1.create_window(200, 100, window=Load_Button)


canvas1.pack()






#canvas1.create_window(200, 140)#, window=entry1)

#canvas1.create_window(200, 50, window=button1)



root.mainloop()