import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =0.5
SHORT_BREAK_MIN =0.5
LONG_BREAK_MIN =0.5
reps=0
reps_of_wrk=""
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps_of_wrk, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer",fg=GREEN)
    reps_of_wrk=""
    check_marks.config(text=reps_of_wrk)
    reps=0
        

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    if reps > 8:
        reps = 1
        
    if reps%2==1:
        time=WORK_MIN
        label.config(text="Work",fg=GREEN)
    elif reps != 8:
        time=SHORT_BREAK_MIN
        label.config(text="Break",fg=PINK)
    else:
        time=LONG_BREAK_MIN
        label.config(text="Break",fg=RED)
    
    countdown(time*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global reps, reps_of_wrk, timer
    
    count_minutes=int(count/60)
    count_seconds=count%60
    if count_seconds<10:
        count_seconds="0"+str(count_seconds)
    
    canvas.itemconfig(timer_text,text=f"{count_minutes}:{count_seconds}")
    if count >0:
        timer = window.after(1000, countdown, count-1)
    else:
        if reps%2==1:
            reps_of_wrk+="✔"
            check_marks.config(text=reps_of_wrk)
        start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title("Pomodore")
window.config(padx=100,pady=50, bg=YELLOW)



canvas =tkinter.Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_image=tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


label =tkinter.Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"), bg=YELLOW)
label.grid(column=2,row=1)

start_button=tkinter.Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=1,row=3,)

reset_button=tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=3,row=3)

check_marks=tkinter.Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,15,"bold"))
check_marks.grid(column=2,row=4)



window.mainloop()