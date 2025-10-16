import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🔒 التوكن الخاص بالبوت (لا تشارك هذا النص علناً)
TOKEN = os.getenv("TOKEN")
PORT = int(os.environ.get("PORT", "8443"))
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

# ==============================
# 🎥 ملفات الفيديو
# ==============================

# --- SUGO ---
SUGO_VIDEO_1 = "BAACAgQAAxkBAANUaOLahrcQ1E6y_f3wSHJvUCYGI6IAAuIaAAKgEBBTz0AhDJV87mE2BA"
SUGO_VIDEO_2 = "BAACAgQAAxkBAANVaOLahuFCLOqxK4qYSVUn6s7-OaoAAugaAAKgEBBTnr9ngJcIq4U2BA"
SUGO_VIDEO_3 = "BAACAgQAAxkBAANWaOLahoyhojLg7mXhEnLppB9GeBQAAusaAAKgEBBTDg6__l6xKPY2BA"

# --- SOMATCH ---
SOMATCH_VIDEO_1 = "BAACAgQAAxkBAANXaOLahr7xZGr4xfapCnELxrPo8fYAAu4aAAKgEBBTpk1D0pJdrBc2BA"
SOMATCH_VIDEO_2 = "BAACAgQAAxkBAANYaOLahk0THhgX_NYIKS03iHhpW-EAAoQaAAIgChBTbPHgRmNBVko2BA"
SOMATCH_VIDEO_3 = "BAACAgQAAxkBAANZaOLahr4GPJYAAedLPNk-sMEAAQStDAAC8RoAAqAQEFPEI53utATwkDYE"

# ==============================
# 📝 النصوص
# ==============================

COMMON_RULES = """⚠️ شروط هامة:
1️⃣ ما يكون عند البنت مشكلة تحكي مع داعمين (شباب).
2️⃣ 🔴 ملاحظة: ما في أي شيء حقيقي بيظهر عن البنت للداعم (✨ هويتك الحقيقية مخفية ✨)."""

APPS_DIFF = """🤔 الفرق بينهما:

1️⃣ المحادثة بالـ 💎 Sugo مدفوعة بالكامل.
2️⃣ أما في 💜 Somatch، أول 25 رسالة فقط مدفوعة للبنت من قبل المستخدم الجديد حصراً.
3️⃣ الـ Somatch يعتمد على الرومات أكثر 🎤.
4️⃣ الـ Somatch أكثر سهولة من حيث النظام 🌸."""

DIFF_NOTICE = "✅ أنتم الآن علمتم ما الفرق بينهما، يرجى الضغط مرة أخرى على التطبيق المختار."

# --- SUGO ---
SUGO_CAPTION_1 = "🎥 خطوة 1 — طريقة إنشاء الحساب بالـ Sugo"
SUGO_TEXT_1_1 = """💡 طرق حل بعض المشاكل:

1️⃣ إذا كان عندك حساب Sugo مضاف مسبقًا على جهازك، لازم تعملي تقديم من جهاز آخر. وبعد القبول (عادةً خلال 6 ساعات) بتقدري ترجعي تفتحيها على موبايلك الأساسي بدون أي مشاكل.

2️⃣ 🔴 ملاحظة: إذا سبق ووثقتِ حساب Sugo (حتى من موبايل مختلف)، فالحل إنك تخلي بنت تانية تقوم بعملية التوثيق عنك."""
SUGO_CAPTION_2 = "🎥 خطوة 2 — طريقة الانضمام إلى الوكالة وتفعيل الحساب"
SUGO_TEXT_2 = """⚠️ شروط التوثيق "هام جداً":

1️⃣ إضاءة واضحة وجيدة 💡.
2️⃣ العمر لازم يكون فوق 18 سنة 🎂.
3️⃣ التوثيق حصراً عن طريق بنت 👩، الشب ما بيقدر يوثق."""
SUGO_CAPTION_3 = "🎥 خطوة 3 — الفيديو الأخير"
SUGO_FINAL_TEXT = "هاد المعرف اللي رح تبعتوا عليه معلومات التواصل متل ما ذكرت بالفيديو @Blueberrykity"

# --- SOMATCH ---
SOMATCH_CAPTION_1 = "🎥 خطوة 1 — طريقة إنشاء الحساب بالـ Somatch"
SOMATCH_TEXT_1_1 = """💡 طرق حل بعض المشاكل:

1️⃣ إذا كان عندك حساب Somatch مضاف مسبقًا على جهازك، لازم تعملي تقديم من جهاز آخر. وبعد القبول (عادةً خلال 6 ساعات) بتقدري ترجعي تفتحيها على موبايلك الأساسي بدون أي مشاكل.

2️⃣ 🔴 ملاحظة: إذا سبق ووثقتِ حساب Somatch (حتى من موبايل مختلف)، فالحل إنك تخلي بنت تانية تقوم بعملية التوثيق عنك."""
SOMATCH_CAPTION_2 = "🎥 خطوة 2 — طريقة الانضمام إلى الوكالة وتفعيل الحساب"
SOMATCH_TEXT_2 = """⚠️ شروط التوثيق "هام جداً":

1️⃣ إضاءة واضحة وجيدة 💡.
2️⃣ العمر لازم يكون فوق 18 سنة 🎂.
3️⃣ التوثيق حصراً عن طريق بنت 👩، الشب ما بيقدر يوثق."""
SOMATCH_CAPTION_3 = "🎥 خطوة 3 — الفيديو الأخير"
SOMATCH_FINAL_TEXT = "هاد المعرف اللي رح تبعتوا عليه معلومات التواصل متل ما ذكرت بالفيديو @Blueberrykity"

# ==============================
# روابط التطبيقات
# ==============================
SUGO_PLAY_LINK = "https://play.google.com/store/apps/details?id=com.voicemaker.android"
SOMATCH_PLAY_LINK = "https://play.google.com/store/apps/details?id=com.somatch.android"

# ==============================
# القوائم
# ==============================
def main_menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🌍 اختر دولة", callback_data="choose_country")]])

def country_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇸🇾 سوريا", callback_data="syria")],
        [InlineKeyboardButton("🌍 باقي الدول", callback_data="other")],
    ])

def syria_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📶 نت سوري", callback_data="net_syria")],
        [InlineKeyboardButton("🛰️ نت فضائي (تركي)", callback_data="net_turkey")],
        [InlineKeyboardButton("⬅️ رجوع", callback_data="main")],
    ])

def apps_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Sugo", callback_data="sugo_info")],
        [InlineKeyboardButton("💜 Somatch", callback_data="somatch_info")],
        [InlineKeyboardButton("⬅️ رجوع", callback_data="syria")],
    ])

def apps_final_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Sugo", callback_data="sugo_link")],
        [InlineKeyboardButton("💜 Somatch", callback_data="somatch_link")],
    ])

def net_turkey_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💜 Somatch", callback_data="somatch_link")],
        [InlineKeyboardButton("⬅️ رجوع", callback_data="syria")],
    ])

def other_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Sugo", callback_data="sugo_info_other")],
        [InlineKeyboardButton("💜 Somatch", callback_data="somatch_info_other")],
        [InlineKeyboardButton("⬅️ رجوع", callback_data="main")],
    ])

# ==============================
# ⚙️ معالج الأزرار
# ==============================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # --- القوائم الرئيسية ---
    if query.data == "choose_country":
        await query.edit_message_text("اختر دولتك 🌍:", reply_markup=country_menu())
        return
    if query.data == "main":
        await query.edit_message_text("مرحباً 👋، تفضل من القائمة:", reply_markup=main_menu())
        return
    if query.data == "syria":
        await query.edit_message_text("🇸🇾 اختر نوع الإنترنت:", reply_markup=syria_menu())
        return
    if query.data == "other":
        await query.message.reply_text(f"{COMMON_RULES}\n\nالرجاء اختيار التطبيق:", reply_markup=other_menu())
        return

    # --- نت سوري ---
    if query.data == "net_syria":
        await query.message.reply_text(COMMON_RULES)
        await query.message.reply_text("اختر التطبيق 📱:", reply_markup=apps_menu())
        return

    # --- عرض الفرق بين التطبيقات ---
    if query.data in ["sugo_info", "somatch_info", "sugo_info_other", "somatch_info_other"]:
        await query.message.reply_text(APPS_DIFF)
        await query.message.reply_text(DIFF_NOTICE, reply_markup=apps_final_menu())
        return

    # --- نت فضائي (تركي) ---
    if query.data == "net_turkey":
        await query.message.reply_text(COMMON_RULES)
        await query.message.reply_text("الخيار المتاح فقط:", reply_markup=net_turkey_menu())
        return

    # --- روابط التطبيقات ---
    if query.data == "sugo_link":
        text = f"💎 تطبيق Sugo للتسجيل:\n{SUGO_PLAY_LINK}\n\nعند تحميل التطبيق ⬆️ يرجى الضغط على تم"
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("✅ تم", callback_data="sugo_confirm")]])
        await query.message.reply_text(text, reply_markup=keyboard)
        return

    if query.data == "somatch_link":
        text = f"💜 تطبيق Somatch للتسجيل:\n{SOMATCH_PLAY_LINK}\n\nعند تحميل التطبيق ⬆️ يرجى الضغط على تم"
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("✅ تم", callback_data="somatch_confirm")]])
        await query.message.reply_text(text, reply_markup=keyboard)
        return

    # --- خطوات SUGO ---
    if query.data == "sugo_confirm":
        await query.message.reply_text("📌 لدينا ثلاث خطوات للتسجيل، يرجى الالتزام بتطبيقها بالتسلسل:")
        await query.message.reply_video(video=SUGO_VIDEO_1, caption=SUGO_CAPTION_1)
        await query.message.reply_text(SUGO_TEXT_1_1)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("✅ الخطوة التالية", callback_data="sugo_step2")]])
        await query.message.reply_text("اضغط للمتابعة ➡️", reply_markup=keyboard)
        return

    if query.data == "sugo_step2":
        await query.message.reply_video(video=SUGO_VIDEO_2, caption=SUGO_CAPTION_2)
        await query.message.reply_text(SUGO_TEXT_2)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("✅ الخطوة التالية", callback_data="sugo_step3")]])
        await query.message.reply_text("اضغط للمتابعة ➡️", reply_markup=keyboard)
        return

    if query.data == "sugo_step3":
        await query.message.reply_video(video=SUGO_VIDEO_3, caption=SUGO_CAPTION_3)
        await query.message.reply_text(SUGO_FINAL_TEXT)
        return

    # --- خطوات SOMATCH ---
    if query.data == "somatch_confirm":
        await query.message.reply_text("📌 لدينا ثلاث خطوات للتسجيل، يرجى الالتزام بتطبيقها بالتسلسل:")
        await query.message.reply_video(video=SOMATCH_VIDEO_1, caption=SOMATCH_CAPTION_1)
        await query.message.reply_text(SOMATCH_TEXT_1_1)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("✅ الخطوة التالية", callback_data="somatch_step2")]])
        await query.message.reply_text("اضغط للمتابعة ➡️", reply_markup=keyboard)
        return

    if query.data == "somatch_step2":
        await query.message.reply_video(video=SOMATCH_VIDEO_2, caption=SOMATCH_CAPTION_2)
        await query.message.reply_text(SOMATCH_TEXT_2)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("✅ الخطوة التالية", callback_data="somatch_step3")]])
        await query.message.reply_text("اضغط للمتابعة ➡️", reply_markup=keyboard)
        return

    if query.data == "somatch_step3":
        await query.message.reply_video(video=SOMATCH_VIDEO_3, caption=SOMATCH_CAPTION_3)
        await query.message.reply_text(SOMATCH_FINAL_TEXT)
        return

    # --- حالة افتراضية ---
    await query.message.reply_text("عذراً، لم أفهم هذا الأمر. الرجاء استخدام الأزرار المتاحة فقط.")

# ==============================
# 🚀 بدء التشغيل
# ==============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 أهلاً بك! تفضل بالاختيار:", reply_markup=main_menu())

def main():
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    # Run the bot using webhook
    if WEBHOOK_URL:
        app.run_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=TOKEN,
                        webhook_url=f"{WEBHOOK_URL}/{TOKEN}")
        logger.info(f"Webhook listening on port {PORT} at {WEBHOOK_URL}/{TOKEN}")
    else:
        app.run_polling()
        logger.info("Bot is running with polling...")

if __name__ == "__main__":
    main()

