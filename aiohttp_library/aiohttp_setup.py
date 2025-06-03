import asyncio

import aiohttp
from aiohttp_retry import ExponentialRetry, RetryClient
from fake_useragent import UserAgent

ua = UserAgent()


class AsyncSessionManager:
    def __init__(self):
        self.user_agent = ua.random
        self.connector = aiohttp.TCPConnector(
            limit_per_host=8, force_close=True, enable_cleanup_closed=True
        )
        self.session = aiohttp.ClientSession(
            connector=self.connector,
            headers={'User-Agent': self.user_agent, 'Accept-Charset': 'utf-8'},
            timeout=aiohttp.ClientTimeout(
                total=90,
                connect=30,
                sock_read=30,
            ),
        )

    def create_client(self):
        retry_options = ExponentialRetry(
            max_timeout=150,
            statuses={429, 500, 502, 503, 504},
            exceptions={aiohttp.ClientError, asyncio.TimeoutError},
        )

        return RetryClient(
            retry_options=retry_options,
            client_session=self.session,
            start_timeout=15,
        )

    async def close_session(self):
        await self.session.close()
        await self.connector.close()
