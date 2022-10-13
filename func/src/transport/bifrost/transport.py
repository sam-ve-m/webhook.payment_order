from bifrost_client import BifrostTopics, BifrostClient
from src.domain.exceptions.exceptions import NotSentToBifrost
from src.domain.validator.webhook.validator import WebHookMessage


class BifrostTransport:
    @staticmethod
    async def send_payment_order_to_process(webhook_message: WebHookMessage) -> bool:
        success, reason = await BifrostClient.send_to_bifrost(
            topic=BifrostTopics.PROCESS_FOREX_EXCHANGE_PAYMENT_ORDER,
            message={
                "payment_order": webhook_message.payment_order_id,
                "reference_date": webhook_message.income_date
            }
        )
        if not success:
            raise NotSentToBifrost(str(reason))
        return success
