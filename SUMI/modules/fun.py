import html
import random
import time

from pyjokes import get_joke  #thanks to @ishikki_akabane who did nothing and just copypasted this joke feature
from SUMI.events import register
import SUMI.modules.fun_strings as fun_strings
from SUMI import dispatcher, COTB
from SUMI.modules.disable import DisableAbleCommandHandler
from SUMI.modules.helper_funcs.chat_status import is_user_admin
from SUMI.modules.helper_funcs.extraction import extract_user
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions, ParseMode, Update)
from telegram.error import BadRequest
from telegram.ext import CallbackContext, run_async

GIF_ID = "CgACAgQAAxkBAAILHWBPN8dL8NvxZ9tUfr3_4SdPGqgjAAJeAgACQQrNUlM24z1ISCsTHgQ"

#----------@ishikki_akabane
@register(pattern="^/joke ?(.*)")
async def joke(event):
    await event.reply(get_joke())
#--------------------------

@run_async
def runs(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))


@run_async
def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(GIF_ID, caption=f"*Sanitizes {name}*")


@run_async
def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(random.choice(fun_strings.GIFS), caption=f"*Sanitizes {name}*")


@run_async
def slap(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = message.reply_to_message.reply_text if message.reply_to_message else message.reply_text

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP2_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False))
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings.SLAP_TEMPLATES)
    item = random.choice(fun_strings.ITEMS)
    hit = random.choice(fun_strings.HIT)
    throw = random.choice(fun_strings.THROW)

    if update.effective_user.id == 1096215023:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(
        user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)

    if update.effective_user.id == 5030730429:
        temp = "Are you stupid {user2}, Ishikki is MY LOVE"

    reply = temp.format(
        user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
def pat(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    pat_type = random.choice(("Text", "Gif", "Sticker"))
    if pat_type == "Gif":
        try:
            temp = random.choice(fun_strings.PAT_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Sticker":
        try:
            temp = random.choice(fun_strings.PAT_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Text":
        temp = random.choice(fun_strings.PAT_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


@run_async
def roll(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(range(1, 7)))

def flirt(update: Update, context: CallbackContext):    #This feature's credit goes to @ishikki_akabane
    args = context.args
    update.effective_message.reply_text(random.choice(fun_strings.FLIRT))

@run_async
def shout(update: Update, context: CallbackContext):
    args = context.args
    text = " ".join(args)
    result = []
    result.append(' '.join(list(text)))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


@run_async
def toss(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(fun_strings.TOSS))
    
@run_async
def cosplay(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(random.choice(fun_strings.COSPLAY))

R_IMG = "https://telegra.ph/file/5a07ded9ebce5b693c4ff.jpg"  #DONT REMOVE THIS CREDITS
TEXT2 = """*‣ REPO OWNER:*
• [Ishikki Akabane](t.me/ishikki_akabane) (◍•ᴗ•◍)
┈─╌┈─╌┈─╌┈─╌
My source codes are now public, you can use them for creating your own bot
Visit @suppporttxd if you face any issue related to the bot or for any kind of help
**Click The Button Below To Get My Repo**""" #DONT REMOVE THIS CREDITS

@run_async
def repo(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(
        R_IMG, caption= TEXT2,
        parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="Source CODE", url="https://github.com/ishikki-akabane/SUMI"),
                InlineKeyboardButton(text="DEVELOPER", url="https://t.me/ishikki_akabane")
                ]
            ]
        )
    )

@run_async
def shrug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(r"¯\_(ツ)_/¯")


@run_async
def bluetext(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(
        "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS"
    )


@run_async
def rlg(update: Update, context: CallbackContext):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)


@run_async
def decide(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.DECIDE))
    
@run_async
def sex(update: Update, context: CallbackContext):
    reply_animation = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_animation(random.choice(fun_strings.SEX))

    
normiefont = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
weebyfont = [
    '卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口',
    '尸', '㔿', '尺', '丂', '丅', '凵', 'リ', '山', '乂', '丫', '乙'
]


@run_async
def weebify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = '  '.join(args).lower()

    if not string:
        message.reply_text(
            "Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


__help__ = """
 ➢ `/runs`*:* reply a random string from an array of replies
 ➢ `/slap`*:* slap a user, or get slapped if not a reply
 ➢ `/shrug`*:* get shrug XD
 ➢ `/sex`*:* get :v
 ➢ `/decide`*:* Randomly answers yes/no/maybe
 ➢ `/toss`*:* Tosses A coin
 ➢ `/bluetext`*:* check urself :V
 ➢ `/roll`*:* Roll a dice
 ➢ `/rlg`*:* Join ears,nose,mouth and create an emo ;-;
 ➢ `/shout <keyword>`*:* write anything you want to give loud shout
 ➢ `/weebify <text>`*:* returns a weebified text
 ➢ `/sanitize`*:* always use this before /pat or any contact
 ➢ `/pat`*:* pats a user, or get patted
 ➢ `/hugs` or `/hug` *:* get hugged, hugs a user 
"""

SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
REPO_HANDLER = DisableAbleCommandHandler("repo", repo)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)
COSPLAY_HANDLER = DisableAbleCommandHandler("cosplay", cosplay)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
SEX_HANDLER = DisableAbleCommandHandler("sex", sex)
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout)
WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify)
FLIRT_HANDLER = DisableAbleCommandHandler("flirt", flirt)

dispatcher.add_handler(WEEBIFY_HANDLER)
dispatcher.add_handler(SHOUT_HANDLER)
dispatcher.add_handler(SANITIZE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(SEX_HANDLER)
dispatcher.add_handler(COSPLAY_HANDLER)
dispatcher.add_handler(FLIRT_HANDLER)  #@ishikki_akabane 
dispatcher.add_handler(REPO_HANDLER)

__mod_name__ = "Fun"
__command_list__ = [
    "runs", "slap", "roll", "toss", "shrug", "bluetext", "rlg", "decide",
    "sex", "pat", "sanitize", "shout", "cosplay", "weebify", "flirt"
]
__handlers__ = [
    RUNS_HANDLER, SLAP_HANDLER, PAT_HANDLER, ROLL_HANDLER, TOSS_HANDLER,
    SHRUG_HANDLER, BLUETEXT_HANDLER, RLG_HANDLER, DECIDE_HANDLER, SANITIZE_HANDLER, 
    SEX_HANDLER, SHOUT_HANDLER, WEEBIFY_HANDLER, COSPLAY_HANDLER
]
