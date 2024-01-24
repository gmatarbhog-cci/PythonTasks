from Framework import Framework


class Selenium(Framework):

    def __init__(self):
        Framework.__init__(self)

    def run_tests(self):
        print('Running automation tests')
        self.generate_report('html')
