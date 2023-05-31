import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import socket
import threading

# Function to handle receiving messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            output_text.insert(tk.END, message + "\n")
        except OSError:
            break

# Function to send messages to the server
def send_message():
    message = input_text.get()
    client_socket.send(message.encode('utf-8'))
    output_text.insert(tk.END, "You: " + message + "\n")
    input_text.delete(0, tk.END)

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 5000)
client_socket.connect(server_address)

# Create a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

root = tk.Tk()
root.title("Chat Application")

# Create a scrolled text widget to display the conversation
output_text = ScrolledText(root, width=50, height=20)
output_text.pack()

# Create an entry widget for user input
input_text = tk.Entry(root, width=50)
input_text.pack()
input_text.focus()

# Create a button to send the message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()

# Close the socket connection when the GUI window is closed
client_socket.close()
