# PROJECT IMPORTS
from src.domain.validator.webhook.validator import WebHookMessage
from src.trasnport.bifrost import BifrostTransport


class ForexAccountService:

    @classmethod
    async def request_payment_order_process(cls, webhook_message: WebHookMessage) -> bool:
        result = await BifrostTransport.send_payment_order_to_process(
            webhook_message=webhook_message
        )
        return result
