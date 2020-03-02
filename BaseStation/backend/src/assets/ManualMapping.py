import json
from tkinter import *
import threading
from tkinter import ttk

import PIL
import PIL.Image, PIL.ImageTk
from src.domain.vision.TableCropper import *
import os


class ManualMapping(object):
    def __init__(self):
        self.puck_mapping = {}
        self.table_mapping = {}
        self.table_id = None
        self.current_image_id = None
        self.temp_puck_position = None
        self.temp_corner_position = None
        self.load_mapping("Mapping/")
        self.master = Tk()
        self.master.title("Manual mapping Design 3")
        self.master.geometry("1600x900")
        self.run()
        self.master.mainloop()

    def run(self):
        app = Frame(self.master)
        frame = Frame(app)
        frame.grid(row=0, column=0, sticky="n")
        # Table Id section
        Label(frame, text="Table Id").grid(row=0, column=0, padx=20, pady=10)
        table_ids_combobox = ttk.Combobox(frame,
                                          width=30,
                                          values=[*self.puck_mapping])
        table_ids_combobox.grid(row=1, column=0, padx=20)

        new_table_id_button = Button(frame, text='new table', width=25)
        new_table_id_button.grid(row=2, column=0, pady=10)

        Label(frame, text="Table Id").grid(row=3, column=0, padx=20, pady=10)
        table_images_ids_listbox = Listbox(frame, width=35, height=25)
        # table_images_ids_listbox.configure(state=DISABLED)
        table_images_ids_listbox.grid(row=4, column=0, padx=20)

        map_button = Button(frame, text='map', width=25, state=DISABLED)
        map_button.grid(row=5, column=0, pady=10)
        capture_button = Button(frame, text='capture new image', width=25, state=DISABLED)
        capture_button.grid(row=6, column=0, pady=10)
        scan_button = Button(frame, text='scan', width=25)
        scan_button.grid(row=7, column=0, pady=10)
        clean_button = Button(frame, text='clean mappings', width=25)
        clean_button.grid(row=8, column=0, pady=10)
        # Create a canvas that can fit the above image
        canvas = Canvas(app, width=1316, height=880, background='white')
        canvas.grid(row=0, column=1)

        def new_table_id_dialog(e):
            sub_master = Toplevel(self.master)
            root = Frame(sub_master)
            Label(root, text="Table id", width=10).grid(row=0)
            table_id = StringVar()
            new_table_id_entry = Entry(root, textvariable=table_id)
            new_table_id_entry.grid(row=0, column=1)

            def add_new_table_id():
                new_table_id = new_table_id_entry.get()
                self.set_default_table_id(new_table_id)
                table_id_list = [*self.puck_mapping]
                table_ids_combobox['values'] = table_id_list
                table_ids_combobox.current(table_id_list.index(new_table_id))
                table_id_change(None)
                self.save_mapping("Mapping/")
                sub_master.destroy()

            Button(root, text='confirm', width=25, command=add_new_table_id).grid(row=1)
            root.pack()

        new_table_id_button.bind("<Button-1>", new_table_id_dialog)

        def table_id_change(e):
            self.tk_preview_image = None
            self.current_image_id = None
            capture_button.config(state=NORMAL)
            map_button.config(state=DISABLED)
            self.table_id = table_ids_combobox.get()
            table_images_ids_listbox.delete(0, END)
            for image_name in sorted([*self.puck_mapping[self.table_id]], key=lambda s: int(s[6:])):
                print(image_name)
                table_images_ids_listbox.insert(END, image_name)

        table_ids_combobox.bind("<<ComboboxSelected>>", table_id_change)

        def table_image_id_change(e):
            self.current_image_id = table_images_ids_listbox.get(int(table_images_ids_listbox.curselection()[0]))
            cv_preview_image = self.table_image_computed_preview(self.table_id, self.current_image_id)
            self.tk_preview_image = self.cv_image_to_tkinter(cv_preview_image)
            if not hasattr(self, "image_on_canvas"):
                self.image_on_canvas = canvas.create_image(658, 440, anchor=CENTER, image=self.tk_preview_image)
            else:
                canvas.itemconfig(self.image_on_canvas, image=self.tk_preview_image)
            map_button.config(state=NORMAL)

        table_images_ids_listbox.bind('<<ListboxSelect>>', table_image_id_change)

        def map_image(e):
            if self.table_id is not None and self.current_image_id is not None:
                self.map_image(self.table_id, self.current_image_id)
                table_image_id_change(None)

        map_button.bind("<Button-1>", map_image)

        def capture_image(e):
            if self.table_id is not None:
                cam = cv2.VideoCapture(0)
                ret, frame = cam.read()
                cam.release()
                count = 0
                image_id = "image_{}".format(count)
                while os.path.exists("Mapping/{}/{}.jpg".format(self.table_id, image_id)):
                    count += 1
                    image_id = "image_{}".format(count)

                cv2.imwrite("Mapping/{}/{}.jpg".format(self.table_id, image_id), frame)

        capture_button.bind("<Button-1>", capture_image)

        def scan_files(e):
            self.scan_new_files()
            table_id_change(None)

        scan_button.bind("<Button-1>", scan_files)

        def clean_mapping(e):
            self.clean_mapping_non_existing()
            table_id_list = [*self.puck_mapping]
            table_ids_combobox['values'] = table_id_list
            table_ids_combobox.current(0)
            table_id_change(None)

        clean_button.bind("<Button-1>", clean_mapping)

        app.pack()

    def load_mapping(self, directory):
        with open(directory + "puck_mapping.json") as mapping_json_file:
            self.puck_mapping = json.loads(mapping_json_file.read())
        with open(directory + "table_mapping.json") as mapping_json_file:
            self.table_mapping = json.loads(mapping_json_file.read())

    def save_mapping(self, directory):
        with open(directory + "puck_mapping.json", "w") as mapping_json_file:
            mapping_json_file.write(json.dumps(self.puck_mapping))
        with open(directory + "table_mapping.json", "w") as mapping_json_file:
            mapping_json_file.write(json.dumps(self.table_mapping))

    def set_default_table_id(self, table_id):
        self.table_mapping.setdefault(table_id, [])
        self.puck_mapping.setdefault(table_id, {})

    def set_default_table_image_id(self, table_id, image_id):
        self.puck_mapping[table_id].setdefault(image_id, {})

    def clean_mapping_non_existing(self):
        table_id_to_remove = []

        self.load_mapping("Mapping/")

        for table_id in self.puck_mapping:
            image_id_to_remove = []
            if not os.path.exists("Mapping/{}".format(table_id)):
                table_id_to_remove.append(table_id)
            else:
                for image_id in self.puck_mapping[table_id]:
                    if not os.path.exists("Mapping/{}/{}.jpg".format(table_id, image_id)):
                        image_id_to_remove.append(image_id)
            for image_id in image_id_to_remove:
                self.puck_mapping[table_id].pop(image_id)

        for table_id in table_id_to_remove:
            self.puck_mapping.pop(table_id)
            self.table_mapping.pop(table_id)

        self.save_mapping("Mapping/")

    def scan_new_files(self):
        table_id_found = 0
        image_found = 0
        self.load_mapping("Mapping/")

        for file in os.listdir("Mapping"):
            if os.path.isdir("Mapping/" + file):
                if not (file in self.puck_mapping):
                    self.puck_mapping.setdefault(file, {})
                    self.table_mapping.setdefault(file, [])
                    table_id_found += 1
        for table_id in self.puck_mapping:
            if os.path.exists("Mapping/{}".format(table_id)):
                for image_name in os.listdir("Mapping/{}".format(table_id)):
                    if image_name.endswith(".jpg"):
                        image_name = image_name.replace(".jpg", "")
                        if not (image_name in self.puck_mapping[table_id]):
                            self.puck_mapping[table_id].setdefault(image_name, {})
                            image_found += 1

        self.save_mapping("Mapping/")

    def table_image_computed_preview(self, table_id, image_id):
        image = cv2.imread("Mapping/{}/{}.jpg".format(table_id, image_id))
        if len(self.table_mapping[table_id]) == 4:
            table_cropper = TableCropper(self.table_mapping[table_id])
            image_cropped = table_cropper.crop(image)
            for color in self.puck_mapping[table_id][image_id]:
                puck_position = self.puck_mapping[self.table_id][self.current_image_id][color]
                cv2.circle(image_cropped, (puck_position['x'], puck_position['y']), 2, (0, 255, 0), 2)
            return image_cropped
        else:
            return image

    @staticmethod
    def cv_image_to_tkinter(cv_image):
        cv_image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        return PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_image_rgb))

    def map_corners(self, image):
        sub_master = Toplevel(self.master)
        self.get_table_corner(sub_master, image, "Click on the upper left corner of the table")
        self.master.wait_window(sub_master)
        self.table_mapping[self.table_id].append(self.temp_corner_position)
        sub_master = Toplevel(self.master)
        self.get_table_corner(sub_master, image, "Click on the upper right corner of the table")
        self.master.wait_window(sub_master)
        self.table_mapping[self.table_id].append(self.temp_corner_position)
        sub_master = Toplevel(self.master)
        self.get_table_corner(sub_master, image, "Click on the lower left corner of the table")
        self.master.wait_window(sub_master)
        self.table_mapping[self.table_id].append(self.temp_corner_position)
        sub_master = Toplevel(self.master)
        self.get_table_corner(sub_master, image, "Click on the lower right corner of the table")
        self.master.wait_window(sub_master)
        self.table_mapping[self.table_id].append(self.temp_corner_position)

    def get_table_corner(self, sub_master, image, text):
        self.temp_corner_position = {"x": None, "y": None}
        root = Frame(sub_master)

        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONUP:
                self.temp_corner_position['x'] = x
                self.temp_corner_position['y'] = y
                cv2.destroyAllWindows()
                sub_master.destroy()

        Label(root, text=text).pack()
        cv2.imshow("table_image", image)
        cv2.setMouseCallback("table_image", click_event)
        root.pack()

    def map_puck_color(self, image):
        colors = ["red", "orange", "yellow", "green", "blue", "brown", "gray", "black", "white", "purple"]
        for color in colors:
            self.temp_puck_position = None
            sub_master = Toplevel(self.master)
            self.get_puck_color_position(sub_master, image, color)
            self.master.wait_window(sub_master)
            if self.temp_puck_position is None:
                self.puck_mapping[self.table_id][self.current_image_id].pop(color, None)
            else:
                self.puck_mapping[self.table_id][self.current_image_id][color] = self.temp_puck_position

    def get_puck_color_position(self, sub_master, image, color):
        image_copy = image.copy()
        self.temp_puck_position = {"x": None, "y": None}

        get_puck_position_app = Frame(sub_master)

        def click_event(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONUP:
                self.temp_puck_position['x'] = x
                self.temp_puck_position['y'] = y
                cv2.destroyAllWindows()
                sub_master.destroy()

        def no_position():
            self.temp_puck_position = None
            cv2.destroyAllWindows()
            sub_master.destroy()

        def keep_same():
            cv2.destroyAllWindows()
            sub_master.destroy()
        Label(get_puck_position_app, text=color).grid(row=0)
        not_on_image_button = Button(get_puck_position_app, text='not on image', width=25, command=no_position)
        if 'x' in self.puck_mapping[self.table_id][self.current_image_id].get(color, {}):
            self.temp_puck_position['x'] = self.puck_mapping[self.table_id][self.current_image_id][color]['x']
            self.temp_puck_position['y'] = self.puck_mapping[self.table_id][self.current_image_id][color]['y']
            cv2.circle(image_copy, (self.temp_puck_position['x'], self.temp_puck_position['y']), 2, (0, 255, 0), 2)
            not_on_image_button.grid(row=1, column=0)
            Button(get_puck_position_app, text='keep current value', width=25, command=keep_same).grid(row=1, column=1)
        else:
            not_on_image_button.grid(row=1)
        cv2.imshow("table_image", image_copy)
        cv2.setMouseCallback("table_image", click_event)
        get_puck_position_app.pack()

    def map_image(self, table_id, image_id):
        image = cv2.imread("Mapping/{}/{}.jpg".format(table_id, image_id))
        while len(self.table_mapping[table_id]) != 4:
            self.table_mapping[self.table_id] = []
            self.map_corners(image)
        table_cropper = TableCropper(self.table_mapping[self.table_id])
        cropped = table_cropper.crop(image)
        self.map_puck_color(cropped)
        self.save_mapping("Mapping/")




if __name__ == '__main__':
    manualMapping = ManualMapping()
    # manualMapping.complete_mapping()
    # manualMapping.scan_new_files()
    # manualMapping.main_menu()
