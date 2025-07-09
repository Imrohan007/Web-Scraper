import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
from bs4 import BeautifulSoup

def scrape_links():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        result_box.delete('1.0', tk.END)
        for link in links:
            href = link.get('href')
            text = link.get_text(strip=True)
            if href:
                result_box.insert(tk.END, f'Text: {text or "N/A"}\nURL: {href}\n\n')

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Request Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Simple Web Scraper")

root.geometry("600x500")
root.resizable(False, False)

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Enter URL:").pack(anchor='w')
url_entry = ttk.Entry(frame, width=80)
url_entry.pack(pady=5)

scrape_button = ttk.Button(frame, text="Scrape Links", command=scrape_links)
scrape_button.pack(pady=10)

result_box = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=70, height=20)
result_box.pack(fill=tk.BOTH, expand=True)

root.mainloop()
#https://www.empireonline.com/movies/features/best-movies-2/  #
