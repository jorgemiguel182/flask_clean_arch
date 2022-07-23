import re


class CPF:
    def __init__(self, numero: str):
        if not self._validar(numero):
            raise Exception("CPF Inválido.")
        self.numero = numero

    def get_value(self):
        return self.numero

    def _validar(self, numero: str) -> bool:
        cpf = self._limpar_cpf(numero)
        if self._tamanho_invalido(cpf):
            return False

        if self._check_repeated_digits(cpf):
            return False

        calc = lambda t: int(t[1]) * (t[0] + 2)
        d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
        d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
        return str(d1) == cpf[-2] and str(d2) == cpf[-1]

    def _limpar_cpf(self, cpf: str) -> str:
        return re.sub('[^0-9]', '', cpf)

    def _tamanho_invalido(self, cpf: str) -> bool:
        return len(cpf) != 11

    def _check_repeated_digits(self, doc: str) -> bool:
        """Verifica se é um CPF com números repetidos.
        Exemplo: 111.111.111-11"""
        return len(set(list(doc))) == 1