from View import View

class MainView(View):

    def __init__(self, control):

        super().__init__(control)

    def display(self):

        print('\n           Main Menu')
        print('================================')
        print('1) Add an exploit')
        print('2) Scan a target')
        print('3) Exploit a target')
        print('4) Exit')

    def dispose(self):
        pass

    def results(self, results):
        print('\n         Results')
        print('================================')

        try:
            for result in results:
                print(result)
        except Exception as e:
            print('[-] Unspecified error: ' + str(e))

    def run(self):

        choice = None
        while (choice != '4'):
            self.display()
            choice = super().query_user('Please make a choice: ') 
            if choice == '1':
                self.results(super().get_control().add_exploit()) 
            elif choice == '2':
                self.results(super().get_control().scan())
            elif choice == '3':
                self.results(super().get_control().exploit('10.0.0.209',9999)) 
            elif choice == '4':
                pass
            else:
                print('Invalid choice!  Please try again!')
                continue

        print('Thank you for using the scanner!')

        
