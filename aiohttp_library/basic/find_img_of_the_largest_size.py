import asyncio

from aiohttp_library.useful_functions import get_response_data


async def main():
    with open('files/text_files/images.txt') as images_file:
        images_names = images_file.readlines()

    images_names = [name.strip("',\n") for name in images_names]
    tasks = [get_image_size(name) for name in images_names]

    max_size = -float('inf')
    img_with_max_size = ''

    result = await asyncio.gather(*tasks)
    for img_name, img_size in result:
        if img_size > max_size:
            max_size = img_size
            img_with_max_size = img_name

    print(f'Image of the largest size {max_size}: {img_with_max_size}')


async def get_image_size(img_name):
    url = f'https://parsinger.ru/3.3/3/img/{img_name}'

    async with await get_response_data(url, return_response=True) as response:
        if response.ok:
            size = int(response.headers.get('content-length'))
            return img_name, size
        else:
            print(f'Failed to retrieve page content: {url}')
            return None


if __name__ == '__main__':
    asyncio.run(main())
