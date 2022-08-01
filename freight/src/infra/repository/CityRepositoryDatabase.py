from src.domain.entity.City import City
from src.domain.repository.CityRepository import CityRepository
from src.infra.database.Connection import Connection


class CityRepositoryDatabase(CityRepository):
    def __init__(self, connection: Connection):
        self.connection = connection

    def get_by_zip_code(self, code: str) -> City:
        sql = "select id_city, name, lat, long from ccca_freight.zipcode join ccca_freight.city using (id_city) where code = %s"
        params = (code, )
        results = self.connection.query(sql, params, False)
        if len(results) < 1: raise Exception("City not found")
        return City(results[0][0], results[0][1], results[0][2], results[0][3])
