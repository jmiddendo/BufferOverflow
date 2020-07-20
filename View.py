class View():

    def __init__(self, control, prior_view = None):
        self.control = control
        self.prior_view = prior_view

    def get_control(self):
        return self.control

    def query_user(self, message):
        return input(message)

    def set_control(self, control):
        self.control = control
