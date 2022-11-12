import tkinter as tk
from tkinter import messagebox
import dbManager as db

BGCOLOR_002 = "#2c3e50"
FGCOLOR_002 = "#ffffff"
FONTFACE_002 = "Monospace"


def show_002(root: tk.Tk) -> None:
    def validate_signup_form_002() -> bool:
        if any(
            [
                txt_name_002.get() == "",
                txt_address_002.get("1.0", "end") == "",
                txt_email_002.get() == "",
                txt_username_002.get() == "",
                txt_password_002.get() == "",
                txt_confirm_password_002.get() == "",
            ]
        ):
            lbl_error_002.config(text="All fields are mandatory", fg="orange")
            return False

        if db.get_user_002(txt_username_002.get()) is not None:
            lbl_error_002.config(text="Username already exists", fg="orange")
            lbl_username_002.focus()
            return False

        if txt_password_002.get() != txt_confirm_password_002.get():
            lbl_error_002.config(text="Passwords do not match", fg="orange")
            txt_confirm_password_002.focus()
            return False

        db.insert_user_002(
            txt_name_002.get(),
            txt_username_002.get(),
            txt_password_002.get(),
            txt_address_002.get("1.0", "end"),
            txt_email_002.get(),
        )
        lbl_error_002.config(text="")

        messagebox.showinfo("Success", "User created successfully",parent = signup_window_002)
        signup_window_002.destroy()
        return True

    signup_window_002 = tk.Toplevel(root)
    signup_window_002.title("Signup")
    signup_window_002.geometry("800x600")
    signup_window_002.resizable(False, False)
    signup_window_002.configure(bg=BGCOLOR_002)

    frame_002 = tk.Frame(signup_window_002)
    frame_002.configure(bg=BGCOLOR_002)

    lbl_title_002 = tk.Label(frame_002, text="Signup")
    lbl_title_002.config(font=(FONTFACE_002, 24), fg=FGCOLOR_002, pady=5)
    lbl_title_002.configure(bg=BGCOLOR_002)
    lbl_title_002.grid(row=0, column=0, columnspan=2)

    lbl_name_002 = tk.Label(frame_002, text="Name")
    lbl_name_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
    lbl_name_002.configure(bg=BGCOLOR_002)
    lbl_name_002.grid(row=1, column=0, sticky="e")

    txt_name_002 = tk.Entry(frame_002, width=30)
    txt_name_002.config(font=(FONTFACE_002, 12))
    txt_name_002.grid(row=1, column=1, sticky="w")

    lbl_email_002 = tk.Label(frame_002, text="Email")
    lbl_email_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
    lbl_email_002.configure(bg=BGCOLOR_002)
    lbl_email_002.grid(row=2, column=0, sticky="e")

    txt_email_002 = tk.Entry(frame_002, width=30)
    txt_email_002.config(font=(FONTFACE_002, 12))
    txt_email_002.grid(row=2, column=1, sticky="w")

    lbl_address_002 = tk.Label(frame_002, text="Address")
    lbl_address_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
    lbl_address_002.configure(bg=BGCOLOR_002)
    lbl_address_002.grid(row=3, column=0, sticky="e")

    txt_address_002 = tk.Text(frame_002, height=5, width=30)
    txt_address_002.config(font=(FONTFACE_002, 12))
    txt_address_002.grid(row=3, column=1, sticky="w", pady=5)

    lbl_username_002 = tk.Label(frame_002, text="Username")
    lbl_username_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
    lbl_username_002.configure(bg=BGCOLOR_002)
    lbl_username_002.grid(row=4, column=0, sticky="e")

    txt_username_002 = tk.Entry(frame_002, width=30)
    txt_username_002.config(font=(FONTFACE_002, 12))
    txt_username_002.grid(row=4, column=1, sticky="w")

    lbl_password_002 = tk.Label(frame_002, text="Password")
    lbl_password_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7)
    lbl_password_002.configure(bg=BGCOLOR_002)
    lbl_password_002.grid(row=5, column=0, sticky="e")

    txt_password_002 = tk.Entry(frame_002, show="•", width=30)
    txt_password_002.config(font=(FONTFACE_002, 12))
    txt_password_002.grid(row=5, column=1, sticky="w")

    lbl_confirm_password_002 = tk.Label(frame_002, text="Confirm Password")
    lbl_confirm_password_002.config(
        font=(FONTFACE_002, 12), fg=FGCOLOR_002, pady=5, padx=7
    )
    lbl_confirm_password_002.configure(bg=BGCOLOR_002)
    lbl_confirm_password_002.grid(row=6, column=0, sticky="e")

    txt_confirm_password_002 = tk.Entry(frame_002, show="•", width=30)
    txt_confirm_password_002.config(font=(FONTFACE_002, 12))
    txt_confirm_password_002.grid(row=6, column=1, sticky="w")

    lbl_error_002 = tk.Label(frame_002, text="")
    lbl_error_002.config(font=(FONTFACE_002, 12), fg=FGCOLOR_002)
    lbl_error_002.configure(bg=BGCOLOR_002)
    lbl_error_002.grid(row=7, column=0, columnspan=2)

    btn_register = tk.Button(
        frame_002, text="Register", command=validate_signup_form_002
    )
    btn_register.configure(bg=BGCOLOR_002, fg=FGCOLOR_002)
    btn_register.grid(row=8, column=0, columnspan=2, pady=7)

    txt_name_002.focus()
    frame_002.pack(expand=True)
    signup_window_002.mainloop()
