from Scanner import Scanner

class Controller():

    def __init__(self):
        pass

    def add_exploit(self):
        results = ['[-] Not yet implemeted']
        return results

    def exploit(self, ip, port):

        scanner = Scanner()

        results = []	

        response = scanner.grab_banner(ip,port) 

        if response: 
            chk = scanner.check_vulns(response)
            # Update with specific name call
            from VulnServer import VulnServer
            exp = VulnServer(ip,port)
            results.extend(exp.exploit())
        	
            try:
                results.append('[*] Check your listener')
            except Exception as e:
                results = ['[-] ' + str(e)]
            finally:
                return results

        else:
            return ['[-] Unable to grab the banner']

    def scan(self):
        results = ['[-] Not yet implemented']
        return results
			

    def switch_views(self, current_view, new_view):
        current_view.dispose()
        new_view.run()
