import tkinter as tk
import pyautogui

class Window():
    def __init__(self):
        self.win = tk.Tk()
        self.w, self.h = 263, 337
        self.win.title('auto clicker')
        self.win.geometry(f'{self.w}x{self.h}')
        self.win.resizable(width=False, height=False)
        self.win['bg'] = '#aaa'

        self.nonstop = True
        self.times = 100
        self.count = 0
        self.but_val = 1
        self.mouse_btn = 'left'
        self.cd = 1

        self.repeat_val = tk.IntVar()
        self.repeat_val.set(1)
        self.cooldown = tk.Entry(self.win, width=round(self.w*0.019), justify=tk.CENTER, font=('Regular', 14),
                                 validate='all', validatecommand=(self.win.register(lambda num: self.isfloat(num) or num==''), '%P'))
        self.cooldown.insert(0, '1')
        self.second = tk.Label(self.win, text='Click interval\n(Second):', bg='#a5a5a5', font=('Regular', 8, 'bold'))
        self.mouse_pos = tk.Label(self.win, text='X: 0\nY: 0', bg='#a5a5a5', font=('Regular', 18, 'bold'),
                                  padx=7, justify=tk.LEFT, anchor='w', width=round(self.w*0.0187))
        self.mouse_but_text = tk.Label(self.win, text='Mouse button:', bg='#a5a5a5', font=('Regular', 8, 'bold'))
        self.mouse_but_val = tk.StringVar(self.win, value='left')
        self.mouse_but = tk.OptionMenu(self.win, self.mouse_but_val, *['left', 'middle', 'right'])
        self.repeat_s = tk.Radiobutton(self.win, text='Repeat until stopped', variable=self.repeat_val, value=1)
        self.repeat_c = tk.Radiobutton(self.win, width=round(self.w*0.0225), text='Repeat', variable=self.repeat_val, value=2)
        self.repeat_ct = tk.Entry(self.win, width=round(self.w*0.0228), justify=tk.CENTER, font=('Regular',13),
                                  validate='all', validatecommand=(self.win.register(lambda num: num.isdigit() or num == ''), '%P'))
        self.repeat_ct.insert(0, '10')
        self.start = tk.Button(self.win, text='Start (Shift+S)', bg='white',
                               font=('Regular', 25, 'bold'), command=self.btn)
        self.stop = tk.Button(self.win, state=tk.DISABLED, text='Stop (Shift+S)', bg='white',
                              font=('Regular', 25, 'bold'), command=self.btn)

        self.cooldown.place(x=self.w*0.75, y=self.h*0.0215)
        self.second.place(x=self.w*0.4375, y=self.h*0.022)
        self.mouse_but_text.place(x=self.w*0.021, y=self.h*0.02)
        self.mouse_but.place(x=self.w*0.021, y=self.h*0.12)
        self.repeat_s.place(x=self.w*0.021, y=self.h*0.255)
        self.repeat_c.place(x=self.w*0.021, y=self.h*0.38)
        self.repeat_ct.place(x=self.w*0.325, y=self.h*0.38)
        self.mouse_pos.place(x=self.w*0.62, y=self.h*0.255)
        self.start.place(x=self.w*0.021, y=self.h*0.56)
        self.stop.place(x=self.w*0.021, y=self.h*0.78)
        self.win.bind('<Key>', lambda val: self.btn() if val.keysym=='S' else None)

        self.change_coord()

    def change_coord(self):
        pos = list(pyautogui.position())
        pos = pos[0]+1,pyautogui.size()[1]-pos[1]
        x,y = pos
        self.mouse_pos['text'] = f'X: {x}\nY: {y}'
        self.win.after(30, self.change_coord)

    def click(self):
        if self.times != self.count and self.nonstop:
            print(self.count, end=' ')
            pyautogui.click(button=self.mouse_btn)
            self.win.after(round(float(self.cooldown.get())*1000), self.click)
            self.count+=1
        else:
            self.start['state'], self.stop['state'] = tk.NORMAL, tk.DISABLED
            self.but_val = 1
            self.nonstop = False
            self.count = 0
            self.times = -1
            return

    def btn(self):
        if self.but_val == 1:
            self.start['state'], self.stop['state'] = tk.DISABLED, tk.NORMAL
            self.but_val = 2
            self.times = -1 if self.repeat_val.get() == 1 else int(self.repeat_ct.get())
            self.nonstop = True
            self.mouse_btn = self.mouse_but_val.get()
            self.cd = round(float(self.cooldown.get())*1000)
            print('\n%i' % self.times)
            self.click()
        elif self.but_val == 2:
            self.start['state'], self.stop['state'] = tk.NORMAL, tk.DISABLED
            self.but_val = 1
            self.nonstop = False
            self.count = 0
            self.times = -1

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
def main():
    win = Window()
    win.win.mainloop()

if __name__ == '__main__':
    main()
