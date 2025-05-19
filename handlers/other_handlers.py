from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_with_id_message(message: Message):
    media_ids = []
    match message:
        case Message(photo=photo) if photo:
            largest = photo[-1]
            media_ids.append(f"📷 Фото: {largest.file_id}")

        case Message(voice=voice) if voice:
            media_ids.append(f"🎤 Голосовое сообщение: {voice.file_id}")

        case Message(video=video) if video:
            media_ids.append(f"🎬 Видео: {video.file_id}")

        case _:
            pass  # Другие типы сообщений нас не интересуют

        # Ответ пользователю
    if media_ids:
        await message.answer("\n".join(media_ids))
    else:
        await message.answer("Медиа не найдено 🙃")