import os
from kivy.app import App
from kivy.uix.webview import WebView # Unterstützt Android Webansichten

class WebApp(App):
    def build(self):
        # Startet direkt die index.html, die wir vorhin erstellt haben
        return WebView(url="file://" + os.path.abspath("index.html"))

if __name__ == '__main__':
    WebApp().run()

