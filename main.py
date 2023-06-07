from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivyauth.google_auth import initialize_google,login_google,logout_google


class Homescreen(Screen):
    pass

class Fistscreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        initialize_google(self.GoFirst,self.GoFirst,'388939015279-00vmdoso1vj6i10lop3qetlkj1lht08o.apps.googleusercontent.com','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')
        self.sm = ScreenManager()
        self.sm.add_widget(Homescreen(name='home'))
        self.sm.add_widget(Fistscreen(name='first'))
        return self.sm


    def GoToHome(self):
        self.sm.current='home'

    def GoFirst(self,name,email,photo_url):
        print('DEEEEEEEEDERRRRRRRRRRRRRRRRRRRRRR',name,email,photo_url)

    def login(self):
        login_google()

MainApp().run()