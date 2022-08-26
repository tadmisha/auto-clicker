import tkinter as tk
import pyautogui

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
class Window():
    def __init__(self):
        self.win = tk.Tk()
        self.w, self.h = 400, 400
        self.win.title('auto clicker')
        self.win.geometry(f'{self.w}x{self.h}')
        self.win.resizable(width=False, height=False)
        self.win['bg'] = '#aaa'

        self.repeat_val = tk.IntVar()
        self.repeat_val.set(1)
        self.cooldown = tk.Entry(self.win, text='1', width=round(self.w*0.018), justify=tk.CENTER, font=('Regular', 10),
                                 validate='all', validatecommand=(self.win.register(lambda num: isfloat(num) or num==''), '%P'))
        self.cooldown.insert(0, '1')
        self.second = tk.Label(self.win, text='Click interval\n(Second):', bg='#a5a5a5', font=('Regular', 9))
        self.mouse_pos = tk.Label(self.win, text='X: 0\nY: 0', bg='#a5a5a5', font=('Regular', 17, 'bold'),
                                  padx=7, justify=tk.LEFT, anchor='w', width=round(self.w*0.0187))
        self.mouse_click = tk.OptionMenu(self.win, tk.StringVar(self.win, value='Mouse button'), *['left', 'center', 'right'])
        self.repeat_c = tk.Radiobutton(self.win, text='Repeat', variable=self.repeat_val, value=1)
        self.repeat_s = tk.Radiobutton(self.win, text='Repeat until stopped', variable=self.repeat_val, value=2)
        self.repeat_ct = tk.Entry(self.win, text='1', width=round(self.w*0.018), justify=tk.CENTER, font=('Regular',13),
                                  validate='all', validatecommand=(self.win.register(lambda num: isfloat(num)), '%P'))
        self.start = tk.Button(self.win, text='Start (Shift+S)', bg='white',
                               font=('Regular', 25, 'bold'))
        self.stop = tk.Button(self.win, text='Stop (Shift+S)', bg='white',
                              font=('Regular', 25, 'bold'))

        self.cooldown.place(x=self.w*0.765, y=self.h*0.0325)
        self.second.place(x=self.w*0.48, y=self.h*0.01)
        self.mouse_click.place(x=self.w*0.021, y=self.h*0.01)
        self.repeat_c.place(x=self.w*0.021, y=self.h*0.175)
        self.repeat_ct.place(x=self.w*0.25, y=self.h*0.175)
        self.repeat_s.place(x=self.w*0.021, y=self.h*0.3)
        self.mouse_pos.place(x=self.w*0.5575, y=self.h*0.175)
        self.start.place(x=self.w*0.021, y=self.h*0.4375)
        self.stop.place(x=self.w*0.021, y=self.h*0.725)

        self.change_coord()


    def change_coord(self):
        pos = list(pyautogui.position())
        pos = pos[0]+1,pyautogui.size()[1]-pos[1]
        x,y = pos
        self.mouse_pos['text'] = f'X: {x}\nY: {y}'
        self.win.after(30, self.change_coord)

    def click(self, x, y):
        print(x,y)

def main():
    win = Window()
    win.win.mainloop()

if __name__ == '__main__':
    main()