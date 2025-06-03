import asyncio
import os

from aiohttp_library.useful_functions import download_video


async def main():
    video_link = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
    file_path = 'files/videos/short_video.mp4'

    success = await download_video(video_link, file_path, 10000)

    if success:
        video_size_bytes = os.path.getsize(file_path)
        video_size_mb = video_size_bytes / (1024 * 1024)
        print(f'Video size: {video_size_mb:.2f} MB')
    else:
        print('Failed to download video')


if __name__ == '__main__':
    asyncio.run(main())
