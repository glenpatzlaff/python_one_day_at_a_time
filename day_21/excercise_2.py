import aiohttp
import asyncio


async def fetch_content(url, session):
    async with session.get(url) as response:
        content = await response.read()
        print(f"URL: {url}, Content Length: {len(content)}")


async def main():
    urls = [
        'http://example.com',
        'http://example.org',
        'http://example.net'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_content(url, session) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
