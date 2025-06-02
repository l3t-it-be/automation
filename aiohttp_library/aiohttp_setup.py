import asyncio

import aiohttp
from aiohttp_retry import ExponentialRetry, RetryClient
from fake_useragent import UserAgent

ua = UserAgent()


class AsyncSessionManager:
    def __init__(self, max_connections: int = 10):
        self.max_connections = max_connections
        self.semaphore = asyncio.Semaphore(max_connections)
        self.user_agent = ua.random
        self.connector = aiohttp.TCPConnector(
            force_close=True, limit=0, enable_cleanup_closed=True
        )
        self.session = aiohttp.ClientSession(
            connector=self.connector,
            headers={'User-Agent': self.user_agent, 'Accept-Charset': 'utf-8'},
            timeout=aiohttp.ClientTimeout(total=60),
        )

    def create_client(self):
        retry_options = ExponentialRetry(
            max_timeout=120,
            statuses={301, 302, 500, 502, 503, 504},
            exceptions={aiohttp.ClientError, asyncio.TimeoutError},
        )

        return RetryClient(
            retry_options=retry_options,
            client_session=self.session,
            start_timeout=10,
        )

    async def close_session(self):
        await self.session.close()
        await self.connector.close()
