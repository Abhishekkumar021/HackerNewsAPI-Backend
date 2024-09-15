import pytest
from app.services.hn_api_service import fetch_stories

@pytest.mark.asyncio
async def test_fetch_stories():
    stories = await fetch_stories("newstories")
    assert len(stories) > 0

@pytest.mark.asyncio
async def test_fetch_stories_error():
    with pytest.raises(Exception):
        await fetch_stories("invalid_url")