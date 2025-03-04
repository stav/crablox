from io import BytesIO

import httpx
from starlette.responses import StreamingResponse

import hauls

from config import SPEECHIFY_API_KEY


async def get_audio(id: str):
    for block in hauls.blocks:
        if block.id == id:
            break
    else:
        return f"Block not found: `{id}`", 404

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.sws.speechify.com/v1/audio/stream",
            headers={
                "Authorization": f"Bearer {SPEECHIFY_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "input": "Hello, world!",
                "voice_id": "george",
            },
        )
        response.raise_for_status()

    audio_stream = BytesIO(response.content)
    return StreamingResponse(audio_stream, media_type="audio/mpeg")
