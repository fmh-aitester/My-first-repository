import tkinter as tk
from tkinter import messagebox

# Erstellt ein echtes, einfaches App-Fenster
root = tk.Tk()
root.title("Meine FOSS App")
root.geometry("400x600")
root.configure(bg='#eef2f3')

# Überschrift
label = tk.Label(root, text="Glückwunsch!", font=("Arial", 24, "bold"), bg='#eef2f3', fg='#333')
label.pack(pady=40)

# Text
text = tk.Label(root, text="Ihre erste eigene App läuft.", font=("Arial", 14), bg='#eef2f3', fg='#666')
text.pack(pady=10)

# Funktion für den Button
def zeige_hinweis():
    messagebox.showinfo("Erfolg", "Perfekt, der Code funktioniert!")

# Grüner Button
btn = tk.Button(root, text="Hier tippen", font=("Arial", 14, "bold"), bg='#28a745', fg='white', 
                padx=20, pady=10, borderwidth=0, command=zeige_hinweis)
btn.pack(pady=40)

if __name__ == '__main__':
    root.mainloop()
