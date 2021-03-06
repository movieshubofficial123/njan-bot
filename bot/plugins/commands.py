#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG
# Modified by @Leos_tg

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # hmmm
from bot.database import Database # hmmm
 # removed ForceSub #add if u want
db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption =f"<b>πΎ:@PrimeFlixMedia_All.<code>{file_name}</code>π½οΈ\n\n@PrimeFlix_Chats</b>\n\n<i>πππππ & πππππππ ππ~π.\nπΈπ πππππ ππ π πΆππ΄π°π π·πππβ€οΈπ.",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'π‘sΚα΄Κα΄ & sα΄α΄α΄α΄Κα΄π‘', url="https://t.me/share/url?url=%20https://t.me/PrimeFlix_Chats"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'π‘sΚα΄Κα΄ & sα΄α΄α΄α΄Κα΄π‘', url="https://t.me/share/url?url=%20https://t.me/PrimeFlix_Chats"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'π‘sΚα΄Κα΄ & sα΄α΄α΄α΄Κα΄π‘', url="https://t.me/share/url?url=%20https://t.me/PrimeFlix_Chats"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('β­Moviesβ­', url='https://t.me/joinchat/zLLsYNJJyRxkMzY1'),
        InlineKeyboardButton('β­Seriesβ­', url ='https://t.me/joinchat/RzAj6C0C6zWiuaxL')
    ],[
        InlineKeyboardButton('β­Groupβ­', url='https://t.me/PrimeFlix_Chats')
    ],[
        InlineKeyboardButton('β»οΈHelpβ»οΈ', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo = 'https://telegra.ph/file/24a1ddd705122b1c9e4a1.jpg',
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('β­Backβ­', callback_data='start'),
        InlineKeyboardButton('β­Aboutβ­', callback_data='about')
    ],[
        InlineKeyboardButton('β­Closeβ­', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('β­Backβ­', callback_data='start'),
        InlineKeyboardButton('β­Closeβ­', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
