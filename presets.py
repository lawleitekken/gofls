# ----------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------ #

class Presets(object):
    CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
    CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
    ASK_PM_TEXT = "<b>Click the below button</b>"
    WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>I can help you getting movies from</code> " \
                   "<code>Just Keep this message live Here</code>😉\n\n" \
                  
    CLEAN_CHAT_MSG = "⚠️ <b>Deleting all messages..</b>"
    MSG_FOR_PIN = "<b>For getting medias from here..</b>\n\n🔛 <code>Please start</code> @{} <code>in PM\n\n" \
                  "Send the exact Movie name.\n\n🔊 I'll reply the file in PM if available in our channel !</code>"

    BOT_PM_TEXT = "<b>Sorry.. 😢</b>\n\n<code>Bot won't work in PM, Ask in ma Group. I'll reply the file in PM if " \
                  "available in our DB !</code>"
    PM_ERROR = "<b>Unable to send movie</b> ⛔️\n<code>Click the below button\nAsk here for movies later!</code>"
    MEDIA_SEND_TEXT = "<code> 𝙃𝙚𝙧𝙚 𝙔𝙤𝙪𝙧 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙈𝙤𝙫𝙞𝙚🥳</code>"
    NO_MEDIA = "Requested movie: <b>{}</b>\n\n<b>Not available " \
               "Right Now</b>\n<code>Possible Causes : 🤔\n\n⭕️ Not " \
               "released yet</code>\n⭕️ <a href='https://www.google.com/search?q={}'> Check Spelling in Google</a>\n" \
               "<code>⭕️ Try In Below Format\nEx: SpiderMan 2021 Telugu\n⭕ Send Request Msg @justwatch_movies</code>"
    BLOCK_LIST = ['http://', 'https://', '@', '#', 'bit.ly', 't.me', '/']
