from queue import Queue

urls_to_crawl = Queue()
urls_to_crawl.put("http://example.com")

import aiohttp
import asyncio
from threading import Thread

async def download_url(session, url):
    async with session.get(url) as response:
        print(f"Downloaded {url}: {response.status}")
        return await response.text()

def start_download_thread(loop, urls_queue):
    asyncio.set_event_loop(loop)
    while not urls_queue.empty():
        url = urls_queue.get()
        with aiohttp.ClientSession(loop=loop) as session:
            loop.run_until_complete(download_url(session, url))

def start_crawler(urls_queue):
    loop = asyncio.new_event_loop()
    for _ in range(5):  # Number of concurrent threads
        t = Thread(target=start_download_thread, args=(loop, urls_queue))
        t.start()
        t.join()

from bs4 import BeautifulSoup

async def parse_and_extract_urls(session, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith("http"):
            print(f"Found URL: {href}")
            urls_to_crawl.put(href)

async def download_url(session, url):
    try:
        async with session.get(url) as response:
            print(f"Downloaded {url}: {response.status}")
            return await response.text()
    except aiohttp.ClientError as e:
        print(f"Error downloading {url}: {str(e)}")

import time

last_request_time = None

async def rate_limited_get(session, url):
    global last_request_time
    if last_request_time is not None:
        await asyncio.sleep(max(1 - (time.time() - last_request_time), 0))
    last_request_time = time.time()
    return await session.get(url)

