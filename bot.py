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
    raise RuntimeError("Missing required environment variables.")


# ============================================================
# MONEY MAKER — CONTENT ENGINE
# Market: United States
# Language: English
# ============================================================

CONTENT = {

    # --------------------------------------------------------
    # WELCOME
    # --------------------------------------------------------

    "welcome": [

        """💸 MONEY MAKER WORLDWIDE

Welcome to the official MONEY MAKER channel.

Here you'll find:

⚡ New digital drops
📦 Catalog updates
🧠 Useful strategies
🔍 Product spotlights
💬 Direct support

Stay connected.

👇 EXPLORE MONEY MAKER""",

        """🌎 WELCOME TO MONEY MAKER

Built for people who move fast.

New releases.
Digital resources.
Store updates.
Practical information.

Everything starts here.

👇 ENTER THE STORE""",

        """⚡ MONEY MAKER IS LIVE

This channel connects you directly to the MONEY MAKER ecosystem.

📦 Browse the catalog
🔔 Follow new releases
🧠 Learn something useful
💬 Contact support directly

👇 START HERE"""
    ],


    # --------------------------------------------------------
    # STORE
    # --------------------------------------------------------

    "store": [

        """🟢 STORE IS LIVE

The MONEY MAKER catalog is online.

Browse the current selection and explore what's available.

👇 OPEN THE STORE""",

        """💰 LOOKING FOR YOUR NEXT DIGITAL RESOURCE?

The MONEY MAKER catalog is available 24/7.

Browse the current selection directly through the official store.

👇 VIEW CATALOG""",

        """🌎 MONEY MAKER MARKETPLACE

One place.
Multiple digital resources.
Direct access to the complete catalog.

See what's currently available.

👇 BROWSE THE STORE""",

        """📦 CATALOG CHECK

Have you checked the latest MONEY MAKER selection?

The store is open and accessible worldwide.

👇 EXPLORE THE CATALOG""",

        """⚡ DON'T WASTE TIME SEARCHING

We've organized the MONEY MAKER catalog in one place.

Browse.
Compare.
Choose what fits your needs.

👇 ENTER STORE""",

        """💻 DIGITAL CATALOG ONLINE

MONEY MAKER gives you direct access to the current product selection.

No endless searching.

👇 SEE WHAT'S AVAILABLE""",

        """🔎 WHAT'S INSIDE MONEY MAKER?

The fastest way to find out is simple:

Open the catalog and explore it yourself.

👇 VIEW THE STORE"""
    ],


    # --------------------------------------------------------
    # EDUCATION
    # --------------------------------------------------------

    "education": [

        """🧠 MONEY MAKER RULE #1

Information without execution produces nothing.

Research.
Decide.
Execute.
Measure.
Improve.

Then repeat.""",

        """⚡ SPEED MATTERS

Research forever and nothing happens.

A better system:

1. Find the opportunity
2. Understand it
3. Test it
4. Measure the result
5. Improve

Execution creates information.""",

        """🌎 THINK GLOBAL

The internet doesn't care where you live.

Markets are global.
Customers are global.
Information is global.

Your thinking should be too.""",

        """🧠 BUILD SYSTEMS, NOT CHAOS

A repeatable process beats random effort.

Find what works.
Document it.
Improve it.
Repeat it.""",

        """📊 DATA > GUESSING

Don't assume something works.

Measure it.

Clicks.
Conversion.
Cost.
Time.
Result.

Good decisions start with real information.""",

        """⚡ EXECUTION RULE

You don't need 100 ideas.

You need one useful idea executed properly.

Focus creates speed.""",

        """🔍 OPPORTUNITY IS OFTEN HIDDEN IN INFORMATION

Two people can look at the same market and see completely different things.

The difference?

Research.
Timing.
Execution.""",

        """💡 SMALL TESTS. FAST FEEDBACK.

Before committing heavily to an idea:

Test.
Observe.
Adjust.

Fast feedback can save enormous amounts of time.""",

        """📈 THE COMPOUND EFFECT

One improvement doesn't look important.

But improving something repeatedly changes the entire result.

Better research.
Better execution.
Better conversion.
Better systems.""",

        """🧠 DON'T CONFUSE ACTIVITY WITH PROGRESS

Being busy isn't the goal.

Ask one question:

Did today's work move the objective forward?""",

        """🌎 THE INTERNET RUNS 24/7

Your systems don't always need to depend on your physical presence.

Automation can handle repetitive work while you focus on decisions.""",

        """⚙️ AUTOMATE THE REPETITIVE

If you're doing the exact same task repeatedly, ask:

Can this become a system?

Automation creates leverage when the underlying process is useful."""
    ],


    # --------------------------------------------------------
    # STRATEGY
    # --------------------------------------------------------

    "strategy": [

        """🎯 SIMPLE BUSINESS FILTER

Before spending time on an opportunity, ask:

Is there demand?
Can I reach the customer?
Can it scale?
Can the process be repeated?

Simple questions eliminate bad ideas quickly.""",

        """📊 TRACK THE FUNNEL

Attention → Click → Visit → Decision → Conversion

If results are weak, identify where people are dropping.

Fix the bottleneck instead of guessing.""",

        """⚡ REMOVE FRICTION

Every unnecessary step reduces conversion.

Make the path clear:

Discover → Understand → Decide → Act.""",

        """🧠 ATTENTION IS ONLY STEP ONE

Traffic without a clear destination doesn't accomplish much.

Every piece of content should have a purpose.""",

        """📈 OPTIMIZE WHAT ALREADY WORKS

Finding something that works is only the beginning.

Then ask:

Can it be faster?
Can it be clearer?
Can it reach more people?
Can it convert better?"""
    ],


    # --------------------------------------------------------
    # FAQ
    # --------------------------------------------------------

    "faq": [

        """❓ WHERE CAN I SEE THE MONEY MAKER CATALOG?

The complete current selection is available through the official store.

👇 OPEN STORE""",

        """❓ NEED MORE INFORMATION?

If you're unsure which option fits what you're looking for, contact support directly.

👇 TALK TO SUPPORT""",

        """❓ IS THE STORE AVAILABLE 24/7?

Yes.

The MONEY MAKER website can be accessed online at any time.

👇 VISIT STORE""",

        """❓ WHERE DO I GET MONEY MAKER UPDATES?

Right here.

Stay subscribed to the official channel for new releases, information and catalog updates.""",

        """❓ HAVE A QUESTION BEFORE MAKING A DECISION?

Ask first.

Direct MONEY MAKER support is available through Telegram.

👇 CONTACT SUPPORT"""
    ],


    # --------------------------------------------------------
    # SUPPORT
    # --------------------------------------------------------

    "support": [

        """💬 NEED HELP?

Have a question about the catalog?

Contact MONEY MAKER support directly.

👇 TALK TO SUPPORT""",

        """⚡ DIRECT SUPPORT

Don't waste time guessing.

If you need more information, contact us directly through Telegram.

👇 CONTACT SUPPORT""",

        """💬 QUESTIONS?

We're here.

For information about MONEY MAKER products or the store, use the direct support channel below.

👇 MESSAGE SUPPORT""",

        """🧠 NOT SURE WHERE TO START?

Browse the catalog first.

If you still have questions, contact MONEY MAKER directly.

👇 GET SUPPORT""",

        """📩 MONEY MAKER SUPPORT

Need clarification before making a decision?

Use our direct Telegram contact.

👇 SPEAK WITH SUPPORT"""
    ],


    # --------------------------------------------------------
    # CTA
    # --------------------------------------------------------

    "cta": [

        """👀 STILL WATCHING?

Take a look at the MONEY MAKER catalog.

👇 SEE WHAT'S AVAILABLE""",

        """⚡ YOUR NEXT MOVE STARTS WITH INFORMATION.

Explore the current MONEY MAKER selection.

👇 OPEN THE STORE""",

        """💸 DON'T JUST SCROLL.

Explore.
Research.
Decide.

👇 MONEY MAKER STORE""",

        """🔎 SEE IT FOR YOURSELF

The current MONEY MAKER catalog is one click away.

👇 VIEW CATALOG""",

        """🌎 READY TO EXPLORE?

Enter MONEY MAKER and browse the current selection.

👇 VISIT STORE""",

        """⚡ ONE CLICK.

That's all it takes to see the complete MONEY MAKER catalog.

👇 ENTER STORE""",

        """📦 WHAT'S AVAILABLE RIGHT NOW?

Check the official MONEY MAKER store.

👇 BROWSE NOW"""
    ]
}


# ============================================================
# BUTTON SYSTEM
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
        [support]
    ])


# ============================================================
# CHOOSE BUTTON TYPE
# ============================================================

def keyboard_for(category):

    if category in (
        "store",
        "cta"
    ):
        return buttons("store")

    if category in (
        "support",
        "faq"
    ):
        return buttons("support")

    return buttons("both")


# ============================================================
# PUBLISH
# ============================================================

async def send_post(category):

    if category not in CONTENT:
        raise ValueError(
            f"Unknown content category: {category}"
        )

    bot = Bot(token=TOKEN)

    text = random.choice(
        CONTENT[category]
    )

    keyboard = keyboard_for(category)

    sent = await bot.send_message(
        chat_id=CHANNEL,
        text=text,
        reply_markup=keyboard,
        disable_web_page_preview=True
    )

    print(
        f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
        f"POSTED | "
        f"category={category} | "
        f"message_id={sent.message_id}"
    )


# ============================================================
# RANDOM ENGINE
# ============================================================

async def send_random():

    # Weighted distribution.
    # Store/CTA remain commercially important,
    # but the channel isn't just constant advertising.

    categories = [
        "education",
        "education",
        "strategy",
        "strategy",
        "faq",
        "store",
        "cta",
        "support"
    ]

    category = random.choice(categories)

    await send_post(category)


# ============================================================
# SYSTEM TEST
# ============================================================

async def system_test():

    bot = Bot(token=TOKEN)

    me = await bot.get_me()

    total_posts = sum(
        len(posts)
        for posts in CONTENT.values()
    )

    print()
    print("=" * 62)
    print(" MONEY MAKER — CONTENT ENGINE")
    print("=" * 62)
    print(f"Bot       : @{me.username}")
    print(f"Channel   : {CHANNEL}")
    print(f"Support   : @{SUPPORT}")
    print(f"Store     : {STORE_URL}")
    print(f"Categories: {len(CONTENT)}")
    print(f"Templates : {total_posts}")
    print("=" * 62)
    print("STATUS: READY")
    print("=" * 62)
    print()


# ============================================================
# COMMAND ROUTER
# ============================================================

async def main():

    if len(sys.argv) < 2:
        await system_test()
        return

    command = sys.argv[1].lower().strip()

    if command == "test":
        await system_test()

    elif command == "random":
        await send_random()

    elif command in CONTENT:
        await send_post(command)

    else:
        print()
        print(f"Unknown command: {command}")
        print()
        print(
            "Available commands: "
            "test | welcome | store | education | "
            "strategy | faq | support | cta | random"
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    asyncio.run(main())