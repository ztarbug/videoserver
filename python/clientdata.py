

class ClientData:

    def __init__(self, hostname, client_id, cmd_queue):
        print("created new instance")
        self.command_queue = cmd_queue
        self.client_hostname = hostname
        self.client_id = client_id

    def to_string(self):
        return "host: " + self.client_hostname + ", id: " + str(self.client_id)