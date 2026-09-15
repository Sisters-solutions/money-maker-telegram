import asyncio
import random
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from bot import send_post


# ============================================================
# MONEY MAKER — US TELEGRAM AUTOMATION ENGINE
# Primary market: United States
# Master timezone: US Eastern Time
# Automatically handles EST / EDT
# ============================================================

TIMEZONE = "America/New_York"

last_category = None


# ============================================================
# PUBLISH A SPECIFIC CATEGORY
# ============================================================

def publish(category):
    global last_category

    try:
        now = datetime.now()

        print(
            f"[{now:%Y-%m-%d %H:%M:%S}] "
            f"Starting scheduled post | category={category}"
        )

        asyncio.run(send_post(category))

        last_category = category

        print(
            f"[{datetime.now():%Y-%m-%d %H:%M:%S}] "
            f"Completed | category={category}"
        )

    except Exception as e:
        print(
            f"[ERROR] Could not publish "
            f"category={category} | {e}"
        )


# ============================================================
# ROTATING CONTENT
# Prevents the same category from being selected twice
# consecutively by the rotating job.
# ============================================================

def publish_rotating():
    global last_category

    categories = [
        "education",
        "store",
        "support",
        "cta"
    ]

    available = [
        category
        for category in categories
        if category != last_category
    ]

    if not available:
        available = categories

    selected = random.choice(available)

    publish(selected)


# ============================================================
# SCHEDULER
# ============================================================

scheduler = BlockingScheduler(
    timezone=TIMEZONE
)


# ------------------------------------------------------------
# 09:00 ET
# Morning / education
#
# New York:    09:00
# Chicago:     08:00
# Denver:      07:00
# Los Angeles: 06:00
# ------------------------------------------------------------

scheduler.add_job(
    publish,
    CronTrigger(
        hour=9,
        minute=0,
        timezone=TIMEZONE
    ),
    args=["education"],
    id="us_morning",
    replace_existing=True
)


# ------------------------------------------------------------
# 12:30 ET
# Store / catalog
#
# New York:    12:30
# Chicago:     11:30
# Denver:      10:30
# Los Angeles: 09:30
# ------------------------------------------------------------

scheduler.add_job(
    publish,
    CronTrigger(
        hour=12,
        minute=30,
        timezone=TIMEZONE
    ),
    args=["store"],
    id="us_midday_store",
    replace_existing=True
)


# ------------------------------------------------------------
# 15:30 ET
# Rotating content
#
# New York:    15:30
# Chicago:     14:30
# Denver:      13:30
# Los Angeles: 12:30
# ------------------------------------------------------------

scheduler.add_job(
    publish_rotating,
    CronTrigger(
        hour=15,
        minute=30,
        timezone=TIMEZONE
    ),
    id="us_afternoon_rotation",
    replace_existing=True
)


# ------------------------------------------------------------
# 18:30 ET
# Commercial CTA
#
# New York:    18:30
# Chicago:     17:30
# Denver:      16:30
# Los Angeles: 15:30
# ------------------------------------------------------------

scheduler.add_job(
    publish,
    CronTrigger(
        hour=18,
        minute=30,
        timezone=TIMEZONE
    ),
    args=["cta"],
    id="us_evening_cta",
    replace_existing=True
)


# ------------------------------------------------------------
# 21:30 ET
# Support / late audience
#
# New York:    21:30
# Chicago:     20:30
# Denver:      19:30
# Los Angeles: 18:30
# ------------------------------------------------------------

scheduler.add_job(
    publish,
    CronTrigger(
        hour=21,
        minute=30,
        timezone=TIMEZONE
    ),
    args=["support"],
    id="us_night_support",
    replace_existing=True
)


# ============================================================
# STARTUP INFORMATION
# ============================================================

print()
print("=" * 62)
print(" MONEY MAKER — US TELEGRAM AUTOMATION ENGINE")
print("=" * 62)
print()
print("TARGET MARKET : UNITED STATES")
print("MASTER ZONE   : AMERICA/NEW_YORK (ET)")
print()
print("DAILY SCHEDULE")
print("-" * 62)
print("09:00 ET  | EDUCATION")
print("12:30 ET  | STORE")
print("15:30 ET  | ROTATING CONTENT")
print("18:30 ET  | CTA")
print("21:30 ET  | SUPPORT")
print("-" * 62)
print()
print("BOT     : @MoneyMakerSystem_bot")
print("CHANNEL : @MoneyMakerWorldwide")
print("SUPPORT : @MoneyMakerXXXL")
print()
print("AUTOMATION STATUS: RUNNING")
print()
print("Press CTRL+C to stop.")
print("=" * 62)
print()


# ============================================================
# RUN
# ============================================================

try:
    scheduler.start()

except (KeyboardInterrupt, SystemExit):

    print()
    print("=" * 62)
    print(" MONEY MAKER AUTOMATION STOPPED")
    print("=" * 62)