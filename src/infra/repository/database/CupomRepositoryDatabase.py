from src.domain.entity.Cupom import Cupom
from src.domain.repository.CupomRepository import CupomRepository
from src.infra.database.Connection import Connection


class CupomRepositoryDatabase(CupomRepository):
    def __init__(self, connection: Connection):
        self.connection = connection

    def get_cupom_by_codigo(self, codigo: str) -> Cupom:
        results = self.connection.query("SELECT * FROM cccat7.cupom where codigo = %s", (codigo, ), False)
        return Cupom(codigo, results[0][2], results[0][3])
