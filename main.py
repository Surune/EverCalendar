from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
from turtle import Screen, Turtle, mainloop
import calendar

# 변수 선언==========================================================================================================================================
height=0 ; width=0
year=0 ; month=0
pic_x=0 ; pic_y=0
cal_pos_x=0; cal_pos_y=0
filename=None
r=0; g=0; b=0
#===================================================================================================================================================

# 달력의 배경화면으로 쓰일 사진 입력==================================================================================================================
def select_file():
    global filename
    filename = filedialog.askopenfilename(initialdir = "C:",title = "Choose your file",filetypes = (("PNG","*.png"),("all files","*.*")))
    start.destroy()
    sel_size()
#===================================================================================================================================================

# 달력의 전체 크기 조절자=============================================================================================================================
def size1():
    global pic_x, pic_y
    pic_x=1440 ; pic_y=1080
    ask_ym()
    s_size.destroy()
    
def size2():
    global pic_x, pic_y
    pic_x=1080 ; pic_y=1440
    ask_ym()
    s_size.destroy()

def size3():
    global pic_x, pic_y
    pic_x=2560 ; pic_y=1440
    ask_ym()
    s_size.destroy()
    
def size4():
    global pic_x, pic_y
    pic_x=1440 ; pic_y=2560
    ask_ym()
    s_size.destroy()
    
def sel_size():
    global s_size
    s_size=Tk()
    s_size.title("Select Size")
    
    global filename
    global width, height
    img=Image.open(filename)
    width, height= img.size
    
    reimg=img.resize((int(width/3), int(height/3)))
    reimg.save("resized.png")
    photo=PhotoImage(file="resized.png")
    l_img=Label(s_size, image=photo)
    l_img.image=photo
    l_img.pack()
    l_des=Label(s_size, text="[  화질이 깨져 보일 수 있으나, 걱정하지 않으셔도 됩니다 :)  ]")
    l_des.pack()
    Selsize1=Button(s_size, text="\n      1440 x 1080       \n", command=size1)
    Selsize2=Button(s_size, text="\n      1080 x 1440       \n", command=size2)
    Selsize3=Button(s_size, text="\n      2560 x 1440       \n", command=size3)
    Selsize4=Button(s_size, text="\n      1440 x 2560       \n", command=size4)
    Selsize1.pack(side=LEFT)
    Selsize2.pack(side=LEFT)
    Selsize3.pack(side=LEFT)
    Selsize4.pack(side=LEFT)
#===================================================================================================================================================

# 색상 조합 및 선택==================================================================================================================================
def color_cal():
    global check_col
    check_col=Tk()
    check_col.title("Changel calendar's color")
    check_col.resizable(width=False, height=False)
    B_col=Button(check_col, text="\n   색상 변경   \n", command=change_cal)
    B_col.pack()
    sel_color()

# Python IDLE - Help - Turtle Demo
def sel_color():
    class ColorTurtle(Turtle):
        def __init__(self, x, y):
            Turtle.__init__(self)
            self.shape("circle")
            self.resizemode("user")
            self.shapesize(2,2,4)
            self.pensize(7)
            self._color = [0,0,0]
            self.x = x
            self._color[x] = y
            self.color(self._color)
            self.speed(0)
            self.left(90)
            self.pu()
            self.goto(x,0)
            self.pd()
            self.sety(1)
            self.pu()
            self.sety(y)
            self.pencolor("gray25")
            self.ondrag(self.shift)

        def shift(self, x, y):
            self.sety(max(0,min(y,1)))
            self._color[self.x] = self.ycor()
            self.fillcolor(self._color)
            setbgcolor()

    def setbgcolor():
        global r, g, b
        screen.bgcolor(red.ycor(), green.ycor(), blue.ycor())
        r=red.ycor()
        g=green.ycor()
        b=blue.ycor()
        
    def main():
        global screen, red, green, blue
        screen = Screen()
        screen.delay(0)
        screen.setworldcoordinates(-1, -0.3, 3, 1.3)

        red = ColorTurtle(0, .5)
        green = ColorTurtle(1, .5)
        blue = ColorTurtle(2, .5)
        setbgcolor()

        writer = Turtle()
        writer.ht()
        writer.pu()
        writer.goto(1, 1.13)
        writer.write("원하는 색상을 만드세요", align="center", font=('맑은 고딕', 19))
        return "EVENTLOOP"
    
    if __name__ == "__main__":
        msg = main()
        mainloop()

def change_cal():
    save_cal()
    resized=Image.open("resized2.png")
    calendar=Image.open("cal.png")
    width_cal, height_cal=calendar.size
    resized_calendar=calendar.resize((int(width_cal*1.5), int(height_cal*1.5)))
    calendar.close()
    resized_calendar.save("cal.png")
    img_resized_cal=Image.open("cal.png")
    resized.paste(img_resized_cal, (cal_pos_x, cal_pos_y), img_resized_cal)
    resized.save("resized3.png")
    photo=PhotoImage(file="resized3.png")
    L_edit_img.configure(image=photo)
    L_edit_img.image=photo
#===================================================================================================================================================

# 달력 위치 입력받기 및 작동==========================================================================================================================    
def callback(event):
    save_cal()
    global cal_pos_x, cal_pos_y
    resized=Image.open("resized2.png")
    calendar=Image.open("cal.png")
    width_cal, height_cal=calendar.size
    resized_calendar=calendar.resize((int(width_cal*1.5), int(height_cal*1.5)))
    calendar.close()
    resized_calendar.save("cal.png")
    img_resized_cal=Image.open("cal.png")
    resized.paste(img_resized_cal, (event.x, event.y), img_resized_cal)
    resized.save("resized3.png")
    photo=PhotoImage(file="resized3.png")
    L_edit_img.configure(image=photo)
    L_edit_img.image=photo
    cal_pos_x=event.x
    cal_pos_y=event.y
    
def sel_pos():
    #http://noon.tistory.com/1157
    global height, width
    sel_pos=Tk()
    sel_pos.title("Click to select position")
    
    frame=Frame(sel_pos, width=int(width/2), height=int(height/2), bg='white')
    frame.bind("<Button-1>", callback)
    frame.pack()
    lab_pos=Label(sel_pos, text="위치를 선택해주세요.", bg='black', fg='white')
    lab_pos.pack(fill=BOTH)
#===================================================================================================================================================

# 달력 만들 년, 월 입력 및 생성=======================================================================================================================
def ask_ym():
    global asking, entry_y, entry_m
    asking=Tk()
    asking.title("Input Year&Month")
    asking.resizable(width=False, height=False)
    entry_y=Entry(asking)
    entry_m=Entry(asking)
    label_ym=Label(asking, text="\n달력을 만들 년, 월을 입력해주세요\n")
    label_y=Label(asking, text=" 년  ")
    label_m=Label(asking, text=" 월  ")
    button_ym=Button(asking, text="\n    확인    \n", command = make_cal, bg="white")
    label_ym.grid(row=0, columnspan=4)
    entry_y.grid(row=1, column=0)
    label_y.grid(row=1, column=1)
    entry_m.grid(row=1, column=2)
    label_m.grid(row=1, column=3)
    button_ym.grid(row=2, columnspan=4)

def make_cal():
    global year, month
    year=int(entry_y.get())
    month=int(entry_m.get())
    save_cal()
    asking.destroy()
    editor()

def save_cal():
    cal_text=calendar.month(year, month)
    im=Image.new('RGBA', (250, 250))
    draw=ImageDraw.Draw(im)
    draw.text((1,1), text=cal_text, fill='black')
    for x in range(250):
        for y in range(250):
            if(im.getpixel((x,y))==(0,0,0,255)):
                im.putpixel((x,y),(int(r*255),int(g*255),int(b*255), 255))
    im.save("cal.png")
#===================================================================================================================================================

# 달력 저장==========================================================================================================================================
def save_img():
    global width, height
    pathway = filedialog.asksaveasfilename(initialdir = "C:", title = "Save your file")
    img=Image.open("resized3.png")
    reimg=img.resize((pic_x, pic_y))
    reimg.save(pathway)
#===================================================================================================================================================

# 전체 편집기========================================================================================================================================
def editor():
    edit=Tk()
    edit.title("Edit your Calendar")
    edit.resizable(width=False, height=False)
    
    global filename
    global width, height
    global L_edit_img
    img=Image.open(filename)
    width, height= img.size
    reimg=img.resize((int(width/2), int(height/2)))
    reimg.save("resized2.png")
    resized=Image.open("resized2.png")
    calendar=Image.open("cal.png")
    width_cal, height_cal=calendar.size
    resized_calendar=calendar.resize((int(width_cal*1.5), int(height_cal*1.5)))
    calendar.close()
    resized_calendar.save("cal.png")
    img_resized_cal=Image.open("cal.png")
    resized.paste(img_resized_cal, (0,0), img_resized_cal)
    resized.save("resized3.png")
    photo=PhotoImage(file="resized3.png")
    L_edit_img=Label(edit, image=photo)
    L_edit_img.image=photo
    L_edit_img.grid(row=0, columnspan=4)
    L_des=Label(edit, text="[  화질이 깨져 보일 수 있으나, 걱정하지 않으셔도 됩니다 :)  ]")
    L_des.grid(row=1, columnspan=4)

    B_1=Button(edit, text="\n 달력 위치 조절 \n", command=sel_pos)
    B_1.grid(row=2, column =0)

    B_2=Button(edit, text="\n 달력 색상 변경 \n", command=color_cal)
    B_2.grid(row=2, column=1)

    B_3=Button(edit, text="\n               \n", state="disabled")
    B_3.grid(row=2, column=2)

    B_4=Button(edit, text="\n      저장      \n", command=save_img)
    B_4.grid(row=2, column=3)

    edit.mainloop()
#===================================================================================================================================================

# 시작===============================================================================================================================================
def start_program():
    root.destroy()
    
    global start
    start=Tk()
    start.title("Select Background")
    start.resizable(width=False, height=False)
    start.geometry("470x110")

    SelpicL=Label(start, text="배경 화면을 선택해주세요\n\n(되도록이면 고화질의 사진을 이용해주세요)")
    SelpicB=Button(start, text="\n 파일 선택 \n", command=select_file, bg="white")
    SelpicL.place(x=40, y=30)
    SelpicB.place(x=350, y=30)
#===================================================================================================================================================

# 프로그램 실행======================================================================================================================================
root=Tk()
root.title("EverCalendar")
root.resizable(width=False, height=False)
photo=PhotoImage(file="LOGO.png")
L_logo=Label(root, image=photo)
L_logo.pack()
root.after(2222, start_program)
#===================================================================================================================================================
