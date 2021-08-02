from tkinter import Tk,Label,Canvas,Button,Frame,PhotoImage
from tkinter import colorchooser
from tkinter import filedialog as fd
import mediapipe as mp
import cv2

import numpy as np
from math import sqrt

import PIL.Image, PIL.ImageTk

mpDraw =  mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hands   = mpHands.Hands(max_num_hands=1)

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Virtual Painter')
        
        self.isrunning = False
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight() - 100
        
        self.canvas_img = np.ones((self.height,self.width,3),dtype=np.int8) * 255
        self.color = (0,0,0)
        self.mcolor = (0,0,0)
        self.xp = self.yp = ''
        self.thickness = 5
        self.drawhand = False

        # * Top Label
        l1 = Label(self,borderwidth=2, relief="solid")
        l1.pack(fill='x',expand=True)

        # * Button for Save the Canvas
        # Creating a photoimage object to use image
        save_img = PhotoImage(file = r"./Assets/save.png")
        # Resizing image to fit on button
        save_img = save_img.subsample(20, 20)
        # Button Creation
        Button(l1,image=save_img, compound='left', command=self.save_canvas).pack(side='left')


        # * Button for Color Changer
        # Creating a photoimage object to use image
        color_bucket_img = PhotoImage(file = r"./Assets/paint-bucket.png")
        # Resizing image to fit on button
        color_bucket_img = color_bucket_img.subsample(20, 20)
        # Button Creation
        self.color_bucket_bt = Button(l1, image=color_bucket_img, compound='left', bg='#000000', command=self.choose_color)
        self.color_bucket_bt.pack(side='left',padx=10)

        # * Button for Pen
        # Creating a photoimage object to use image
        pen_img = PhotoImage(file = r"./Assets/pen.png")
        # Resizing image to fit on button
        pen_img = pen_img.subsample(20, 20)
        # Button Creation
        Button(l1,image=pen_img, compound='left',command=self.pen).pack(side='left',padx=5)

        # * Button for Eraser
        # Creating a photoimage object to use image
        eraser_img = PhotoImage(file = r"./Assets/eraser.png")
        # Resizing image to fit on button
        eraser_img = eraser_img.subsample(10, 10)
        # Button Creation
        Button(l1, image=eraser_img, compound='left', command=self.eraser).pack(side='left',padx=10)
        
        # Extra Gap
        Label(l1).pack(side='left',padx=15)

        # * Button for Clear the Canvas
        # Creating a photoimage object to use image
        clear_img = PhotoImage(file = r"./Assets/clear.png")
        # Resizing image to fit on button
        clear_img = clear_img.subsample(20, 20)
        # Button Creation
        Button(l1, image=clear_img, compound='left', command=self.clear).pack(side='left',padx=10)

        # Extra Gap
        Label(l1).pack(side='left',padx=15)

        # * Button for increase Pen Size
        # Creating a photoimage object to use image
        plus_img = PhotoImage(file = r"./Assets/plus.png")
        # Resizing image to fit on button
        plus_img = plus_img.subsample(20, 20)
        # Button Creation
        Button(l1, image=plus_img, compound='left', command=lambda: self.change_thicness(i=1)).pack(side='left')
        
        # * Pen Size Display
        self.brush_size = Label(l1,text=self.thickness,font=('',15))
        self.brush_size.pack(side='left',padx=5)

        # * Button for decrease Pen Size
        # Creating a photoimage object to use image
        minus_img = PhotoImage(file = r"./Assets/minus.png")
        # Resizing image to fit on button
        minus_img = minus_img.subsample(20, 20)
        # Button Creation
        Button(l1, image=minus_img, compound='left', command=lambda: self.change_thicness(i=-1)).pack(side='left')
        
        # * Start/Stop Button for detection
        self.command_bt = Button(l1,text='Strat',command=self.engine)
        self.command_bt.pack(side='right')

        # * Button to show hand Landmarks
        self.hand_bt = Button(l1,text='Show Hand',command=self.draw_hand)
        self.hand_bt.pack(side='right')
        
        # * Middle Frame
        frame = Frame(self)
        frame.pack(fill='both',expand=True)
        
        # * Image Canvas
        self.canvas = Canvas(frame,width=self.width,height=self.height)
        self.canvas.pack()

        # * Bottum Label
        self.l2 = Label(self,bg='#3e00ff',text='Not Started',font=('',18),fg='#d4087a',height=2)
        self.l2.pack(fill='x',expand=True)

        # * Key Bindings
        self.bind('<Control-s>',self.save_canvas)       # Key bind for saving canvas
        self.bind('<Control-C>',self.clear)             # Key bind for clean the canvas
        self.bind('<Control-h>',self.draw_hand)         # Key bind for Toggle display of hand Landmarks


        # * Main Loop
        self.mainloop()
    
    def choose_color(self):
        '''
        Method for the Color Picker
        '''
        # variable to store hexadecimal code of color
        color = colorchooser.askcolor(title ="Choose color")
        self.mcolor = self.color = color[0]
        self.color_bucket_bt.config(bg=color[1])
    
    def pen(self):
        '''
        Method for the Pen
        '''
        self.color = self.mcolor
        self.thickness = 5
        self.brush_size['text'] = 5
        self.color_bucket_bt['state'] = 'normal'
    
    def eraser(self):
        '''
        Method for the Eraser
        '''
        self.mcolor = self.color
        self.color=(255,255,255)
        self.thickness = 20
        self.brush_size['text'] = 20
        self.color_bucket_bt['state'] = 'disable'
    
    def change_thicness(self,i):
        '''
        Method for changing the thicness
        '''
        if self.thickness + i != 0:
            self.thickness = self.thickness + i
            self.brush_size['text'] = self.thickness

    def clear(self,event=None):
        '''
        Method for Clear the Canvas
        '''
        self.canvas_img = np.ones((self.height,self.width,3),dtype=np.int8) * 255

    def draw_hand(self,event=None):
        '''
        Method to toggle the display the hand landmarks
        '''
        if self.drawhand:
            self.drawhand = False
            self.hand_bt['text'] = 'Show Hand'
        else:
            self.drawhand = True
            self.hand_bt['text'] = 'Hide Hand'
    
    def save_canvas(self,event=None):
        '''
        Method to save the Canvas
        '''
        try:
            file_loc = fd.asksaveasfilename(master=self, initialdir = "./",
                                            title = "Save the Image",
                                            filetypes = (("PNG Images","*.png"),
                                                        ("JPG Images","*.jpg")))
            img = self.canvas_img.astype(np.uint8)
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            cv2.imwrite(file_loc,img)
        except Exception:
            pass

    def engine(self):
        '''
        Method to Start the cam
        '''
        if self.isrunning:
            self.cam.release()
            self.command_bt.config(text='Start')
            self.xp = self.yp = ''
            self.isrunning = False
            self.l2.config(text='Stoped',font=('',18))
            self.after_cancel(self.after_id)

            # Convert the Image object into a TkPhoto object
            img = self.canvas_img.astype(np.uint8)
            self.imgtk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(img))
            # Put it in the display window
            self.canvas.create_image(0, 0, image = self.imgtk, anchor='nw')
        else:
            self.cam = cv2.VideoCapture(0)
            self.command_bt.config(text='Stop')
            self.isrunning = True
            self.detect()
    
    @staticmethod
    def get_landmarks(handLM,imgshape):
        '''
        Method to get the land marks into list formate
        '''
        lm_list = []
        for ids, lm in enumerate(handLM.landmark):
            h, w = imgshape
            lm_list.append([int(w*lm.x),int(h*lm.y)])
        return lm_list

    def detect(self):
        '''
        Method to detect the hand from the Image
        '''
        # Get the Frame
        _, frame = self.cam.read()
        
        # Mirror the frame output
        frame = cv2.flip(frame,1)

        # Converting into RBG space
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        # creating a tracker for hand
        tracker = np.ones((self.height,self.width,3),dtype=np.int8) * 255 

        # Getting the Hand deatils
        results = hands.process(frame)

        # Cheking is their any hand detected or not
        if results.multi_hand_landmarks:
            # Only selcting the first detected hand
            handLM = results.multi_hand_landmarks[0]

            # converting the hand landmarks in a python list    
            lm_list = self.get_landmarks(handLM,(self.height,self.width))

            # all 5 fingers tips
            x1, y1 = lm_list[8]
            x2, y2 = lm_list[12]
            x3, y3 = lm_list[16]
            x4, y4 = lm_list[20]

            # * Checking of the Modes
            if lm_list[6][1] >= y1 and lm_list[10][1] >= y2 and lm_list[14][1] <= y3 and lm_list[18][1] <= y4:
                # * Hover Mode
                # index finger tip position updation
                self.xp = self.yp = ''

                # merging the canvas to the frame
                tracker = cv2.bitwise_and(self.canvas_img,tracker)

                # display the marker
                cv2.circle(tracker,(x1,y1),10,self.mcolor,2)
                
                # display the mode
                self.l2.config(text='In Hover Mode',font=('',18))

            elif lm_list[6][1] >= y1 and lm_list[10][1] <= y2 and lm_list[14][1] <= y3 and lm_list[18][1] <= y4:
                # * Draw Mode

                # If it not the Frist detection
                if self.xp != '' and self.yp != '':
                    # drawing into the canvas
                    cv2.line(self.canvas_img,(x1,y1),(self.xp,self.yp),self.color,self.thickness)
                
                # index finger tip position updation
                self.xp = x1
                self.yp = y1
                
                # merging the canvas to the frame
                tracker = cv2.bitwise_and(self.canvas_img,tracker)
                
                # display the marker
                cv2.circle(tracker,(x1,y1),10,self.mcolor,2)

                # display the mode
                self.l2.config(text='In Draw Mode',font=('',18))

            else:
                # * Undefined Gesture Mode

                # index finger tip position updation
                self.xp = self.yp = ''

                # merging the canvas to the frame
                tracker = cv2.bitwise_and(self.canvas_img,tracker)

                # display te mode
                self.l2.config(text='Undefined Gesture',font=('',18))
            
            # for draning the hand landmark
            if self.drawhand:
                mpDraw.draw_landmarks(tracker,handLM,mpHands.HAND_CONNECTIONS)
        else:
            # if no hand dected

            # merging the canvas to the frame
            tracker = cv2.bitwise_and(self.canvas_img,tracker)

            # display te mode
            self.l2.config(text='Unable To Detect',font=('',18))

        # Convert the Image object into a TkPhoto object
        tracker = tracker.astype(np.uint8)
        self.imgtk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(tracker))
        
        # Put it in the display window
        self.canvas.create_image(0, 0, image=self.imgtk, anchor='nw')
        self.after_id = self.after(10,self.detect)

    def __del__(self):
        '''
        Method to destory the cam
        '''
        try:
            if self.cam.isOpened():
                self.cam.release()
        except Exception:
            pass

if __name__ == "__main__":
    App()