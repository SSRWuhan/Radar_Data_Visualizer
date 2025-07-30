import math
import time
import threading
import tkinter as tk
from tkinter import ttk


class rdv:
    def __init__(self, title = "radar_visualizer", refreash_rate=0.00125, data_visualization_scope = 30, max_distance=180):
        self.distance = 0
        self.angle = 0
        self.max_distance = max_distance
        self.angle_data = [] # format: [(angle, lenght), (angle, lenght), .....]

        self.CANVAS_WIDTH = 300
        self.CANVAS_HEIGTH = 150
        self.RADAR_BASE_X = 150
        self.RADAR_BASE_y = 150
        self.radius =(self.CANVAS_WIDTH - 60) / 2
        self.title = title
        self.refreash_rate = refreash_rate
        self.data_visualization_scope = data_visualization_scope

    def __change(self, max, radius_type, canvas):
        self.max_distance = int(max)
        self.radius_type = radius_type
        if self.radius_type == "circle":
            self.CANVAS_HEIGTH = 300
            canvas.config(height=self.CANVAS_HEIGTH)
        else:
            self.CANVAS_HEIGTH = 150
            canvas.config(height=self.CANVAS_HEIGTH)

    def __draw_lines(self, canvas):
        while True:
            if(len(self.angle_data) == 0):
                break

            if(len(self.angle_data) > self.data_visualization_scope):
                self.angle_data.pop(0)

            if(len(self.angle_data) < self.data_visualization_scope):
                end = len(self.angle_data) -1
            else:
                end = self.data_visualization_scope

            for i in range(0, end):
                self.distance = self.angle_data[i][1]
                self.angle = self.angle_data[i][0]
                phi = self.angle * (math.pi / 180)
                relative_length = round((self.distance * self.radius) / self.max_distance)
                x_length = round(relative_length * math.cos(phi))
                y_length = round(relative_length * math.sin(phi))


                x_length += self.RADAR_BASE_X
                y_length = self.RADAR_BASE_y - y_length
                
                canvas.create_line(self.RADAR_BASE_X, self.RADAR_BASE_y, x_length, y_length, fill="blue")
                self.__distance_label.config(text=f"distance: {self.distance}")
                self.__angle_label.config(text=f"angle: {self.angle}")
            time.sleep(self.refreash_rate)

            canvas.delete("all")
            if(self.radius_type == "semi circle"):
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH*2 - 20, outline="green")
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH*2 - 20, outline="green", start=45)
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH*2 - 20, outline="green", start=90)
            else:
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH - 20, outline="green")
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH - 20, outline="green", start=90)
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH - 20, outline="green", start=180)
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH - 20, outline="green", start=270)
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH - 20, outline="green", start=225)
                canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH - 20, outline="green", start=45)
        

    def __run(self):
        window = tk.Tk()
        window.geometry("360x500")
        window.title(self.title)

        radius_type = tk.StringVar()
        self.radius_type = "semi circle"

        frame1 = tk.Frame(window, bg="white", width=360, height=50)
        frame1.pack()

        max_distance_entry = ttk.Entry(frame1, width=13)
        max_distance_entry.insert(0, self.max_distance)
        max_distance_entry.grid(row=0, column=0, padx=20)

        radar_field_of_view = ttk.OptionMenu(frame1, radius_type, "semi circle", "circle", "semi circle")
        radar_field_of_view.grid(row=0, column=1, padx=20)
    
        button = ttk.Button(frame1, text="Ok", command=lambda: self.__change(max_distance_entry.get(), radius_type.get(), canvas))
        button.grid(row=0, column=2, padx=20)

        canvas = tk.Canvas(window, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGTH, bg="black")
        print(f"canvas created with width {self.CANVAS_WIDTH}, height{self.CANVAS_HEIGTH}")
        canvas.pack(padx=20, pady=30)
        canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH*2 - 20, outline="green")
        canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH*2 - 20, outline="green", start=45)
        canvas.create_arc(20, 20, self.CANVAS_WIDTH - 20, self.CANVAS_HEIGTH*2 - 20, outline="green", start=90)


        frame2 = tk.Frame(window, bg="white", width=300, height=100)
        frame2.pack()

        self.__distance_label = ttk.Label(frame2, text=f"distance: {self.distance}")
        self.__distance_label.grid(row=0, column=0, padx=20)

        self.__angle_label = ttk.Label(frame2, text=f"angle: {self.angle}")
        self.__angle_label.grid(row=0, column=1, padx=20)
        stop_event = threading.Event()
        threading.Thread(target=lambda: self.__draw_lines(canvas), daemon=True).start()
      
        window.update()
        tk.mainloop()

        exit()


    def add_data(self, data): # incoming data from radar should be in this string format "angle,length"
        data = data.split(",")
        data = tuple([int(x) for x in data])
        self.angle_data.append(data)
    
    def start(self):
        threading.Thread(target=self.__run, daemon=False).start()
