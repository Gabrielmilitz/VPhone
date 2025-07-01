
class Gerenciador_senha:
    def __init__(self):
        self.senhas_armazenadas = []

    def armazenar_gui(self, senha):
        if senha:
            self.senhas_armazenadas.append(senha)
            return "Senha armazenada com sucesso!"
        return "Senha vazia. Digite algo."

    def exibir_gui(self):
        if not self.senhas_armazenadas:
            return "Nenhuma senha armazenada."
        return "\n".join(self.senhas_armazenadas)
