from telegram.ext import Updater, CommandHandler
import subprocess

TELEGRAM_TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

def start(update, context):
    update.message.reply_text("أرسل /osint [username] لبدء جمع المعلومات من Instagram.")

def osint(update, context):
    if len(context.args) != 1:
        update.message.reply_text("الرجاء إرسال اسم مستخدم واحد فقط.\nمثال: /osint nasa")
        return

    username = context.args[0]
    cmd = f"cd osintgram && python3 main.py {username} --command followers"

    update.message.reply_text("جارٍ تنفيذ الأمر، الرجاء الانتظار...")
    try:
        result = subprocess.getoutput(cmd)
        if len(result) > 4000:
            result = result[:3990] + "...\n[Output Truncated]"
        update.message.reply_text(result)
    except Exception as e:
        update.message.reply_text(f"حدث خطأ أثناء التنفيذ: {e}")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("osint", osint))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
