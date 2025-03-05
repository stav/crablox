import os
from io import BytesIO

import httpx
from starlette.responses import StreamingResponse

import hauls

from config import SPEECHIFY_API_KEY

# Get the output directory for the audio files
file_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(file_path)
audio_dir = os.path.join(parent_dir, "audio")
output_dir = os.path.abspath(audio_dir)


async def get_audio(id: str):
    # Find the block with the given ID
    for block in hauls.blocks:
        if block.id == id:
            break
    else:
        return f"Block not found: `{id}`", 404

    # Check if the audio file already exists
    output_file_path = os.path.join(output_dir, f"{id}.mp3")

    # If the file exists, return it
    if os.path.exists(output_file_path):
        with open(output_file_path, "rb") as f:
            audio_stream = BytesIO(f.read())
        return StreamingResponse(audio_stream, media_type="audio/mpeg")

    # If the file does not exist, get it from the Speechify API
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.post(
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

    # Save the audio file to the output directory
    with open(output_file_path, "wb") as f:
        f.write(response.content)

    # Buffer the audio file
    audio_stream = BytesIO(response.content)

    # Return the audio stream
    return StreamingResponse(audio_stream, media_type="audio/mpeg")
