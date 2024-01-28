import smtplib
import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("My Email App")
window.config(padx=50, pady=50)


def send_email():
    my_email = "your_email@gmail.com"
    password = "your email app password"
    target_email = email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tkinter.END)

    if len(target_email) == 0 or len(subject) == 0 or len(message) == 0:
        messagebox.showinfo(title="Error", message="Please enter data")
    else:
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # name of the mail provider
                connection.starttls()  # this enables encryption in our mail
                connection.login(user=my_email, password=password)

                # Send the email
                connection.sendmail(from_addr=my_email, to_addrs=target_email,
                                    msg=f"Subject:{subject}\n\n{message}")
                messagebox.showinfo(title="Email Send", message=f"Email send to {target_email}")

                email_entry.delete(0, tkinter.END)
                subject_entry.delete(0, tkinter.END)
                message_text.delete("1.0", tkinter.END)
        except smtplib.SMTPRecipientsRefused:
            messagebox.showinfo(title="email error", message=f"{target_email} is not valid email address")
            email_entry.delete(0, tkinter.END)
            subject_entry.delete(0, tkinter.END)
            message_text.delete("1.0", tkinter.END)
            send_email()


# Email Label
email_label = tkinter.Label(text="Email: ", width=8)
email_label.grid(row=0, column=0)
# Email entry
email_entry = tkinter.Entry(width=30)
email_entry.grid(row=0, column=1)
email_entry.focus()

# subject label
subject_label = tkinter.Label(text="Subject: ", width=8)
subject_label.grid(row=1, column=0)
# subject entry
subject_entry = tkinter.Entry(width=30)
subject_entry.grid(row=1, column=1)

# message_label
message_label = tkinter.Label(text="Message: ", width=8)
message_label.grid(row=2, column=0)

# message_text
message_text = tkinter.Text(height=8, width=40)
message_text.grid(row=2, column=1)

# Send Button
send_button = tkinter.Button(text="Send", width=20, command=send_email)
send_button.grid(row=3, column=1)

window.mainloop()
