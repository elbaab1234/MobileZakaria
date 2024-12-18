from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDFloatingActionButton
import webbrowser
from kivy.core.window import Window

KV = '''
MDScreenManager:
    MDScreen:
        name: "screen 0"
        BoxLayout:
            orientation: 'vertical'
            padding:20
            spacing:20
            MDFloatingActionButton:
                icon: "language-python"
                size_hint: 1, 0.4
                pos_hint: {'center_x':0.5}
                md_bg_color: app.theme_cls.primary_color
            MDLabel:
                text:'Langage Python'
                size_hint: 1, 0.5
                halign: "center"
                theme_text_color: "Primary"
                font_style:"H4"
                pos_hint: {'center_x': 0.5}
            MDFillRoundFlatIconButton:
                size_hint: 1, 0.1
                text: "Entrer"
                font_size: 22
                pos_hint: {"center_x": .5}
                on_release:
                    root.current = "screen A"

    MDScreen:
        name: "screen A"
        Image:
            source: 'imageA.png'
            size_hint: 1, 1
            pos_hint: {'center_x':0.5, 'center_y': 0.86}  
        MDLabel:
            text:'Python'
            halign: "center"
            theme_text_color: "Primary"
            font_style:"H3"
            pos_hint: {'center_x': 0.5, 'center_y':0.69}
        MDRectangleFlatIconButton:
            text: "* * Introduction * *"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.6}
            font_size : 20
            on_release:
                root.current = "screen B"
        MDRectangleFlatIconButton:
            text: "* * Variables * *"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.51}
            font_size : 20
            on_release:
                root.current = "screen C"
        MDRectangleFlatIconButton:
            text: "* * Opérations * *"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.42}
            font_size : 20
            on_release:
                root.current = "screen D"
        MDRectangleFlatIconButton:
            text: "* * Conditions * *"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.33}
            font_size : 20
            on_release:
                root.current = "screen E"
        MDRectangleFlatIconButton:
            text: "* * Boucles * *"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.24}
            font_size : 20
            on_release:
                root.current = "screen F"
        MDRectangleFlatIconButton:
            text: "* * * Web * * *"
            pos_hint: {"center_x": .5}
            size_hint: (0.6, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.15}
            font_size : 20
            on_release:
                root.current = "screen G"
        MDFillRoundFlatIconButton:
            text: "Quiter"
            pos_hint: {"center_x": .5}
            size_hint: (0.9, 0.08)
            pos_hint: {'center_x':0.5, 'center_y':0.06}
            font_size : 20
            on_release:
                app.Open_dialog()
        MDIconButton:
            icon: "application-braces-outline"
            pos_hint: {'center_x':0.26,'center_y':0.33}
        MDIconButton:
            icon: "order-numeric-ascending"
            pos_hint: {'center_x':0.26,'center_y':0.42}
        MDIconButton:
            icon: "application-variable-outline"
            pos_hint: {'center_x':0.26,'center_y':0.51}
        MDIconButton:
            icon: "language-python"
            pos_hint: {'center_x':0.26,'center_y':0.6}
        MDIconButton:
            icon: "web-check"
            pos_hint: {'center_x':0.26,'center_y':0.15}
        MDIconButton:
            icon: "content-copy"
            pos_hint: {'center_x':0.26,'center_y':0.24}   

    MDScreen:
        name: "screen B"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            MDRaisedButton:
                text: "Introduction"
                font_size : 20
                size_hint: (1, 0.1)
            Image:
                source: 'imageB.png'
                size_hint: 1, 0.8
            MDRaisedButton:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    MDScreen:
        name: "screen C"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            MDRaisedButton:
                text: "Variables"
                font_size : 20
                size_hint: (1, 0.1)
            Image:
                source: 'imageC.png'
                size_hint: 1, 0.8
            MDRaisedButton:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    MDScreen:
        name: "screen D"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            MDRaisedButton:
                text: "Operations"
                font_size : 20
                size_hint: (1, 0.1)
            Image:
                source: 'imageD.png'
                size_hint: 1, 0.8
            MDRaisedButton:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    MDScreen:
        name: "screen E"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            MDRaisedButton:
                text: "Conditions"
                font_size : 20
                size_hint: (1, 0.1)
            Image:
                source: 'imageE.png'
                size_hint: 1, 0.8
            MDRaisedButton:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    MDScreen:
        name: "screen F"
        BoxLayout:
            padding:12
            spacing:3
            orientation: 'vertical'
            MDRaisedButton:
                text: "Conditions"
                font_size : 20
                size_hint: (1, 0.1)
            Image:
                source: 'imageF.png'
                size_hint: 1, 0.8
            MDRaisedButton:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"
    MDScreen:
        name: "screen G"
        BoxLayout:
            orientation: 'vertical'
            padding:10
            spacing:10
            MDRectangleFlatIconButton:
                text: "Page Web : Python version arabe"
                font_size : 20
                size_hint: (1, 0.35)
            MDFillRoundFlatIconButton:
                text: "Cliquer Ici"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    app.launch_link(0)
            MDRectangleFlatIconButton:
                text: "Livre : Introduction pratique à python"
                font_size : 20
                size_hint: (1, 0.35)
            MDFillRoundFlatIconButton:
                text: "Cliquer Ici"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    app.launch_link(1)
            MDFillRoundFlatIconButton:
                text: "Retour"
                font_size : 19
                size_hint: (1, 0.1)
                on_release:
                    root.current = "screen A"      

'''

def close_application(self): 
        
        MDApp.get_running_app().stop() 
        
        Window.close() 

class Test(MDApp):
    mydialog= None
    def dialog_close(self, *args):
        self.mydialog.dismiss(Force=True)
    def build(self):
        self.title='Langage Python'
        self.theme_cls.primary_palette="Blue"
        self.theme_cls.primary_hue="A700"
        self.theme_cls.theme_style= "Dark"
        return Builder.load_string(KV)
    def Open_dialog(self):
        if not self.mydialog:
            self.mydialog = MDDialog(
                text="You Want To Exit?",
                buttons=[MDFlatButton(text="yes",theme_text_color="Custom",text_color='blue',on_release=close_application)
                         ,MDFlatButton(text="Cancel",theme_text_color="Custom",text_color='blue',on_release=self.dialog_close)])
            self.mydialog.open()
        else:
            self.mydialog = MDDialog(
            text="You Want To Exit?",
            buttons=[MDFlatButton(text="yes",theme_text_color="Custom",text_color='blue',on_release=close_application)
                         ,MDFlatButton(text="Cancel",theme_text_color="Custom",text_color='blue',on_release=self.dialog_close)])
            self.mydialog.open()
    def launch_link(self, index):
        link = ''
        if index == 0:
            link = 'https://harmash.com/tutorials/python/overview'
        else:
            link = 'https://www.mediafire.com/file/6m3rkj8q9f7iwb7/introduction-pratique-python.pdf/file'
        webbrowser.open(link)
    
Test().run()