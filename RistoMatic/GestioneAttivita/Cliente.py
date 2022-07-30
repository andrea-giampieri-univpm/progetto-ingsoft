class Cliente():

    id = 0
    def __init__(self, nomeCliente, recapitoTelefonico):
        self.idCliente = self.id
        self.id += 1
        self.nomeCliente = nomeCliente
        self.recapitoTelefonico = recapitoTelefonico

    def getIdCliente(self):
        return self.idCliente

    def getNomeCliente(self):
        return self.nomeCliente

    def getInfoCliente(self):
        return {
            "nomeCliente": self.nomeCliente,
            "idCliente": self.idCliente,
            "recapitoTelefonico": self.recapitoTelefonico
        }

    def getRecapitoTelefonico(self):
        return self.recapitoTelefonico

    def setNomeCliente(self, nomeCliente):
        self.nomeCliente = nomeCliente

    def setRecapitoTelefonico(self, recapitoTelefonico):
        self.recapitoTelefonico = recapitoTelefonico


