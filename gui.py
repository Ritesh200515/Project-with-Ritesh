from tkinter import *
from PIL import Image, ImageTk

# ------------------ ROOT WINDOW ------------------
root = Tk()
root.title("AI Assistant")
root.geometry("600x700")
root.resizable(False, False)
root.config(bg="#2c3e50")   # Dark background

# ------------------ MAIN FRAME ------------------
frame = LabelFrame(root, padx=20, pady=20, borderwidth=3, relief="raised", bg="white")
frame.pack(pady=20)

# ------------------ TITLE ------------------
text_label = Label(
    frame,
    text="AI Assistant",
    font=("Comic Sans MS", 18, "bold"),
    bg="black",
    fg="white",
    width=20
)
text_label.pack(pady=10)

# ------------------ IMAGE ------------------
img = Image.open("robot.png")     # Make sure robot.png is in same folder
img = img.resize((200, 200))      # Resize image
image = ImageTk.PhotoImage(img)

image_label = Label(frame, image=image, bg="white")
image_label.image = image
image_label.pack(pady=10)

# ------------------ CHAT DISPLAY ------------------
chat_box = Text(root, height=10, width=60, font=("Arial", 11))
chat_box.pack(pady=10)
chat_box.insert(END, "Assistant: Hello Hrithik! 👋\n")

# ------------------ USER INPUT FRAME ------------------
input_frame = Frame(root, bg="#2c3e50")
input_frame.pack(pady=10)

user_input = Entry(input_frame, width=40, font=("Arial", 12))
user_input.grid(row=0, column=0, padx=10)

# ------------------ SEND FUNCTION ------------------
def send_message():
    message = user_input.get()
    if message.strip() != "":
        chat_box.insert(END, f"You: {message}\n")
        chat_box.insert(END, "Assistant: I am still learning 🤖\n\n")
        user_input.delete(0, END)

# ------------------ SEND BUTTON ------------------
send_button = Button(
    input_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    bg="#3498db",
    fg="white",
    command=send_message
)
send_button.grid(row=0, column=1)

# ------------------ MAIN LOOP ------------------
root.mainloop()






root.mainloop()
