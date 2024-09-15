import httpx
from fastapi import HTTPException
from datetime import datetime
from app.models.story import Story
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)


async def fetch_stories(storyType: str = "newstories"):
    try:
        # print(settings.BASE_HN_URL)
        base_hn_url = os.getenv('BASE_HN_URL')
        logger.info(f"Fetching stories of type: {storyType} and url : {base_hn_url}/{storyType}.json?print=pretty")
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{base_hn_url}/{storyType}.json?print=pretty"
            )
            response.raise_for_status()

            storyIds = response.json()[:15]

            stories = []

            for story_id in storyIds:
                response = await client.get(
                    f"{base_hn_url}/item/{story_id}.json?print=pretty"
                )
                response.raise_for_status()

                data = response.json()

                # print(f'Data for storyId : {story_id}\n', data)
                # print('-------------------------')

                time = data["time"]
                formatted_time = datetime.fromtimestamp(time).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                if all(key in data for key in ["url", "by", "title", "score", "time"]):
                    story_data = {
                        "title": data["title"],
                        "author": data["by"],
                        "url": data["url"],
                        "score": data["score"],
                        "time": formatted_time,
                    }

                    stories.append(Story(**story_data))

                if len(stories) == 10:
                    break

            # print(stories)
            logger.info(f"Fetched {len(stories)} stories")
        return stories
    except httpx.ConnectError:
        logger.error("HackerNews API is unreachable.")
        raise HTTPException(
            status_code=503,
            detail="HackerNews API is unreachable. Please try again later.",
        )
    except httpx.HTTPStatusError as e:
        logger.error(f"Error fetching data from HackerNews: {e.response.status_code}")
        raise HTTPException(
            status_code=e.response.status_code,
            detail="Error fetching data from HackerNews",
        )
    except httpx.TimeoutException:
        logger.error("Request to HackerNews API timed out.")
        raise HTTPException(
            status_code=504,
            detail="Request to HackerNews API timed out. Please try again later.",
        )
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred: " + str(e)
        )


# import httpx
# from fastapi import HTTPException
# from datetime import datetime
# from app.config import settings
# from app.models.story import Story
# import asyncio
# import logging


# logging.basicConfig(level=logging.INFO)

# client = httpx.AsyncClient(timeout=httpx.Timeout(10.0))


# async def fetch_story(story_id: int):
#     response = await client.get(
#         f"{settings.BASE_HN_URL}/item/{story_id}.json?print=pretty"
#     )
#     response.raise_for_status()
#     data = response.json()

#     time = data["time"]
#     formatted_time = datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")

#     if all(key in data for key in ["url", "by", "title", "score", "time"]):
#         return Story(
#             title=data["title"],
#             author=data["by"],
#             url=data["url"],
#             score=data["score"],
#             time=formatted_time,
#         )
#     return None


# async def fetch_stories(storyType: str = "newstories"):
#     try:
#         response = await client.get(
#             f"{settings.BASE_HN_URL}/{storyType}.json?print=pretty"
#         )
#         response.raise_for_status()

#         storyIds = response.json()[:15]
#         tasks = [fetch_story(story_id) for story_id in storyIds]
#         stories = await asyncio.gather(*tasks)

#         # Filter out None values (in case some stories were invalid)
#         return [story for story in stories if story is not None][:10]

#     except httpx.ConnectError:
#         logging.error("HackerNews API is unreachable.")
#         raise HTTPException(status_code=503, detail="HackerNews API is unreachable. Please try again later.")
#     except httpx.HTTPStatusError as e:
#         logging.error(f"Error fetching data from HackerNews: {e.response.status_code} - {e.response.text}")
#         raise HTTPException(status_code=e.response.status_code, detail="Error fetching data from HackerNews")
#     except httpx.TimeoutException:
#         logging.error("Request to HackerNews API timed out.")
#         raise HTTPException(status_code=504, detail="Request to HackerNews API timed out. Please try again later.")
#     except Exception as e:
#         logging.error(f"An unexpected error occurred: {str(e)}")
#         raise HTTPException(status_code=500, detail="An unexpected error occurred: " + str(e))
