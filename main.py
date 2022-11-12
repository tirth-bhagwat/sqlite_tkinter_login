import tkinter as tk
import dbManager as db
import signup_window
import user_dashboard

BGCOLOR_002 = "#2c3e50"
FGCOLOR_002 = "#ffffff"
FONTFACE_002 = "Monospace"


def login_002(
    username_002: str, password_002: str, err_label_002: tk.Label = None
) -> bool:

    if not username_002.isalnum():
        if err_label_002 is not None:
            err_label_002.config(
                text="Username cannot be balnk or have spectal characters", fg="orange"
            )
        txt_username_002.focus()
        return False

    if db.get_user_002(username_002) is None:
        if err_label_002 is not None:
            err_label_002.config(text="Invalid username or password", fg="orange")
        txt_username_002.focus()
        return False

    if db.get_user_002(username_002)[3] != password_002:
        if err_label_002 is not None:
            err_label_002.config(text="Invalid username or password", fg="orange")
        txt_password_002.focus()
        return False

    if err_label_002 is not None:
        err_label_002.config(text="")
    user_dashboard.show_002(root_002, username_002)
    return True


root_002 = tk.Tk()
root_002.title("Login")
root_002.geometry("800x600")
root_002.resizable(False, False)
root_002.configure(bg=BGCOLOR_002)

login_frame_002 = tk.Frame(root_002, bg=BGCOLOR_002)

lbl_title_002 = tk.Label(login_frame_002, text="Login")
lbl_title_002.config(font=(FONTFACE_002, 24), fg=FGCOLOR_002, pady=5)
lbl_title_002.configure(bg=BGCOLOR_002)
lbl_title_002.grid(row=0, column=0, columnspan=2)

lbl_username_002 = tk.Label(login_frame_002, text="Username")
lbl_username_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
lbl_username_002.configure(bg=BGCOLOR_002)
lbl_username_002.grid(row=1, column=0)
txt_username_002 = tk.Entry(login_frame_002)
txt_username_002.config(font=(FONTFACE_002, 12))
txt_username_002.grid(row=1, column=1)

lbl_password_002 = tk.Label(login_frame_002, text="Password")
lbl_password_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
lbl_password_002.configure(bg=BGCOLOR_002)
lbl_password_002.grid(row=2, column=0)
txt_password_002 = tk.Entry(login_frame_002, show="•")
txt_password_002.config(font=(FONTFACE_002, 12))
txt_password_002.grid(row=2, column=1)

lbl_error_002 = tk.Label(login_frame_002, text="")
lbl_error_002.config(font=(FONTFACE_002, 12), fg="orange")
lbl_error_002.configure(bg=BGCOLOR_002)
lbl_error_002.grid(row=3, column=0, columnspan=2)

btn_login_002 = tk.Button(
    login_frame_002,
    text="Login",
    command=lambda: login_002(
        txt_username_002.get(), txt_password_002.get(), lbl_error_002
    ),
)
btn_login_002.configure(bg=BGCOLOR_002, fg=FGCOLOR_002)
btn_login_002.grid(row=4, column=0, columnspan=2, pady=5)

btn_signup_002 = tk.Button(
    login_frame_002, text="Signup", command=lambda: signup_window.show_002(root_002)
)
btn_signup_002.configure(bg=BGCOLOR_002, fg=FGCOLOR_002)
btn_signup_002.grid(row=5, column=0, columnspan=2, pady=5)
txt_username_002.focus()

login_frame_002.pack(expand=True)

db.create_tables_002()
root_002.mainloop()
