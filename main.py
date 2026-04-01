import tkinter as tk
from scraper import NewsScraper
from gui import NewsGUI

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.scraper = NewsScraper()
        # Pass the refresh logic to the GUI
        self.gui = NewsGUI(self.root, self.refresh_data)
        
    def refresh_data(self):
        # 1. Fetch data from scraper
        bbc_news = self.scraper.fetch_bbc_tech()
        reuters_news = self.scraper.fetch_reuters_tech()
        
        combined_news = bbc_news + reuters_news
        
        # 2. Tell GUI to show the data
        if combined_news:
            self.gui.display_data(combined_news)
        else:
            print("No news found.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
    app.run()