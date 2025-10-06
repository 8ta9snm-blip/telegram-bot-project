from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# التوكن الخاص بالبوت
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# مسارات ملفات الفيديو لكل تطبيق
SUGO_VIDEO_1 = "BAACAgQAAxkBAANUaOLahrcQ1E6y_f3wSHJvUCYGI6IAAuIaAAKgEBBTz0AhDJV87mE2BA"
SUGO_VIDEO_2 = "BAACAgQAAxkBAANVaOLahuFCLOqxK4qYSVUn6s7-OaoAAugaAAKgEBBTnr9ngJcIq4U2BA"
SUGO_VIDEO_3 = "BAACAgQAAxkBAANWaOLahoyhojLg7mXhEnLppB9GeBQAAusaAAKgEBBTDg6__l6xKPY2BA"

SOMATCH_VIDEO_1 = "BAACAgQAAxkBAANXaOLahr7xZGr4xfapCnELxrPo8fYAAu4aAAKgEBBTpk1D0pJdrBc2BA"
SOMATCH_VIDEO_2 = "BAACAgQAAxkBAANYaOLahk0THhgX_NYIKS03iHhpW-EAAoQaAAIgChBTbPHgRmNBVko2BA"
SOMATCH_VIDEO_3 = "BAACAgQAAxkBAANZaOLahr4GPJYAAedLPNk-sMEAAQStDAAC8RoAAqAQEFPEI53utATwkDYE"

# النصوص المرتبطة بكل فيديو
COMMON_RULES = """⚠️ شروط هامة:
1️⃣ ما يكون عند البنت مشكلة تحكي مع داعمين (شباب).
2️⃣ 🔴 ملاحظة: ما في أي شيء حقيقي بيظهر عن البنت للداعم (✨ هويتك الحقيقية مخفية ✨)."""

APPS_DIFF = """🤔 الفرق بينهما:

1️⃣ المحادثة بالـ 💎 Sugo مدفوعة بالكامل.
2️⃣ أما في 💜 Somatch، أول 25 رسالة فقط مدفوعة للبنت من قبل المستخدم الجديد حصراً.
3️⃣ الـ Somatch يعتمد على الرومات أكثر 🎤.
4️⃣ الـ Somatch أكثر سهولة من حيث النظام 🌸."""

DIFF_NOTICE = "✅ أنتم الآن علمتم ما الفرق بينهما، يرجى الضغط مرة أخرى على التطبيق المختار."

SUGO_CAPTION_1 = "🎥 خطوة 1 — طريقة إنشاء الحساب بالـ Sugo"
SUGO_TEXT_1_1 = """💡 طرق حل بعض المشاكل:

1️⃣ إذا كان عندك حساب Sugo مضاف مسبقًا على جهازك، لازم تعملي تقديم من جهاز آخر. وبعد القبول (عادةً خلال 6 ساعات) بتقدري ترجعي تفتحيه على موبايلك الأساسي بدون أي مشاكل.

2️⃣ 🔴 ملاحظة: إذا سبق ووثقتِ حساب Sugo (حتى من موبايل مختلف)، فالحل إنك تخلي بنت تانية تقوم بعملية التوثيق عنك."""

SUGO_CAPTION_2 = "🎥 خطوة 2 — طريقة الانضمام إلى الوكالة وتفعيل الحساب"
SUGO_TEXT_2 = """⚠️ شروط التوثيق "هام جداً":

1️⃣ إضاءة واضحة وجيدة 💡.
2️⃣ العمر لازم يكون فوق 18 سنة 🎂.
3️⃣ التوثيق حصراً عن طريق بنت 👩، الشب ما بيقدر يوثق."""

SUGO_CAPTION_3 = "🎥 خطوة 3 — الفيديو الأخير"
SUGO_FINAL_TEXT = "هاد المعرف اللي رح تبعتوا عليه معلومات التواصل متل ما ذكرت بالفيديو @Blueberrykity"

SOMATCH_CAPTION_1 = "🎥 خطوة 1 — طريقة إنشاء الحساب بالـ Somatch"
SOMATCH_TEXT_1_1 = """💡 طرق حل بعض المشاكل:

1️⃣ إذا كان عندك حساب Somatch مضاف مسبقًا على جهازك، لازم تعملي تقديم من جهاز آخر. وبعد القبول (عادةً خلال 6 ساعات) بتقدري ترجعي تفتحيه على موبايلك الأساسي بدون أي مشاكل.

2️⃣ 🔴 ملاحظة: إذا سبق ووثقتِ حساب Somatch (حتى من موبايل مختلف)، فالحل إنك تخلي بنت تانية تقوم بعملية التوثيق عنك."""

SOMATCH_CAPTION_2 = "🎥 خطوة 2 — طريقة الانضمام إلى الوكالة وتفعيل الحساب"
SOMATCH_TEXT_2 = """⚠️ شروط التوثيق "هام جداً":

1️⃣ إضاءة واضحة وجيدة 💡.
2️⃣ العمر لازم يكون فوق 18 سنة 🎂.
3️⃣ التوثيق حصراً عن طريق بنت 👩، الشب ما بيقدر يوثق."""

SOMATCH_CAPTION_3 = "🎥 خطوة 3 — الفيديو الأخير"
SOMATCH_FINAL_TEXT = "هاد المعرف اللي رح تبعتوا عليه معلومات التواصل متل ما ذكرت بالفيديو @Blueberrykity"

# القوائم

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
        [InlineKeyboardButton("💎 Sugo", callback_data="sugo_start")],
        [InlineKeyboardButton("💜 Somatch", callback_data="somatch_start")],
    ])

def net_turkey_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💜 Somatch", callback_data="somatch_start")],
        [InlineKeyboardButton("⬅️ رجوع", callback_data="syria")],
    ])

def other_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💎 Sugo", callback_data="sugo_info_other")],
        [InlineKeyboardButton("💜 Somatch", callback_data="somatch_info_other")],
        [InlineKeyboardButton("⬅️ رجوع", callback_data="main")],
    ])

# معالج الأزرار

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "choose_country":  
        await query.edit_message_text("اختر دولتك 🌍:", reply_markup=country_menu())  
        return  
    if query.data == "main":  
        await query.edit_message_text("مرحبا 👋، تفضل من القائمة:", reply_markup=main_menu())  
        return  
    if query.data == "syria":  
        await query.edit_message_text("🇸🇾 اختر نوع الإنترنت:", reply_markup=syria_menu())  
        return  
    if query.data == "other":  
        await query.edit_message_text(f"{COMMON_RULES}\nالرجاء اختيار التطبيق:", reply_markup=other_menu())  
        return  

    # نت سوري  
    if query.data == "net_syria":  
        await query.message.reply_text(COMMON_RULES)  
        await query.message.reply_text("اختر التطبيق 📱:", reply_markup=apps_menu())  
        return  
    if query.data in ["sugo_info", "somatch_info", "sugo_info_other", "somatch_info_other"]:  
        await query.message.reply_text(APPS_DIFF)  
        await query.message.reply_text(DIFF_NOTICE, reply_markup=apps_final_menu())  
        return  
    if query.data == "net_turkey":  
        await query.message.reply_text(COMMON_RULES)  
        await query.message.reply_text("الخيار المتاح فقط:", reply_markup=net_turkey_menu())  
        return  

    # --- خطوات SUGO ---  
    if query.data == "sugo_start":  
        await query.message.reply_text("📌 لدينا ثلاث خطوات للتسجيل يرجى الالتزام بتطبيقها حرفياً مع الحفاظ على تسلسلها")  
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
    if query.data == "somatch_start":  
        await query.message.reply_text("📌 لدينا ثلاث خطوات للتسجيل يرجى الالتزام بتطبيقها حرفياً مع الحفاظ على تسلسلها")  
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

    await query.message.reply_text("عذرًا، لم أفهم الأمر. الرجاء استخدام الأزرار المتاحة.")

# بدء التشغيل

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 أهلاً بك! تفضل بالاختيار:", reply_markup=main_menu())

def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
