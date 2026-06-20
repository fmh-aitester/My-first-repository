from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class MeineApp(App):
    def build(self):
        # Das Hauptlayout der App (vertikal geordnet)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Überschrift und Text
        title = Label(text="Glückwunsch!", font_size='32sp', bold=True, size_hint_y=0.2)
        subtitle = Label(text="Ihre erste FOSS-App läuft.", font_size='18sp', size_hint_y=0.4)
        
        # Der grüne Klick-Button
        btn = Button(text="Hier tippen", font_size='20sp', bold=True, size_hint_y=0.2,
                     background_normal='', background_color=(0.15, 0.65, 0.27, 1)) # Grün
        
        # Funktion für das Pop-up Fenster bei Klick
        def zeige_popup(instance):
            popup_layout = BoxLayout(orientation='vertical', padding=10)
            popup_layout.add(Label(text="Perfekt, der Code funktioniert!"))
            close_btn = Button(text="Schliessen", size_hint_y=0.4)
            popup = Popup(title="Erfolg!", content=popup_layout, size_hint=(0.8, 0.4))
            close_btn.bind(on_release=popup.dismiss)
            popup_layout.add(close_btn)
            popup.open()
            
        btn.bind(on_release=zeige_popup)
        
        # Alles dem Layout hinzufügen
        layout.add(title)
        layout.add(subtitle)
        layout.add(btn)
        
        return layout

if __name__ == '__main__':
    MeineApp().run()
