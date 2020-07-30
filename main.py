import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

import configparser
import os
import errno
import sys
import shutil
import subprocess


def Set_game_path(): #Sets noita's game file
    filename = askopenfilename()
    config.set('BASE', 'noita_path', filename)
    with open("config.ini", "w+") as configfile:
        config.write(configfile)
    Game_Path_Button.destroy()
    return()
    
def Set_game_save_path(): #Sets noita's save file i.e. save00
    filename = askdirectory()
    config.set('BASE', 'noita_save_path', filename)
    with open("config.ini", "w+") as configfile:
        config.write(configfile)
    Game_Save_Path_Button.destroy()
    return()

def Save_Game(): #Save button function
    MsgBox = tk.messagebox.askquestion ('Overwrite Save','Are you sure you want to save over this slot?',icon = 'warning')
    if MsgBox == 'yes':
        try: shutil.rmtree(str(config['BASE']['SAVE_GAME_PATH'])+'\\'+ str(save_selection.get()) + '\\save00')
        except: return()
        finally: shutil.copytree(config['BASE']['noita_save_path'], 
                    str(config['BASE']['SAVE_GAME_PATH'])+'\\'+ str(save_selection.get()) + '\\save00')
        return()
    else:
        return()

def Load_Game(): #Load button function
    try: shutil.rmtree(config['BASE']['noita_save_path'])
    except: return()
    finally: shutil.copytree(str(config['BASE']['SAVE_GAME_PATH'])+'\\'+ str(save_selection.get()) + '\\save00', 
                    config['BASE']['noita_save_path'])
    #subprocess.call(config['BASE']['NOITA_PATH']) #Bugged
    return()

def Do_Nothing(): #Testing Function
    return()

def on_closing(): #Prevents python from crashing
    root.destroy()
    sys.exit()

def UI(): #Main UI function
    root = tk.Tk()
    root.title("Noita Save Manager")
    root.iconbitmap('icon.ico')
    ### Dynamically Changes the radiobutton name based on if the save slot is filled
    # def Check_Save():
    #     if config['SAVED_GAMES']['save1'] == 'False': save_button_1['text'] = 'Empty Slot'
    #     if config['SAVED_GAMES']['save2'] == 'False': savegame_2 = 'Empty Slot'
    #     if config['SAVED_GAMES']['save3'] == 'False': savegame_3 = 'Empty Slot'
    #     root.after(500, Check_Save)
    #root.after(500, Check_Save)
    ###
    global save_selection
    save_selection = tk.IntVar()
    save_selection.set(1)
    
    canvas1 = tk.Canvas(root, width = 100, height = 100)

    save_button_1 = tk.Radiobutton(root, 
                    text= 'Slot 1',
                    indicatoron = 0,
                    width = 20,
                    padx = 20, 
                    variable=save_selection, 
                    value=1).pack(anchor=tk.W)
    save_button_2 = tk.Radiobutton(root, 
                    text= 'Slot 2',
                    indicatoron = 0,
                    width = 20,
                    padx = 20, 
                    variable=save_selection, 
                    value=2).pack(anchor=tk.W)
    save_button_3 = tk.Radiobutton(root, 
                    text= 'Slot 3',
                    indicatoron = 0,
                    width = 20,
                    padx = 20, 
                    variable=save_selection, 
                    value=3).pack(anchor=tk.W)
    
    Save_Button = tk.Button(root, text='Save Game', command=Save_Game)
    Load_Button = tk.Button(root, text='Load Game', command=Load_Game)
    
    canvas1.create_window(50, 40, window=Save_Button)
    canvas1.create_window(50, 75, window=Load_Button)
    canvas1.pack()
    
    root.mainloop()    
    
if __name__ == "__main__": #file setup
    config = configparser.ConfigParser()                                     
    config.read('config.ini')
    
    if os.path.exists(config['BASE']['SAVE_GAME_PATH']) == False:
        try:
            os.makedirs('Saved_Games')
            os.makedirs('Saved_Games/1')
            os.makedirs('Saved_Games/2')
            os.makedirs('Saved_Games/3')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        config.set('BASE', 'SAVE_GAME_PATH', str(os.getcwd()) +'\Saved_Games')   
        with open("config.ini", "w+") as configfile:
            config.write(configfile)

    if os.path.exists(config['BASE']['NOITA_PATH']) == False or os.path.exists(config['BASE']['NOITA_SAVE_PATH']) == False:
        root = tk.Tk()
        root.title("Noita Save Manager")
        root.iconbitmap('icon.ico')
        canvas1 = tk.Canvas(root, width = 200, height = 200)
        Game_Path_Button = tk.Button(root, text='Select Noita Path', command=Set_game_path)
        Game_Save_Path_Button = tk.Button(root, text='Select Noita Save Path', command=Set_game_save_path)
        canvas1.create_window(100, 40, window=Game_Path_Button)
        canvas1.create_window(100, 75, window=Game_Save_Path_Button)
        canvas1.pack()
        root.protocol("WM_DELETE_WINDOW", on_closing)
        def check_path(): 
            if (os.path.isfile(config['BASE']['NOITA_PATH']) == False or os.path.exists(config['BASE']['NOITA_SAVE_PATH']) == False):
                root.after(500, check_path)
            else: root.destroy()  
        root.after(500, check_path)
        root.mainloop()
        
    UI()