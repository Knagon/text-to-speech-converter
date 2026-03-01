from tkinter import *
import edge_tts
import asyncio
import subprocess
import ttkbootstrap as ttkb
import threading


def tts_working(text,voice, on_done):
    async def convert():
        file = "text_converted.mp3"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(file)
        on_done()
        subprocess.Popen(["start", file], shell=True)

    asyncio.run(convert())


def progress_work():
    if not tts_done[0]:
        progress.step(0.5)
        app.after(100, progress_work)
    else:
        progress['value'] = 100
        l5_progress2.configure(text="Kompilacja Zakończona", foreground="red")
        l4_progress.grid_forget()


def change_to_done():
    tts_done[0] = True

def start_convert():
    text = text_to_con.get("1.0", "end-1c")
    if not text.strip():
        return
    words = len(text.split())
    time_left = max(1, words / 3)
    #steps_left[0] = int(time_left * 10)

    l4_progress.grid(row=7,column=0,pady=5)
    l5_progress2.grid(row=8,column=0,pady=5)
    progress.grid(row=6,column=0,pady=5)

    time_left = int(time_left)
    if time_left > 60:
        minuts = time_left/60
        minuts = int(minuts)
        l5_progress2.configure(text=f"Zajmie to max: {minuts} minut.")
    else:
        l5_progress2.configure(text=f"Zajmie to max: {time_left} sekund.")

    tts_done[0] = False
    progress_work()

    thread = threading.Thread(target=tts_working, args=(text, voice_box.get(), change_to_done))
    thread.start()



app = ttkb.Window(themename="superhero")
app.geometry("1000x900")
app.title("Konwerter XMZ")
app.columnconfigure(0, weight=1)

tts_done = [False]
#steps_left = [50]

list_voices = ["pl-PL-MarekNeural", "pl-PL-ZofiaNeural", "en-US-MichelleNeural", "en-US-RogerNeural"]

l1 = ttkb.Label(app, text="Witaj w konwerterze tekstu na mowę!", font=("Arial",18, "bold"), foreground="goldenrod3")
l2 = ttkb.Label(app, text="Wpisz tekst do przeczytania ⬇", font=("Arial",18), foreground="gray70")
l3_list = ttkb.Label(app, text="Dźwięk/język", font=("Arial",12, "bold"), foreground="gray70")
voice_box = ttkb.Combobox(app, values=list_voices, height=6, state="readonly")
voice_box.current(0)
btn_start = ttkb.Button(app, text="▶", bootstyle="success", command=start_convert, width=20)
btn_exit = ttkb.Button(app, text="Wyjście", bootstyle="danger",command=app.destroy, width=20)
text_to_con = ttkb.Text(app, font=("Consolas",16), height=20, width=60, wrap="word")
text_to_con.configure(background="#2b3e50",relief="flat")

progress = ttkb.Progressbar(app, orient=HORIZONTAL, length=250, mode="determinate")

l4_progress = ttkb.Label(app, text="Proces w trakcie kompilacji.", font=("Arial", 18), foreground="gray70")
l5_progress2 = ttkb.Label(app, text=f"", font=("Arial", 18), foreground="gray70")


widgets = [l1,l2,l3_list,voice_box,text_to_con,btn_start]

for i in range(len(widgets)):
    widgets[i].grid(row=i, column=0, pady=10)

btn_exit.grid(row=9, column=0, pady=10)
app.mainloop()
