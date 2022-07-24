from src.domain.repository.CupomRepository import CupomRepository
from src.infra.dto.CupomDTO import CupomDTO


class ValidateCupomUseCase:
    def __init__(self, cupom_repository: CupomRepository):
        self.cupom_repository = cupom_repository

    def execute(self, input_dto: CupomDTO) -> bool:
        cupom = self.cupom_repository.get_cupom_by_codigo(input_dto.codigo)
        expired = cupom.is_expired(input_dto.date_to_validate)
        return False if expired else True
