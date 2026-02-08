from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, UploadFile
from starlette.status import HTTP_202_ACCEPTED

from application.transcription.use_cases import TranscriptionUseCase
from infrastructure.containers import TranscriptionContainer

route = APIRouter(prefix='/transcription', tags=['Transcription'])


@route.post('/transcribe', status_code=HTTP_202_ACCEPTED)
@inject
async def transcribe(
    file: UploadFile, use_case: TranscriptionUseCase = Depends(Provide[TranscriptionContainer.use_case])
) -> None:
    await use_case.transcribe(await file.read(), file.filename)
