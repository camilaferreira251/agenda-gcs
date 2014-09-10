class Crud():
	def __init__(self):
	        pass
	def inserirContato(self, nome, sobrenome, endereco, telefone, dicionario):
		ultimoID = max(dicionario.keys())
