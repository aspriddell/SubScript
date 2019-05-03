import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'SubScript.xaml')

    
    def Button_Click(self, sender, e):
    	print("Hello")


if __name__ == '__main__':
    Application().Run(MyWindow())
