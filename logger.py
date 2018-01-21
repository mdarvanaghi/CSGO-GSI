class LogFile:
    def __init__(self, timestamp):
        self.name = str(timestamp).replace(' ', '_').replace(':', '-')
        self.path = 'logs/' + self.name + '.txt'
        self.create_file()

    def create_file(self):
        file = open(self.path, 'w')
        file.write('Log file created at ' + self.name + '\n')
        file.close()

    def log_event(self, timestamp, event):
        file = open(self.path, 'a')
        file.write(timestamp + '\n')
        file.write(str(event))
        file.write('\n')
        file.close()