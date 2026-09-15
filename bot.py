import os
import sys
import random
import asyncio
from datetime import datetime

from dotenv import load_dotenv
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

from catalog import (
    get_products,
    random_product,
    telegram_product_text,
    product_count,
    approved_product_count,
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL = os.getenv("TELEGRAM_CHANNEL")
SUPPORT = os.getenv("SUPPORT_USERNAME")
STORE_URL = os.getenv("STORE_URL")

if not all([TOKEN, CHANNEL, SUPPORT, STORE_URL]):
    raise RuntimeError("Missing environment variables")


POSTS = {
    "welcome": [
        """💸 MONEY MAKER WORLDWIDE

Welcome to the official MONEY MAKER channel.

⚡ Digital opportunities
📦 Product drops
🧠 Strategies
🌎 Online business resources
🔔 Store updates

👇 ENTER MONEY MAKER""",
    ],

    "store": [
        """🟢 MONEY MAKER STORE

The current catalog is online.

Explore the latest MONEY MAKER drops and digital resources.

👇 OPEN THE STORE""",

        """⚡ MONEY MAKER ACCESS

Browse the current catalog directly through the official store.

New drops and resources are available online.

👇 VIEW CATALOG""",
    ],

    "education": [
        """🧠 MONEY MAKER RULE

Information without execution produces nothing.

Research.
Understand.
Execute.
Measure.
Improve.

Then repeat.""",

        """⚡ EXECUTION > INFORMATION

Knowing something has little value until it becomes action.

Learn.
Test.
Measure.
Improve.""",

        """🌎 THINK GLOBAL

Digital products can reach a global audience.

Distribution matters.
Execution matters.
Consistency matters.""",

        """🧠 BUILD SYSTEMS

Manual work has limits.

Systems can operate repeatedly.

Build processes that keep working.""",
    ],

    "strategy": [
        """📈 MONEY MAKER STRATEGY

Don't depend on one source of traffic.

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

Every repetitive legitimate task should eventually become a system.

Content.
Distribution.
Analytics.
Support.
Operations.""",

        """📊 TEST EVERYTHING

Publish.
Measure.
Compare.
Improve.

Data beats assumptions.""",
    ],

    "faq": [
        """❓ WHERE IS THE STORE?

The official MONEY MAKER catalog is available through the button below.

👇 OPEN STORE""",

        """❓ NEED MORE INFORMATION?

Product information is available directly through MONEY MAKER.

For additional questions, contact Telegram support.

👇 CONTACT SUPPORT""",

        """🔐 SECURITY REMINDER

MONEY MAKER support will never need your:

• Seed phrase
• Private key
• Account password

Keep authentication credentials private.""",
    ],

    "support": [
        """💬 NEED HELP?

Questions about a product?
Need more information?
Not sure where to start?

Direct Telegram support is available.

👇 CONTACT SUPPORT""",

        """⚡ DIRECT SUPPORT

Need information before making a decision?

Contact MONEY MAKER directly through Telegram.

👇 TALK TO SUPPORT""",
    ],

    "cta": [
        """👀 EXPLORE MONEY MAKER

Browse the current catalog whenever you're ready.

👇 SEE WHAT'S AVAILABLE""",

        """💸 DON'T JUST SCROLL.

Explore.
Research.
Decide.

👇 MONEY MAKER STORE""",

        """⚡ YOUR NEXT MOVE STARTS HERE.

Browse the current MONEY MAKER catalog.

👇 ENTER""",
    ],
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
    ])


def find_product(name):
    for product in get_products():
        if product["name"].upper() == name.upper():
            return product

    raise RuntimeError(
        f"Product not found: {name}"
    )


async def publish_text(text, mode="both"):
    bot = Bot(token=TOKEN)

    sent = await bot.send_message(
        chat_id=CHANNEL,
        text=text,
        reply_markup=buttons(mode),
        disable_web_page_preview=True,
    )

    return sent


async def send_post(category):
    if category not in POSTS:
        raise RuntimeError(
            f"Unknown category: {category}"
        )

    text = random.choice(POSTS[category])

    if category in ("store", "cta"):
        mode = "store"

    elif category == "support":
        mode = "support"

    else:
        mode = "both"

    sent = await publish_text(
        text,
        mode
    )

    print(
        f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
        f"POSTED | "
        f"category={category} | "
        f"message_id={sent.message_id}"
    )


async def send_product(product=None):
    if product is None:
        product = random_product()

    text = telegram_product_text(product)

    sent = await publish_text(
        text,
        "store"
    )

    print(
        f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
        f"PRODUCT POSTED | "
        f"{product['name']} | "
        f"${product['price']} | "
        f"message_id={sent.message_id}"
    )


async def send_cashapp_daily():
    """
    Fixed daily product.

    This command is called by GitHub Actions
    once per day at 12:30 America/New_York.
    """

    product = find_product(
        "CASHAPP TRANSFER SAUCE"
    )

    await send_product(product)


async def send_evening():
    """
    Evening commercial slot.

    Uses the approved weighted catalog.
    CASHAPP TRANSFER SAUCE is excluded here
    because it already has its fixed daily slot.
    """

    products = [
        p for p in get_products()
        if p.get("auto_publish", False)
        and p.get("weight", 0) > 0
        and p["name"] != "CASHAPP TRANSFER SAUCE"
    ]

    if not products:
        await send_post("store")
        return

    weights = [
        p.get("weight", 1)
        for p in products
    ]

    product = random.choices(
        products,
        weights=weights,
        k=1
    )[0]

    await send_product(product)


async def send_night():
    category = random.choice([
        "cta",
        "support",
        "faq",
    ])

    await send_post(category)


async def test():
    bot = Bot(token=TOKEN)
    me = await bot.get_me()

    template_count = sum(
        len(items)
        for items in POSTS.values()
    )

    cashapp = find_product(
        "CASHAPP TRANSFER SAUCE"
    )

    print("=" * 60)
    print(" MONEY MAKER — US CONTENT ENGINE")
    print("=" * 60)

    print(f"Bot              : @{me.username}")
    print(f"Channel          : {CHANNEL}")
    print(f"Support          : @{SUPPORT}")
    print(f"Store            : {STORE_URL}")
    print(f"Templates        : {template_count}")
    print(f"Catalog products : {product_count()}")
    print(f"Auto products    : {approved_product_count()}")

    print()
    print("DAILY CASHAPP")
    print(
        f"{cashapp['name']} | "
        f"${cashapp['price']}"
    )

    print()
    print("US SCHEDULE")
    print("09:00 ET | EDUCATION")
    print("12:30 ET | CASHAPP DAILY")
    print("15:30 ET | STRATEGY")
    print("18:30 ET | PRODUCT ROTATION")
    print("21:30 ET | CTA / SUPPORT / FAQ")

    print("=" * 60)
    print("STATUS: READY")
    print("=" * 60)


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

    elif command == "education":
        await send_post("education")

    elif command == "strategy":
        await send_post("strategy")

    elif command == "faq":
        await send_post("faq")

    elif command == "support":
        await send_post("support")

    elif command == "cta":
        await send_post("cta")

    elif command == "product":
        await send_product()

    elif command == "cashapp_daily":
        await send_cashapp_daily()

    elif command == "evening":
        await send_evening()

    elif command == "night":
        await send_night()

    else:
        print()
        print("UNKNOWN COMMAND")
        print()
        print(
            "Use: test | welcome | store | "
            "education | strategy | faq | support | "
            "cta | product | cashapp_daily | "
            "evening | night"
        )


if __name__ == "__main__":
    asyncio.run(main())