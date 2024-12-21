import asyncio
import uuid
import aiormq
import aiormq.abc
from core import config
import json
from threading import Thread


class ValidationRpcClient:
    def __init__(self):
        self.connection = None  # type: aiormq.Connection
        self.channel = None  # type: aiormq.Channel
        self.callback_queue = ''
        self.futures = {}
        self.loop = None

    def configure(self, loop):
        self.loop = loop

    async def connect(self):
        for _ in range(10):
            try:
                self.connection = await aiormq.connect(config.settings.RABBITMQ_URL)
            except aiormq.AMQPConnectionError:
                await asyncio.sleep(1)
        if self.connection is None:
            raise Exception("Can't connect to rabbitmq")

        self.channel = await self.connection.channel()
        declare_ok = await self.channel.queue_declare(
            exclusive=True, auto_delete=True
        )

        await self.channel.basic_consume(declare_ok.queue, self.on_response)

        self.callback_queue = declare_ok.queue

        return self

    async def on_response(self, message: aiormq.abc.DeliveredMessage):
        future = self.futures.pop(message.header.properties.correlation_id)
        future.set_result(message.body)

    async def call(self, phone):
        correlation_id = str(uuid.uuid4())
        future = self.loop.create_future()

        self.futures[correlation_id] = future
        payload = {"command": "validate_phone", "phone": phone}
        await self.channel.basic_publish(
            json.dumps(payload).encode(),
            routing_key='rpc_queue',
            properties=aiormq.spec.Basic.Properties(
                content_type='application/json',
                correlation_id=correlation_id,
                reply_to=self.callback_queue,
            )
        )
        result = (await future).decode()
        result = json.loads(result)
        return result.get("result")


# why
# async def validate_phone(phone):
#     test_rpc = await ValidationRpcClient(asyncio.get_event_loop()).connect()
#     response = await test_rpc.call(phone)
#     return response
