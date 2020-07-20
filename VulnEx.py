from Controller import Controller
from MainView import MainView

def main():

    ct = Controller()
    mv = MainView(ct)
    mv.run()
    

if __name__ == '__main__':
    main()
