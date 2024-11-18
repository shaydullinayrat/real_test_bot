from django.core.management.base import BaseCommand, CommandError
import asyncio

from the_core.apps.bot.main_bot import bot


class Command(BaseCommand):
    help = "Запускаем бота"

    def handle(self, *args, **options):
        asyncio.run(bot.polling())
