import asyncio
import aiohttp

SUCCESS_COLOR = '\033[92m'
FAIL_COLOR = '\033[91m'
NO_COLOR = '\033[0m'
PURPLE_COLOR = '\033[95m'
CYAN_TEXT = '\033[96m'
BOLD_TEXT = '\033[1m'


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def fetch_all(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(
            *[fetch(session, url) for url in urls],
            return_exceptions=True)
        return results


def get_formulae_urls():
    import sys
    return [f'https://formulae.brew.sh/api/formula/{line.strip()}.json'
            for line in sys.stdin.readlines()]


def check_for_ventura_support(formulae_data):
    supported_formulae = []

    for formula in formulae_data:
        name = formula['name']
        ventura_bottle = formula.get('bottle', {})\
            .get('stable', {})\
            .get('files', {})\
            .get('arm64_ventura')

        if not ventura_bottle:
            print(f'{FAIL_COLOR}Formula "{name}" does '
                  f'not have a bottle for Ventura{NO_COLOR}')
            continue

        print(f'{SUCCESS_COLOR}Formula "{name}" has a bottle for Ventura{NO_COLOR}')
        supported_formulae.append(name)

    return f'brew reinstall {" ".join(supported_formulae)}'


def main():
    loop = asyncio.get_event_loop_policy().get_event_loop()
    formulae_urls = get_formulae_urls()
    formulae_data = loop.run_until_complete(fetch_all(formulae_urls, loop))

    print(f"{BOLD_TEXT}Result of the macOS Ventura bottle support:{NO_COLOR}")
    reinstall_command = check_for_ventura_support(formulae_data)

    print(f'{PURPLE_COLOR}{"=" * 20}{NO_COLOR}'
          f'\n{BOLD_TEXT}Run the following command to reinstall '
          f'all formulae that have a bottle for Ventura:{NO_COLOR}\n'
          f'{CYAN_TEXT}{reinstall_command}{NO_COLOR}')


if __name__ == '__main__':
    main()
