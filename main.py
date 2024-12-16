import csv
from os import path,system
import sys
from pyperclip import copy
from random import randrange
from rich.theme import Theme
from rich.console import Console
from rich.table import Table
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from time import sleep

custom_theme = Theme({
    "success": "green",
    "error": "bold red"
})

console = Console(theme=custom_theme)
    
def create_db_files():
    if not path.exists("passworddb.csv"):
        with open("passworddb.csv", 'w', newline='') as db:
            writer = csv.writer(db)
            writer.writerow(["SERIAL NO", "WEBSITE/APP NAME", "WEBSITE/APP LINK", "NOTE", "PASSWORD"])
            db.flush()

def animate(text: str):
    for token in text:
        sys.stdout.write(token)
        sys.stdout.flush()
        sleep(0.1)
    return input()

def start_animation():
    system('cls')
    
    for i in range(13):
        print(" || ")
    
    sleep(0.5)
    system('cls')

    print(" ||=============")
    print(" ||             \\ ")
    print(" ||              \\ ")
    print(" ||               |")
    print(" ||              /")
    print(" ||             /")
    print(" ||=============")

    for i in range(6):
        print(" || ")

    sleep(0.5)
    system('cls')

    print(" ||==============             || ")
    print(" ||              \\            || ")
    print(" ||               \\           || ")
    print(" ||                |          || ")
    print(" ||               /           || ")
    print(" ||              /            || ")
    print(" ||=============              || ")

    for i in range(6):
        print(" ||                           || ")

    sleep(0.5)
    system('cls')
    print(" ||=============              ||============= ")
    print(" ||             \\             ||             \\ ")
    print(" ||              \\            ||              \\ ")
    print(" ||               |           ||               |")
    print(" ||              /            ||              /")
    print(" ||             /             ||             /")
    print(" ||=============              || ===========")
    print(" ||                           ||             \\ ")
    print(" ||                           ||              \\ ")
    print(" ||                           ||               |")
    print(" ||                           ||              /")
    print(" ||                           ||             /")
    print(" ||                           ||============ ")    

    sleep(0.5)
    system('cls')
    print(" ||=============              ||=============                        ")
    print(" ||             \\             ||             \\                       ")
    print(" ||              \\            ||              \\                      ")
    print(" ||               |           ||               |                     ")
    print(" ||              /            ||              /                      ")
    print(" ||             /             ||             /                       ")
    print(" ||=============              || ===========                         ")
    print(" ||                           ||             \\                        ")
    print(" ||                           ||              \\                       ")
    print(" ||                           ||               |                  ")
    print(" ||                           ||              /                 ")
    print(" ||                           ||             /        \\  /       ")
    print(" ||                           ||============           \\/       ")    

    sleep(0.5)
    system('cls')

    print(" ||=============              ||=============                        ")
    print(" ||             \\             ||             \\                       ")
    print(" ||              \\            ||              \\                      ")
    print(" ||               |           ||               |                     ")
    print(" ||              /            ||              /                      ")
    print(" ||             /             ||             /                       ")
    print(" ||=============              || ===========                         ")
    print(" ||                           ||             \\                        ")
    print(" ||                           ||              \\                       ")
    print(" ||                           ||               |                   ___   ")
    print(" ||                           ||              /              |    |   |    ")
    print(" ||                           ||             /         \\  /  |    |   |      ")
    print(" ||                           ||============            \\/   | O  |___|      ")    

    sleep(1)
    animate("\nYou are using Password Buddy v1.0\n~Developed by Shaunak N \n(Press 'Enter' to continue..)")
    system('cls')
    return
    
def help_message():
    help_msg = """\n
    0) Clear the screen
    1) View all your stored passwords
    2) Add a new password
    3) Delete an existing entry
    4) Edit an existing entry  
    5) Copy a password
    6) Generate a random password
    7) Mail yourself the password database
    8) Open this Menu
    9) Exit the app 
    """

    print(help_msg)

def adjust_serial_numbers():
    if path.exists("passworddb.csv"):
        with open("passworddb.csv", 'r', newline='') as db:
            reader = csv.reader(db)
            rows = list(reader)
        
        for i in range(1, len(rows)):
            rows[i][0] = str(i)  
        
        with open("passworddb.csv", 'w', newline='') as db:
            writer = csv.writer(db)
            writer.writerows(rows)
        
        console.print("Serial numbers have been adjusted.", style='success')
    else:
        console.print("No password database found.", style='error')

def get_next_serial_number():
    """Get the next serial number based on existing entries."""
    if path.exists("passworddb.csv"):
        with open("passworddb.csv", 'r', newline='') as db:
            reader = csv.reader(db)
            next(reader) 
            rows = list(reader)
            return len(rows) + 1  
    return 1  

def mail_pass():
    msg = MIMEMultipart()
    msg['From'] = 'Mail ID'
    msg['To'] = animate("Enter your email id(csv file will be sent to this email): ")
    msg['Subject'] = 'Your Passwords'
    body = 'from Password Buddy 1.0'
    msg.attach(MIMEText(body))
    filename = 'passworddb.csv'
    
    with open(filename, 'rb') as f:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f.read())
        attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)
        msg.attach(attachment)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login('Mail ID', 'App Password')
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()
    console.print("Email sent successfully!",style='success')

def read_option(value):
    if value == 0:
        option = input("\nEnter the serial number of the command (8 for Menu, 0 to clear screen): ")
    else:
        option = input("\nEnter the corresponding serial number of the password: ")

    try:
        return int(option) 
    except ValueError:
        console.print("Invalid input. Please enter a valid number.", style="error")
        return None  

def copy_pass():
    serial_no = read_option(1)
    if isinstance(serial_no, int):

        with open("passworddb.csv", 'r', newline='') as db:
            reader = csv.reader(db)
            next(reader) 
            rows = list(reader)  
            
            if serial_no > 0 and serial_no <= len(rows):

                row = rows[serial_no - 1]  
                app_name = row[1] 
                copy(row[4])  
                console.print(f"Password for {app_name} copied to the clipboard!", style="success")    
            else:
                console.print("Enter a valid number!", style="error")          
        
    else:
        console.print("Try again using a valid number",style="error")
        
def generate_pass(length):
    try:
        length = int(length) 
        if 15 <= length <= 100:
            password = ""
            chars = "=!@#$%^&*()1234567890abcdefghijklmnopqrstuvwxyz=!%@#$^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ=!%@#$^&*()"
            for i in range(length):
                password += chars[randrange(0, len(chars))]
            print(password)
            copy(password)
            print("Copied to clipboard")
        else:
            print("Password length must be from 15 to 100.")
    except ValueError:
        print("Invalid input.")

    
def showall():
    table = Table(title="Your Passwords")
    
    table.add_column("Sr. No.", style="magenta")
    table.add_column("App/User Name", justify="right", style="cyan", no_wrap=True)
    table.add_column("Link", justify="right", style="green")
    table.add_column("Note", style="magenta")
    table.add_column("Password", style="magenta")
    
    print("\n")
    with open("passworddb.csv", 'r', newline='') as db:
        reader = csv.reader(db)
        next(reader)
        for row in reader:
            table.add_row(row[0], row[1], row[2], row[3], row[4])

    console.print(table)
    
def addnew():
    app_name = input("\nEnter Website / App name (mandatory): ")
    app_link = input("\nEnter Website / App Link (optional): ")
    note = input("\nLeave a Note (optional): ")
    password = input("\nEnter your Password: ")
    
    serial_no = get_next_serial_number() 
    
    try:
        with open("passworddb.csv", 'a', newline='') as db:
            writer = csv.writer(db)
            writer.writerow([serial_no, app_name, app_link, note, password])

        console.print("Password Added Successfully!", style='success')
        adjust_serial_numbers()
        
    except Exception as e:
        print(f"Error writing to file: {e}")

def delete():
    showall() 

    serial_no = int(input("\nEnter the Serial No of the entry to delete: "))
    rows = []
    found = False
        
    with open("passworddb.csv", 'r', newline='') as db:
        reader = csv.reader(db)
        rows = list(reader)

    with open("passworddb.csv", 'w', newline='') as db:
        writer = csv.writer(db)
        writer.writerow(rows[0])  
        for row in rows[1:]:
            if int(row[0]) != serial_no:  
                writer.writerow(row)
            else:
                found = True
        
    if found:
        console.print(f"Entry with Serial No {serial_no} deleted successfully.", style='success')
        adjust_serial_numbers()
    else:
        console.print(f"No entry found with Serial No {serial_no}.", style='error')

def edit():
    showall()  
    try:
        serial_no = int(input("\nEnter the Serial No of the entry to edit: "))
        rows = []
        found = False
        
        with open("passworddb.csv", 'r', newline='') as db:
            reader = csv.reader(db)
            rows = list(reader)

        for i in range(1, len(rows)):
            if int(rows[i][0]) == serial_no: 
                found = True
                app_name = input(f"Enter new Website/App name (leave blank to keep '{rows[i][1]}'): ") or rows[i][1]
                app_link = input(f"Enter new Website/App Link (leave blank to keep '{rows[i][2]}'): ") or rows[i][2]
                note = input(f"Leave a new Note (leave blank to keep '{rows[i][3]}'): ") or rows[i][3]
                password = input(f"Enter new Password (leave blank to keep it): ") or rows[i][4]
                
                rows[i] = [serial_no, app_name, app_link, note, password] 
                
                # break

        if found:
            with open("passworddb.csv", 'w', newline='') as db:
                writer = csv.writer(db)
                writer.writerow(rows[0])
                for row in rows[1:]:
                    writer.writerow(row)
            
            db.flush()
            
            console.print(f"Entry No. {serial_no} updated successfully.",style="success")
            adjust_serial_numbers()
        else:
            print(f"No entry found with Serial No {serial_no}.", style="error")
        
    except Exception as e:
        print(f"Error editing entry: {e}")

def main():
    create_db_files()
    help_message()
    
    while True:
        option = read_option(0)
        if option is None:  
            continue
        
        if option == 0:
            system('cls')
        elif option == 1:
            showall()
        elif option == 2:
            addnew()
        elif option == 3:
            delete()
        elif option == 4:
            edit()
        elif option == 5:
            copy_pass()
        elif option == 6:
            length = input("\nEnter password length (15 to 100): ")
            generate_pass(length)
        elif option == 7:
            mail_pass()
        elif option == 8:
            help_message()
        elif option == 9:
            sys.exit(0)
        else:
            console.print("Enter a option!", style="error") 


if __name__ == "__main__":
    start_animation()
    main()
