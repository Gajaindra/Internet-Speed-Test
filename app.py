import tkinter as tk
import speedtest


def speedcheck():
    try:
        status_label.config(text="Testing...", fg="orange")
        root.update()

        st = speedtest.Speedtest()
        st.get_best_server()

        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000

        download_label.config(text=f"{download:.2f} Mbps")
        upload_label.config(text=f"{upload:.2f} Mbps")

        status_label.config(text="Test completed", fg="green")

    except Exception as e:
        status_label.config(text="Speed test failed", fg="red")
        download_label.config(text="--")
        upload_label.config(text="--")


# Main window
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#f2f2f2")


# Title
title = tk.Label(
    root,
    text="Internet Speed Test",
    font=("Arial", 28, "bold"),
    bg="#f2f2f2",
    fg="#222222"
)
title.pack(pady=35)


# Download section
tk.Label(
    root,
    text="Download Speed",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2"
).pack(pady=(20, 5))

download_label = tk.Label(
    root,
    text="--",
    font=("Arial", 26, "bold"),
    bg="#f2f2f2",
    fg="#1976D2"
)
download_label.pack()


# Upload section
tk.Label(
    root,
    text="Upload Speed",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2"
).pack(pady=(30, 5))

upload_label = tk.Label(
    root,
    text="--",
    font=("Arial", 26, "bold"),
    bg="#f2f2f2",
    fg="#388E3C"
)
upload_label.pack()


# Status
status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 13),
    bg="#f2f2f2",
    fg="#555555"
)
status_label.pack(pady=25)


# Button
button = tk.Button(
    root,
    text="CHECK SPEED",
    font=("Arial", 16, "bold"),
    bg="#2196F3",
    fg="white",
    padx=30,
    pady=10,
    cursor="hand2",
    command=speedcheck
)
button.pack()


root.mainloop()