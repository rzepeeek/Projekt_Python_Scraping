import aiohttp
import asyncio

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except:
        return ""

async def scrape_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)