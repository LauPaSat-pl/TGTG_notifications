"""
App to check available favourite packages from Too Good To Go, and send Telegram bot message
"""
import asyncio
import os
import time

from telegram import Bot
from tgtg import TgtgClient


async def main() -> None:
	"""
	Main function of the script
	"""
	access_token: str = os.environ['ACCESS_TOKEN']
	refresh_token: str = os.environ["REFRESH_TOKEN"]
	tgtg_user_id: str = os.environ['TGTG_USER_ID']
	cookie: str = os.environ['COOKIE']
	telegram_bot_id: str = os.environ['TG_BOT_ID']
	telegram_chat_id: str = os.environ['TG_CHAT_ID']
	tgtg_client: TgtgClient = TgtgClient(access_token=access_token,
	                                     refresh_token=refresh_token,
	                                     user_id=tgtg_user_id,
	                                     cookie=cookie)
	time.sleep(60)
	bot: Bot = Bot(telegram_bot_id)
	for item in tgtg_client.get_items():
		time.sleep(60)
		items_available: int = item['items_available']
		if items_available > 0:
			await bot.send_message(chat_id=telegram_chat_id,
			                       text=f"There are {items_available} bags")


if __name__ == '__main__':
	asyncio.run(main())
