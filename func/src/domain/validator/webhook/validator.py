import re
from datetime import datetime

import orjson
from pydantic import BaseModel


class WebHookMessage(BaseModel):
    client_id: int
    account_id: int
    payment_order_id: int
    currency_id: int
    currency_name: int
    value: float
    register_date: datetime
    income_date: datetime
    origin: str

    @classmethod
    def from_request(cls, request_body: dict):
        client_id = request_body.get("CodigoCliente")
        account_id = request_body.get("CodigoConta")
        payment_order_id = request_body.get("CodigoOrdemPagamento")
        currency_id = request_body.get("CdMoeda")
        currency_name = request_body.get("SimboloMoeda")
        value = request_body.get("ValorMonetario")
        register_date = request_body.get("DataCadastroOrdem")
        income_date = request_body.get("DataRecebimento")
        origin = request_body.get("Ordenante")

        return cls(
            client_id=client_id,
            account_id=account_id,
            payment_order_id=payment_order_id,
            currency_id=currency_id,
            currency_name=currency_name,
            value=value,
            register_date=register_date,
            income_date=income_date,
            origin=origin,
        )
