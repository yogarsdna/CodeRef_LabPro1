import tkinter as tk
import socket
import threading
from time import sleep

#Initialize server
server = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 9090

#Initialize variables that will be used
client_name = " "
clients = []
clients_names = []
player_data = []

#initialize frame
window = tk.Tk()
window.title("Server")

#Top frame
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Start", foreground="blue", command=lambda : start_server())
btnStart.pack(side=tk.LEFT)
btnStart.configure(fg="blue")
btnStop = tk.Button(topFrame, text="Stop", foreground="red", command=lambda : stop_server(), state=tk.DISABLED)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

#Middle frame
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text = "Address: X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text = "Port:XXXX")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

#The client frame
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text=">>>>>>>>>> Client List <<<<<<<<<<").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(clientFrame, height=10, width=30)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#9dc1cd", highlightbackground="grey", state="disabled")
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))

#Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT 
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)

    threading._start_new_thread(accept_clients, (server, " "))

    lblHost["text"] = "Address: " + HOST_ADDR
    lblPort["text"] = "Port: " + str(HOST_PORT)

#Stop server function
def stop_server():
    global server, clients, clients_names

    # Send shutdown message to each client
    shutdown_message = "SERVER_SHUTDOWN"
    for client in clients:
        try:
            client.send(shutdown_message.encode())
            client.close()
        except:
            pass

    # Clear the client lists
    clients.clear()
    clients_names.clear()

    # Close the server socket
    server.close()

    # Close the GUI window
    window.destroy()

#Accept client requests
client_threads = []

def accept_clients(the_server, y):
    while True:
        if len(clients) < 2:
            client, addr = the_server.accept()
            clients.append(client)

            # Use a thread to handle the client connection
            client_thread = threading.Thread(target=send_receive_client_message, args=(client, addr))
            client_thread.start()

            # Store the thread object
            client_threads.append(client_thread)

def send_opponent_name(client, opponent_name):
    client.send(("opponent_name$" + opponent_name).encode())

def send_data(socket, data):
    socket.send(data.encode())

def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, player_data, player0, player1

    client_msg = " "

    # Send welcome message to client
    client_name = client_connection.recv(4096).decode()
    if len(clients) < 2:
        client_connection.send("welcome1".encode())
    else:
        client_connection.send("welcome2".encode())

    clients_names.append(client_name)
    update_client_names_display(clients_names)
    
    if len(clients) > 1:
        sleep(1)

        # Send opponent name
        send_opponent_name(clients[0], clients_names[1])
        send_opponent_name(clients[1], clients_names[0])

    while True:
        try:
            data = client_connection.recv(4096).decode()
        except ConnectionAbortedError:
            break

        if not data:
            break

        # Get the player choice from received data
        player_choice = data[11:]

        msg = {
            "choice": player_choice,
            "socket": client_connection
        }

        if len(player_data) < 2:
            player_data.append(msg)

        if len(player_data) == 2:
            # Send player 1 choice to player 2 and vice versa
            dataToSend0 = "$opponent_choice" + player_data[1].get("choice")
            dataToSend1 = "$opponent_choice" + player_data[0].get("choice")
            
            player0_socket = player_data[0].get("socket")
            player1_socket = player_data[1].get("socket")

            send_data(player0_socket, dataToSend0)
            send_data(player1_socket, dataToSend1)

            player_data = []

    # Find the client index then remove from both lists
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]

    # Find the thread index then remove from the list
    thread_idx = get_client_index(client_threads, threading.current_thread())
    del client_threads[thread_idx]

    # Close the client connection
    client_connection.close()

    update_client_names_display(clients_names)

def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx

def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, c+"\n")
    tkDisplay.config(state=tk.DISABLED)

window.mainloop()