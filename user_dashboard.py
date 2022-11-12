import tkinter as tk
import dbManager as db

BGCOLOR_002 = "#2c3e50"
FGCOLOR_002 = "#ffffff"
FONTFACE_002 = "Monospace"


def show_002(root_002: tk.Tk, username_002: str) -> None:
    
    dashboard_002 = tk.Toplevel(root_002)
    dashboard_002.title("Dashboard")
    dashboard_002.geometry("800x600")
    dashboard_002.resizable(False, False)
    dashboard_002.configure(bg=BGCOLOR_002)

    dashboard_frame_002 = tk.Frame(dashboard_002, bg=BGCOLOR_002)

    user_002 = db.get_user_002(username_002)
    if user_002 is None:
        return

    title_002 = tk.Label(dashboard_frame_002, text="Welcome " + user_002[1])
    title_002.config(font=(FONTFACE_002, 24), fg=FGCOLOR_002, pady=10)
    title_002.configure(bg=BGCOLOR_002)
    title_002.grid(row=0, column=0, columnspan=2)

    lbl_username_002 = tk.Label(dashboard_frame_002, text="Username")
    lbl_username_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
    lbl_username_002.configure(bg=BGCOLOR_002)
    lbl_username_002.grid(row=1, column=0)
    txt_username_002 = tk.Label(dashboard_frame_002, text=user_002[2])
    txt_username_002.config(font=(FONTFACE_002, 12))
    txt_username_002.grid(row=1, column=1)

    lbl_email_002 = tk.Label(dashboard_frame_002, text="Email")
    lbl_email_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
    lbl_email_002.configure(bg=BGCOLOR_002)
    lbl_email_002.grid(row=2, column=0)
    txt_email_002 = tk.Label(dashboard_frame_002, text=user_002[5])
    txt_email_002.config(font=(FONTFACE_002, 12))
    txt_email_002.grid(row=2, column=1)

    lbl_address_002 = tk.Label(dashboard_frame_002, text="Address")
    lbl_address_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
    lbl_address_002.configure(bg=BGCOLOR_002)
    lbl_address_002.grid(row=3, column=0)
    txt_address_002 = tk.Text(dashboard_frame_002, height=5, width=30)
    txt_address_002.insert(tk.END, user_002[4])
    txt_address_002.config(
        font=(FONTFACE_002, 12), width=30, height=5, state="disabled"
    )
    txt_address_002.grid(row=3, column=1)

    dashboard_frame_002.pack(expand=True)
    dashboard_002.mainloop()
