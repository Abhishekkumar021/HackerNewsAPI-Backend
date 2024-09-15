from fastapi import APIRouter, HTTPException
from app.services.hn_api_service import fetch_stories

router = APIRouter()


@router.get("/new-stories")
async def get_new_stories():
    try:
        stories = await fetch_stories("newstories")
        return stories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/top-stories")
async def get_top_stories():
    try:
        stories = await fetch_stories("topstories")
        return stories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/best-stories")
async def get_best_stories():
    try:
        stories = await fetch_stories("beststories")
        return stories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/show-stories")
async def get_show_stories():
    try:
        stories = await fetch_stories("showstories")
        return stories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/job-stories")
async def get_job_stories():
    try:
        stories = await fetch_stories("jobstories")
        return stories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
