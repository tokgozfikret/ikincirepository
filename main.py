import tkinter as tk
from kocluk_gui import KoclukUygulamasi  # GUI sını

if __name__ == "__main__":
    root = tk.Tk()
    app = KoclukUygulamasi(root)  # GUI sınıfını başlatıyoruz
    root.mainloop()
