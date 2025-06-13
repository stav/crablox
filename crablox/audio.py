import os
from starlette.responses import FileResponse, PlainTextResponse
import logging

logger = logging.getLogger(__name__)

file_path = os.path.abspath(__file__)
parent_dir = os.path.dirname(file_path)
audio_dir = os.path.join(parent_dir, "media")
output_dir = os.path.abspath(audio_dir)


def get_audio_file(id: str):
    logger.info(f"Getting main direct audio for `{id}`")

    path = os.path.join(output_dir, f"{id}.mp3")
    logger.info(f"File path: {path}")

    if not os.path.exists(path):
        logger.error(f"File not found: {path}")
        return PlainTextResponse(f"File not found: {id}.mp3", status_code=404)

    return FileResponse(path, media_type="audio/mpeg", filename=f"{id}.mp3")
