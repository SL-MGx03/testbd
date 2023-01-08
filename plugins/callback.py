#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pyrogram import filters
from pyrogram import Client as Clinton
from plugins.dl_button import ddl_call_back

@Clinton.on_callback_query(filters.regex('^X0$'))
async def delt(bot, update):
          await update.message.delete(True)
