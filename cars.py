import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from PIL import Image, ImageTk

car_brand_images = {
    'Toyota': r'C:\Users\Administrator\Documents\cars\Brands\Toyota.png',
    'Mitsubishi': r'C:\Users\Administrator\Documents\cars\Brands\Mitsubishi.png',
    'Honda': r'C:\Users\Administrator\Documents\cars\Brands\Honda.png',
    'Nissan': r'C:\Users\Administrator\Documents\cars\Brands\nissan.png',
}

car_model_images_Toyota = {
    'Supra': r'C:\Users\Administrator\Documents\cars\Models\Toyota\Supra\image1.jpg',
    '86': r'C:\Users\Administrator\Documents\cars\Models\Toyota\86\image1.jpg',
}

car_model_images_Mitsubishi = {
    'Eclipse': r'C:\Users\Administrator\Documents\cars\Models\Mitsubishi\Eclipse\image1.jpg',
}

car_model_images_Honda = {
    'Civic': r'C:\Users\Administrator\Documents\cars\Models\Honda\Civic\image1.jpg',
}

car_model_images_Nissan = {
    'R34': r'C:\Users\Administrator\Documents\cars\Models\Nissan\R34\image1.jpg',
}

root = tk.Tk()
root.title("Car Selection")

root.resizable(False, False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


x = (screen_width / 2) - (800 / 2)  
y = (screen_height / 2) - (600 / 2)  

root.geometry(f'800x600+{int(x)}+{int(y)}')

current_brand_choice = None

model_image_label = None

user_balance = 0

def deposit_cash():
    global user_balance
    deposit_amount = simpledialog.askinteger("Deposit Cash", "Enter the deposit amount:")
    if deposit_amount is not None and deposit_amount > 0:
        user_balance += deposit_amount
        messagebox.showinfo("Deposit Successful", f"₱{deposit_amount} deposited successfully. Your new balance is ₱{user_balance}.")
        update_balance_label()


def display_car_brand_image(brand_choice):
    brand_image_path = car_brand_images.get(brand_choice, r'C:\Users\Administrator\Documents\cars\default_image.jpg')
    brand_image = Image.open(brand_image_path)
    brand_image.thumbnail((200, 200))  
    brand_image = ImageTk.PhotoImage(brand_image)
    brand_image_label.config(image=brand_image)
    brand_image_label.image = brand_image


def display_car_model_image(model_choice):
    default_model_image_path = r'C:\Users\Administrator\Documents\cars\Models\default_image.jpg'
    if current_brand_choice == 'Toyota':
        model_image_path = car_model_images_Toyota.get(model_choice, default_model_image_path)
    elif current_brand_choice == 'Mitsubishi':
        model_image_path = car_model_images_Mitsubishi.get(model_choice, default_model_image_path)
    elif current_brand_choice == 'Honda':
        model_image_path = car_model_images_Honda.get(model_choice, default_model_image_path)
    elif current_brand_choice == 'Nissan':
        model_image_path = car_model_images_Nissan.get(model_choice, default_model_image_path)
    model_image = Image.open(model_image_path)
    model_image.thumbnail((300, 300))  # Resize the image if necessary
    model_image = ImageTk.PhotoImage(model_image)
    model_image_label.config(image=model_image)
    model_image_label.image = model_image
   
def select_model_window(brand_choice):
    def on_model_selected(event):
        model_choice = model_combobox.get()
        display_car_model_image(model_choice)
        display_car_info(brand_choice, model_choice)  

    model_window = tk.Toplevel(root)
    model_window.title("Select a Car Model")

    x_model = (screen_width / 2) - (400 / 2)  
    y_model = (screen_height / 2) - (300 / 2) 

    model_window.geometry(f'400x300+{int(x_model)}+{int(y_model)}')

    model_label = ttk.Label(model_window, text="Select a Car Model:")
    model_label.pack()

    if brand_choice == 'Toyota':
        model_combobox = ttk.Combobox(model_window, values=list(car_model_images_Toyota.keys()))
    elif brand_choice == 'Mitsubishi':
        model_combobox = ttk.Combobox(model_window, values=list(car_model_images_Mitsubishi.keys()))
    elif brand_choice == 'Honda':
        model_combobox = ttk.Combobox(model_window, values=list(car_model_images_Honda.keys()))
    elif brand_choice == 'Nissan':
        model_combobox = ttk.Combobox(model_window, values=list(car_model_images_Nissan.keys()))
    model_combobox.pack()

    model_combobox.bind("<<ComboboxSelected>>", on_model_selected)

    global model_image_label  
    model_image_label = ttk.Label(model_window)
    model_image_label.pack()

def display_car_info(brand_choice, model_choice):
    car_info = {
        'Toyota': {
            'Supra': {
                'Manufacturer': 'Toyota',
                'Model': 'Supra',
                'Year': '1993',
                'Price': '₱6,500,000',
                'Top Speed': '155 mph',
                'Engine': '2JZ-GTE Twin turbo',
                'Transmission': 'Manual, 6 speed',
            },
            '86': {
                'Manufacturer': 'Toyota',
                'Model': '86',
                'Year': '2014',
                'Price': '₱1,200,000',
                'Top Speed': '140 mph',
                'Engine and Transmission': '2.0L Boxer',
                 'Transmission': 'Automatic, 5 speed',
            },   
        },
        'Mitsubishi': {
            'Eclipse': {
                'Manufacturer': 'Mitsubishi',
                'Model': 'Eclipse',
                'Year': '1998',
                'Price': '₱250,000',
                'Top Speed': '135 mph',
                'Engine and Transmission': '4G63T Stock Turbo ',
                'Transmission': 'Manual, 5 speed',
            },
        },
        'Honda': {
            'Civic': {
                'Manufacturer': 'Honda',
                'Model': 'Civic LXI',
                'Year': '2000',
                'Price': '₱160,000',
                'Top Speed': '130 mph',
                'Engine and Transmission': 'LXI Soch Non Vtec 1.8L 4 Cyl',
                'Transmission': 'Manual, 5 speed',
            },
        },
        'Nissan': {
            'R34': {
                'Manufacturer': 'Nissan',
                'Model': 'Skyline GT-R R34',
                'Year': '1999',
                'Price': '₱2,000,000',
                'Top Speed': '155 mph',
                'Engine and Transmission': 'RB26DETT Twin Turbo',
                'Transmission': 'Manual, 6 speed',
            },
        }
    }

    info_window = tk.Toplevel(root)
    info_window.title("Car Information")

    x_info = (screen_width / 2) - (400 / 2)  
    y_info = (screen_height / 2) - (300 / 2)  

    info_window.geometry(f'400x300+{int(x_info)}+{int(y_info)}')

    car_info_text = ""
    if brand_choice in car_info and model_choice in car_info[brand_choice]:
        model_info = car_info[brand_choice][model_choice]
        car_info_text = "\n".join([f"{key}: {value}" for key, value in model_info.items()])

    info_label = ttk.Label(info_window, text=car_info_text)
    info_label.pack()

def on_brand_selected(event):
    global current_brand_choice
    current_brand_choice = brand_combobox.get()
    display_car_brand_image(current_brand_choice)
    next_button.config(state=tk.NORMAL)  


def update_balance_label():
    balance_label.config(text=f'Balance: ₱{user_balance}')

balance_label = ttk.Label(root, text=f'Balance: ₱{user_balance}')
balance_label.pack()

deposit_button = ttk.Button(root, text="Deposit Cash", command=deposit_cash)
deposit_button.pack()




brand_label = ttk.Label(root, text="Select a Car Brand:")
brand_label.pack()

brand_combobox = ttk.Combobox(root, values=list(car_brand_images.keys()))
brand_combobox.pack()
brand_combobox.bind("<<ComboboxSelected>>", on_brand_selected)
next_button = ttk.Button(root, text="Exit", command=root.destroy)
next_button.pack(pady=20)

brand_image_label = ttk.Label(root)
brand_image_label.pack()

next_button = ttk.Button(root, text="Next", state=tk.DISABLED, command=lambda: select_model_window(current_brand_choice))
next_button.pack()


root.mainloop()



