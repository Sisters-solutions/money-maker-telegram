import os
import sys
import random
import asyncio
from datetime import datetime

from dotenv import load_dotenv
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")
SUPPORT = os.getenv("SUPPORT_USERNAME")
STORE_URL = os.getenv("STORE_URL")

if not all([TOKEN, CHANNEL, SUPPORT, STORE_URL]):
    raise RuntimeError("Missing variables in .env")


# ============================================================
# MONEY MAKER — CONTENT ENGINE
# ============================================================

POSTS = {

    "welcome": [
        """💸 MONEY MAKER WORLDWIDE

Welcome to the official Money Maker channel.

This is where we publish:
⚡ New drops
🌍 Digital opportunities
📦 Store updates
🧠 Strategies & information
🔔 Important announcements

Everything starts here.

👇 ENTER THE STORE""",

        """🌍 WELCOME TO MONEY MAKER

One channel.
One store.
New opportunities constantly.

Stay subscribed so you don't miss new releases and updates.

👇 Explore Money Maker"""
    ],

    "store": [
        """🟢 STORE IS LIVE

The MONEY MAKER catalog is available now.

Browse the current selection directly through the official store.

No searching.
No middlemen.

👇 OPEN THE STORE""",

        """💰 LOOKING FOR THE NEXT OPPORTUNITY?

The complete Money Maker catalog is online.

Browse what's currently available and choose what fits you.

👇 VIEW CATALOG"""
    ],

    "support": [
        """💬 NEED HELP?

Money Maker has direct Telegram support.

Questions about the catalog?
Need more information?
Not sure where to start?

Speak directly with support.

👇 CONTACT SUPPORT""",

        """⚡ DIRECT SUPPORT

Don't waste time guessing.

If you need information before making a decision, contact Money Maker directly.

👇 TALK TO SUPPORT"""
    ],

    "education": [
        """🧠 MONEY MAKER RULE #1

Information without execution produces nothing.

Find the opportunity.
Understand it.
Execute.
Measure.
Improve.

Then repeat.""",

        """⚡ SPEED MATTERS

Most people spend too much time searching and not enough time executing.

Research → Decide → Execute → Measure.

Keep moving.""",

        """🌍 THE INTERNET NEVER CLOSES

Markets operate globally.
Customers operate globally.
Opportunities appear globally.

Think beyond your local market."""
    ],

    "cta": [
        """👀 STILL WATCHING?

You can browse the Money Maker catalog whenever you're ready.

👇 SEE WHAT'S AVAILABLE""",

        """💸 DON'T JUST SCROLL.

Explore.
Research.
Take action.

👇 MONEY MAKER STORE""",

        """⚡ YOUR NEXT MOVE STARTS HERE.

Browse the current Money Maker catalog.

👇 ENTER"""
    ]
}


def buttons(mode="both"):

    store = InlineKeyboardButton(
        "🛒 VISIT STORE",
        url=STORE_URL
    )

    support = InlineKeyboardButton(
        "💬 CONTACT SUPPORT",
        url=f"https://t.me/{SUPPORT}"
    )

    channel = InlineKeyboardButton(
        "📢 MONEY MAKER CHANNEL",
        url="https://t.me/MoneyMakerWorldwide"
    )

    if mode == "store":
        return InlineKeyboardMarkup([
            [store],
            [support]
        ])

    if mode == "support":
        return InlineKeyboardMarkup([
            [support],
            [store]
        ])

    return InlineKeyboardMarkup([
        [store],
        [support],
        [channel]
    ])


async def send_post(category):

    if category not in POSTS:
        print(f"Unknown category: {category}")
        return

    bot = Bot(TOKEN)

    text = random.choice(POSTS[category])

    if category in ("store", "cta"):
        keyboard = buttons("store")

    elif category == "support":
        keyboard = buttons("support")

    else:
        keyboard = buttons("both")

    sent = await bot.send_message(
        chat_id=CHANNEL,
        text=text,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )

    print(
        f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
        f"POSTED | category={category} | "
        f"message_id={sent.message_id}"
    )


async def test():

    bot = Bot(TOKEN)

    me = await bot.get_me()

    print("=" * 55)
    print(" MONEY MAKER TELEGRAM ENGINE")
    print("=" * 55)
    print(f"Bot:      @{me.username}")
    print(f"Channel:  {CHANNEL}")
    print(f"Support:  @{SUPPORT}")
    print(f"Store:    {STORE_URL}")
    print("=" * 55)
    print("SYSTEM READY")


async def main():

    if len(sys.argv) < 2:
        await test()
        return

    command = sys.argv[1].lower()

    if command == "test":
        await test()

    elif command == "welcome":
        await send_post("welcome")

    elif command == "store":
        await send_post("store")

    elif command == "support":
        await send_post("support")

    elif command == "education":
        await send_post("education")

    elif command == "cta":
        await send_post("cta")

    elif command == "random":
        await send_post(
            random.choice(
                ["store", "support", "education", "cta"]
            )
        )

    else:
        print("Unknown command.")
        print(
            "Use: test | welcome | store | support | "
            "education | cta | random"
        )


if __name__ == "__main__":
    asyncio.run(main())