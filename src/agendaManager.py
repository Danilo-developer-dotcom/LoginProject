from .dbManager import DbManager

class AgendaManager:
    def __init__(self, usuario_id):
        self.dbManager = DbManager()
        self.usuario_id = usuario_id

    def meus_agendamentos(self):
        try:
            return self.dbManager.select_meus_agendamentos(self.usuario_id)
        except Exception as e:
            print(e)
            return False

    def marcar_data(self, data):
        return self.dbManager.agendar(data, self.usuario_id)

    def consultar_disponibilidade(self):
        pass