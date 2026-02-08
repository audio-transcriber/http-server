from domain.ports import MessageBrokerProducer


class RabbitMQProducer(MessageBrokerProducer):
    async def send(self) -> None:
        print('Отправил в RabbitMQ')
