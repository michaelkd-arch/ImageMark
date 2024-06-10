import cv2
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from PIL import Image
import os

app = CTk()
app.geometry('400x300')

set_appearance_mode('dark')

app.title('ImageMark')
app.iconbitmap('myapp.ico')


image_path = ''
watermark_text = ''
new_image_name = ''
folder_path = ''
fontScale = 0.8


def select_image():
    global image_path
    global folder_path
    image_path = filedialog.askopenfilename()
    folder_path = os.path.dirname(image_path)
    label_1.configure(text=os.path.basename(image_path))


def capture_text():
    global watermark_text
    watermark_text = entry.get()


def create_watermark():
    global new_image_name
    new_image_name = entry_2.get()
    if image_path:
        if new_image_name:
            img = cv2.imread(image_path)
            img_height, img_width, _ = img.shape
            # new_height, new_width = image_resize((img_height, img_width))
            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255, 255, 255)
            thickness = 1
            text_size_tuple = cv2.getTextSize(watermark_text, font, fontScale, thickness)
            text_size, _ = text_size_tuple[0]
            org = (img_width - (text_size + 10), img_height - 10)
            text_img = cv2.putText(img, watermark_text, org, font,
                                   fontScale, color, thickness, cv2.LINE_AA)

            filename = f'{folder_path}/{new_image_name}.jpg'
            cv2.imwrite(filename, text_img)
            watermarked_image = Image.open(filename)
            watermarked_image.show()
        else:
            message_box_2()
    else:
        message_box()


def clear_text():
    entry.delete(0, END)
    entry_2.delete(0, END)


def message_box():
    CTkMessagebox(title='Warning', button_width=2, button_color='#C850C0',
                  button_hover_color='#4158D0',
                  message='Please select an image first.',)


def message_box_2():
    CTkMessagebox(title='Warning', button_width=2, button_color='#C850C0',
                  button_hover_color='#4158D0',
                  message='Please enter an image name.',)


# def image_resize(shape_tuple):
#     height = shape_tuple[0]
#     width = shape_tuple[1]
#     if height > 1080:
#         if width > height:
#             s_diff = height - 1080
#             size_r = width / height
#             new_height = height - s_diff
#             new_width = round(size_r * new_height)
#             return new_height, new_width
#         else:
#             return width, height
#     else:
#         return width, height


def change_font(value):
    global fontScale
    font_size = int(value[-1])
    if font_size == 8:
        fontScale = 0.8
    else:
        fontScale = font_size


label_1 = CTkLabel(master=app, text='No image selected', wraplength=300, justify='center')
btn_select_image = CTkButton(master=app, text='Select image', corner_radius=32, fg_color='#C850C0',
                             hover_color='#4158D0', width=12, command=select_image)

label_1.pack(pady=(10, 0), expand=True,)
btn_select_image.pack(expand=True,)


entry = CTkEntry(master=app, placeholder_text='Enter watermark text', width=130,
                 text_color='#FFFFFF')
btn_entry = CTkButton(master=app, text='Submit', corner_radius=32, fg_color='#C850C0',
                      hover_color='#4158D0', width=6, command=capture_text)

entry.pack(pady=(10, 0), expand=True,)
btn_entry.pack(expand=True,)


btn_font = CTkComboBox(master=app, values=['FontSize 0.8', 'FontSize 1', 'FontSize 2',
                                           'FontSize 3', 'FontSize 4', 'FontSize 5'],
                       command=change_font, state='readonly', width=110)

btn_font.set('FontSize')
btn_font.pack(pady=(10, 0), expand=True,)


entry_2 = CTkEntry(master=app, placeholder_text='Enter name for the watermarked image', width=235,
                   text_color='#FFFFFF')
btn_create_watermark = CTkButton(master=app, text='Create Watermark', corner_radius=32, fg_color='#C850C0',
                                 hover_color='#4158D0', width=16, command=create_watermark)

entry_2.pack(pady=(10, 0), expand=True,)
btn_create_watermark.pack(pady=(0, 10), expand=True,)










app.mainloop()