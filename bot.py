import os
import sys
import random
import asyncio
from datetime import datetime

from dotenv import load_dotenv
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

from catalog import (
    random_product,
    telegram_product_text,
    product_count,
)

# ============================================================
# MONEY MAKER — TELEGRAM CONTENT ENGINE
# ============================================================

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")
SUPPORT = os.getenv("SUPPORT_USERNAME")
STORE_URL = os.getenv("STORE_URL")

if not all([TOKEN, CHANNEL, SUPPORT, STORE_URL]):
    raise RuntimeError("Missing variables in .env")


# ============================================================
# CONTENT LIBRARY
# ============================================================

POSTS = {

    "welcome": [

        """💸 MONEY MAKER WORLDWIDE

Welcome to the official MONEY MAKER channel.

⚡ Digital opportunities
📦 Product drops
🧠 Strategies
🌎 Online business resources
🔔 Store updates

Stay connected.

👇 ENTER MONEY MAKER""",

        """🌍 WELCOME TO MONEY MAKER

One store.
One channel.
New opportunities and resources.

Follow the channel for catalog updates, product spotlights and new releases.

👇 EXPLORE MONEY MAKER""",
    ],


    "store": [

        """🟢 MONEY MAKER STORE

The catalog is online.

Browse the current selection directly through the official MONEY MAKER store.

👇 OPEN THE STORE""",

        """💰 EXPLORE MONEY MAKER

Browse the current MONEY MAKER catalog and discover what's available.

👇 VIEW CATALOG""",

        """⚡ STORE ACCESS

MONEY MAKER is available online.

Explore the current catalog from anywhere.

👇 ENTER THE STORE""",
    ],


    "support": [

        """💬 NEED HELP?

Direct Telegram support is available.

Questions about a product?
Need more information?
Not sure where to start?

👇 CONTACT SUPPORT""",

        """⚡ DIRECT SUPPORT

Need information before making a decision?

Contact MONEY MAKER directly through Telegram.

👇 TALK TO SUPPORT""",

        """💬 MONEY MAKER SUPPORT

Questions about the catalog or how the store works?

Speak directly with support.

👇 OPEN SUPPORT""",
    ],


    "education": [

        """🧠 MONEY MAKER RULE #1

Information without execution produces nothing.

Research.
Understand.
Execute.
Measure.
Improve.

Then repeat.""",

        """⚡ SPEED MATTERS

Most people spend too much time searching and not enough time executing.

Research → Decide → Execute → Measure.""",

        """🌎 THINK GLOBAL

The internet doesn't operate inside borders.

Products can be digital.
Customers can be global.
Distribution can be instant.

Build accordingly.""",

        """🧠 EXECUTION > INFORMATION

Knowing something has little value until it becomes action.

Learn.
Test.
Measure.
Improve.""",

        """⚡ BUILD SYSTEMS

Manual work has limits.

Systems can operate repeatedly.

The goal isn't simply to work harder.

Build processes that keep working.""",

        """🌍 ONLINE BUSINESS PRINCIPLE

Distribution matters.

A great product nobody sees produces nothing.

Product + Distribution + Execution.""",
    ],


    "strategy": [

        """📈 MONEY MAKER STRATEGY

Don't depend on one source of traffic.

Build multiple distribution channels.

Telegram.
Short-form content.
Search.
Communities.
Direct traffic.

Attention is an asset.""",

        """🧠 BUSINESS SYSTEM

TRAFFIC
↓
OFFER
↓
CONVERSION
↓
DELIVERY
↓
RETENTION

Improve every stage.""",

        """⚡ AUTOMATION

Every repetitive task should eventually become a system.

Content.
Distribution.
Analytics.
Customer support.
Operations.

Automation creates leverage.""",

        """📊 TEST EVERYTHING

Don't guess what works.

Publish.
Measure.
Compare.
Improve.

Data beats assumptions.""",

        """🌎 DISTRIBUTION

The internet gives businesses access to a global audience.

The challenge isn't access.

The challenge is earning attention.""",
    ],


    "faq": [

        """❓ MONEY MAKER FAQ

WHERE IS THE STORE?

The official MONEY MAKER catalog is available through the button below.

👇 OPEN STORE""",

        """❓ NEED MORE INFORMATION?

Each product has its own description inside MONEY MAKER.

For additional questions, direct Telegram support is available.

👇 CONTACT SUPPORT""",

        """🔐 SECURITY REMINDER

MONEY MAKER support will never need your:

• Seed phrase
• Private key
• Account password

Keep authentication credentials private.""",

        """❓ HOW DO I CONTACT MONEY MAKER?

Direct support is available through Telegram.

Use the button below.

👇 CONTACT SUPPORT""",
    ],


    "cta": [

        """👀 STILL WATCHING?

Explore the MONEY MAKER catalog whenever you're ready.

👇 SEE WHAT'S AVAILABLE""",

        """💸 DON'T JUST SCROLL.

Explore.
Research.
Decide.

👇 MONEY MAKER STORE""",

        """⚡ YOUR NEXT MOVE STARTS HERE.

Browse the current MONEY MAKER catalog.

👇 ENTER""",

        """🌎 MONEY MAKER

The store is online.

Explore the current catalog.

👇 OPEN STORE""",
    ],
}


# ============================================================
# BUTTONS
# ============================================================

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
            [support],
        ])

    if mode == "support":
        return InlineKeyboardMarkup([
            [support],
            [store],
        ])

    return InlineKeyboardMarkup([
        [store],
        [support],
        [channel],
    ])


# ============================================================
# SEND STANDARD POST
# ============================================================

async def send_post(category):

    if category not in POSTS:
        print(f"Unknown category: {category}")
        return

    bot = Bot(token=TOKEN)

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
        disable_web_page_preview=True,
    )

    print(
        f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
        f"POSTED | "
        f"category={category} | "
        f"message_id={sent.message_id}"
    )


# ============================================================
# PRODUCT SPOTLIGHT
# ============================================================

async def send_product():

    product = random_product()

    text = telegram_product_text(product)

    bot = Bot(token=TOKEN)

    sent = await bot.send_message(
        chat_id=CHANNEL,
        text=text,
        reply_markup=buttons("store"),
        disable_web_page_preview=True,
    )

    print(
        f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
        f"PRODUCT POSTED | "
        f"{product['name']} | "
        f"${product['price']} | "
        f"message_id={sent.message_id}"
    )


# ============================================================
# ROTATING CONTENT
# ============================================================

async def send_random():

    categories = [
        "education",
        "strategy",
        "faq",
        "store",
        "support",
        "cta",
        "product",
    ]

    category = random.choice(categories)

    if category == "product":
        await send_product()
    else:
        await send_post(category)


# ============================================================
# SYSTEM TEST
# ============================================================

async def test():

    bot = Bot(token=TOKEN)

    me = await bot.get_me()

    template_count = sum(
        len(items)
        for items in POSTS.values()
    )

    print("=" * 60)
    print(" MONEY MAKER — CONTENT ENGINE")
    print("=" * 60)

    print(f"Bot       : @{me.username}")
    print(f"Channel   : {CHANNEL}")
    print(f"Support   : @{SUPPORT}")
    print(f"Store     : {STORE_URL}")

    print(f"Categories: {len(POSTS)}")
    print(f"Templates : {template_count}")
    print(f"Products  : {product_count()}")

    print("=" * 60)
    print("STATUS: READY")
    print("=" * 60)


# ============================================================
# COMMAND ROUTER
# ============================================================

async def main():

    if len(sys.argv) < 2:
        await test()
        return

    command = sys.argv[1].lower().strip()

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

    elif command == "strategy":
        await send_post("strategy")

    elif command == "faq":
        await send_post("faq")

    elif command == "cta":
        await send_post("cta")

    elif command == "product":
        await send_product()

    elif command == "random":
        await send_random()

    else:
        print()
        print("UNKNOWN COMMAND")
        print()
        print(
            "Use: test | welcome | store | support | "
            "education | strategy | faq | cta | "
            "product | random"
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    asyncio.run(main())