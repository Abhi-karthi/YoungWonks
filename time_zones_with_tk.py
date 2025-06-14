from tkinter import *
import pygame
from datetime import datetime
import pytz
from tkinter import messagebox
india_flag_ = pygame.image.load("/Users/aaavi/PycharmProjects/YoungWonks/venv/India_Flag.png")
france_flag_ = pygame.image.load("/Users/aaavi/PycharmProjects/YoungWonks/venv/france_flag.jpeg")
india_flag_ = pygame.transform.scale(india_flag_, (200, 100))
france_flag_ = pygame.transform.scale(france_flag_, (200, 100))
pygame.image.save(india_flag_, "india.png")
pygame.image.save(france_flag_, "france.png")
root = Tk()
root.title("Time Zones")
root.geometry("200x200")
india = Frame(root, width=200, height=250)
india.grid(row=0, column=0)
india_flag = PhotoImage(file="india.png")
india_flag_lable = Label(india, image=india_flag).pack()
india_timezone = pytz.timezone("Asia/Calcutta")
india_current = datetime.now(india_timezone)
final_time = india_current.strftime("%Y-%m-%d %l:%M:%S %p %Z")
print(india_current.strftime("%Y-%m-%d %l:%M:%S %p %Z"))
#Tip: To know all the time zones in the world, print pytz.all_timezones
india_time = Label(india, text=india_current.strftime("%Y-%m-%d %l:%M:%S %p %Z"))
india_time.pack()
print(pytz.all_timezones)
#india_timezone = pytz.timezone("Asia/Calcutta")

indiaa = Frame(root, width=200, height=250)
indiaa.grid(row=0, column=1)
indiaa_flag = PhotoImage(file="france.png")
indiaa_flag_lable = Label(indiaa, image=indiaa_flag).pack()
indiaa_timezone = pytz.timezone("Europe/Chisinau")
indiaa_current = datetime.now(indiaa_timezone)
finaal_time = indiaa_current.strftime("%Y-%m-%d %l:%M:%S %p %Z")
print(indiaa_current.strftime("%Y-%m-%d %l:%M:%S %p %Z"))
#Tip: To know all the time zones in the world, print pytz.all_timezones
indiaa_time = Label(indiaa, text=indiaa_current.strftime("%Y-%m-%d %l:%M:%S %p %Z"))
indiaa_time.pack()
#india_timezone = pytz.timezone("Asia/Calcutta")




# Format the time in a particular order
while True:
    india_timezone = pytz.timezone("Asia/Calcutta")
    india_current = datetime.now(india_timezone)
    india_final_time = india_current.strftime("%Y-%m-%d %l:%M:%S %p %Z")
    print(india_current.strftime("%Y-%m-%d %l:%M:%S %p %Z"))
    #Tip: To know all the time zones in the world, print pytz.all_timezones
    india_time.config(text=india_current.strftime("%Y-%m-%d %l:%M:%S %p %Z"))

    indiaa_timezone = pytz.timezone("Europe/Chisinau")
    indiaa_current = datetime.now(india_timezone)
    indiaa_final_time = indiaa_current.strftime("%Y-%m-%d %l:%M:%S %p %Z")
    print(indiaa_current.strftime("%Y-%m-%d %l:%M:%S %p %Z"))
    # Tip: To know all the time zones in the world, print pytz.all_timezones
    indiaa_time.config(text=indiaa_current.strftime("%Y-%m-%d %l:%M:%S %p %Z"))
    root.update()
