from typing import List, Optional
from src.modules.communication.dto.message_dto import MessageDTO


class MessageDAO:
    MSG_COUNT_TO_FETCH = 300

    async def collect_messages(
        self, last_msg_id: Optional[str] = None
    ) -> List[MessageDTO]:
        # FIXME: скорее всего если я хочу сделать так как указал в коменте таски
        # нужно будет изменить отправляемый обьект на Dict где ключи будут id сообщений
        ...
