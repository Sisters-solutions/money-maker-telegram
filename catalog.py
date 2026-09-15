import random


# ============================================================
# MONEY MAKER — MASTER CATALOG
# Names and prices match the storefront.
#
# auto_publish:
# True  = may appear automatically on Telegram
# False = remains in master catalog but is excluded from
#         automated Telegram advertising.
# ============================================================

PRODUCTS = [

    {
        "id": "mm1",
        "name": "CASHAPP TRANSFER SAUCE",
        "price": 200,
        "description": (
            "Beginner-friendly Cash App transfer workflow. "
            "Phone only, with step-by-step instructions and Telegram support."
        ),
        "weight": 12,
        "auto_publish": True,
    },

    {
        "id": "mm2",
        "name": "PAYPAL LOG",
        "price": 80,
        "description": "Ready-to-use PayPal workflow with Telegram Support",
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm3",
        "name": "VISA CC",
        "price": 60,
        "description": (
            "Visa business-spend workflow for cards. Built for online purchases, "
            "subscriptions, and payment-app organization with instant digital access."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm4",
        "name": "COINBASE LOG",
        "price": 80,
        "description": (
            "Coinbase workflow for accounts and wallets with instant access, "
            "beginner-friendly instructions, and full Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm5",
        "name": "CHASE LOG",
        "price": 80,
        "description": (
            "Chase banking workflow method. Delivered instantly with "
            "detailed instructions and Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm6",
        "name": "CASHAPP LOG",
        "price": 80,
        "description": (
            "Cash App workflow with a Basic Account. Ready to use with instant "
            "digital delivery and a beginner-friendly setup guide."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm7",
        "name": "LINKABLE CC",
        "price": 70,
        "description": (
            "Linkable card workflow. Built for supported payment apps, "
            "online purchases, subscriptions, and instant digital access."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm8",
        "name": "MASTERCARD CC",
        "price": 60,
        "description": (
            "Mastercard business-spend workflow for cards. Built for online "
            "purchases, recurring payments, and instant digital delivery."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm9",
        "name": "HIGH BALANCE DUMP",
        "price": 80,
        "description": (
            "High-balance cash-flow workflow. Delivered instantly with "
            "detailed instructions and Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm10",
        "name": "METAMASK LOG",
        "price": 50,
        "description": (
            "MetaMask wallet workflow with instant access, step-by-step "
            "instructions, and dedicated Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm11",
        "name": "OTP BOT",
        "price": 150,
        "description": (
            "OTP security-testing workflow. Includes instant digital access, "
            "a complete walkthrough, and Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm12",
        "name": "ID + HIGH BALANCE CC",
        "price": 80,
        "description": (
            "Identity and payment-control workflow. Includes instant digital "
            "access, setup instructions, and Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm13",
        "name": "BANK OF AMERICA LOG",
        "price": 50,
        "description": (
            "Bank of America banking workflow method. Delivered instantly "
            "with detailed instructions and beginner-friendly setup."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm14",
        "name": "HILTON HOTEL ACCOUNT",
        "price": 20,
        "description": (
            "Hilton account optimization workflow. Instant digital access "
            "with step-by-step setup and Telegram support."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm15",
        "name": "AIRBNB ACCOUNT",
        "price": 20,
        "description": (
            "Airbnb account workflow. Instant access with setup instructions, "
            "workflow guidance, and Telegram support."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm16",
        "name": "TRUST WALLET LOG",
        "price": 80,
        "description": (
            "Trust Wallet workflow for wallets with instant access, "
            "step-by-step instructions, and dedicated Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm17",
        "name": "WELLS FARGO",
        "price": 50,
        "description": (
            "Wells Fargo banking workflow method. Delivered instantly with "
            "detailed instructions and beginner-friendly setup."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm18",
        "name": "MONEYLION",
        "price": 20,
        "description": (
            "MoneyLion account workflow. Instant digital access with "
            "a simple beginner-friendly guide."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm19",
        "name": "AMEX LINKABLE CC",
        "price": 60,
        "description": (
            "Amex business-spend workflow for cards. Built for online payments, "
            "subscriptions, and payment-app organization with instant access."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm20",
        "name": "AMAZON ACCOUNTS",
        "price": 20,
        "description": (
            "Amazon account workflow. Instant digital access with setup "
            "instructions, order organization, and Telegram support."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm21",
        "name": "STOCKX ACCOUNTS",
        "price": 15,
        "description": (
            "StockX resale workflow. Instant access with product research, "
            "fee tracking, and Telegram support."
        ),
        "weight": 5,
        "auto_publish": True,
    },

    {
        "id": "mm22",
        "name": "ONLYFANS ACCOUNTS",
        "price": 15,
        "description": (
            "Creator account workflow. Instant access with setup guidance, "
            "content planning, and monetization tracking."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm23",
        "name": "GOAT ACCOUNT",
        "price": 20,
        "description": (
            "GOAT resale workflow. Instant access with sourcing guidance, "
            "fee tracking, and Telegram support."
        ),
        "weight": 5,
        "auto_publish": True,
    },

    {
        "id": "mm24",
        "name": "TARGET ACCOUNTS",
        "price": 15,
        "description": (
            "Target account and rewards workflow. Instant access with "
            "offer tracking and beginner-friendly setup."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm25",
        "name": "AMC ACCOUNTS",
        "price": 15,
        "description": (
            "AMC account and rewards workflow. Instant digital access "
            "with a simple setup guide."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm26",
        "name": "BEST BUY ACCOUNTS",
        "price": 15,
        "description": (
            "Best Buy account workflow. Instant access with rewards tracking, "
            "purchase organization, and Telegram support."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm27",
        "name": "EXXON GAS REWARDS",
        "price": 15,
        "description": (
            "Exxon rewards workflow. Instant access with points tracking "
            "and beginner-friendly instructions."
        ),
        "weight": 4,
        "auto_publish": True,
    },

    {
        "id": "mm28",
        "name": "WALMART ACCOUNTS",
        "price": 15,
        "description": (
            "Walmart account workflow. Instant access with order tracking, "
            "rewards organization, and Telegram support."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm29",
        "name": "2FA SPOOFER OPSEC",
        "price": 150,
        "description": (
            "2FA simulation and OPSEC training workflow. Instant access "
            "with a complete walkthrough and Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm30",
        "name": "DOORDASH ACCOUNTS",
        "price": 10,
        "description": (
            "DoorDash account workflow. Instant access with order tracking, "
            "receipt organization, and beginner-friendly setup."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm31",
        "name": "CHICK-FIL-A ACCOUNTS",
        "price": 15,
        "description": (
            "Chick-fil-A rewards workflow. Instant access with points "
            "tracking and simple setup instructions."
        ),
        "weight": 4,
        "auto_publish": True,
    },

    {
        "id": "mm32",
        "name": "MCDONALDS ACCOUNTS",
        "price": 15,
        "description": (
            "McDonald's rewards workflow. Instant access with points "
            "tracking and beginner-friendly setup."
        ),
        "weight": 4,
        "auto_publish": True,
    },

    {
        "id": "mm33",
        "name": "YAHOO MAIL ACCOUNTS",
        "price": 15,
        "description": (
            "Yahoo Mail account workflow. Instant access with setup guidance, "
            "security checklist, and Telegram support."
        ),
        "weight": 0,
        "auto_publish": False,
    },

    {
        "id": "mm34",
        "name": "SNAPCHAT ACCOUNTS",
        "price": 15,
        "description": (
            "Snapchat creator account workflow. Instant access with setup "
            "guidance, audience tracking, and monetization notes."
        ),
        "weight": 3,
        "auto_publish": True,
    },

    {
        "id": "mm35",
        "name": "GAMESTOP ACCOUNTS",
        "price": 15,
        "description": (
            "GameStop account and rewards workflow. Instant access with "
            "points tracking and trade-in organization."
        ),
        "weight": 4,
        "auto_publish": True,
    },

    {
        "id": "mm36",
        "name": "PIZZA HUT ACCOUNTS",
        "price": 15,
        "description": (
            "Pizza Hut rewards workflow. Instant access with points "
            "tracking and simple setup instructions."
        ),
        "weight": 4,
        "auto_publish": True,
    },

    {
        "id": "mm37",
        "name": "EBAY ACCOUNTS",
        "price": 15,
        "description": (
            "eBay seller and buyer workflow. Instant access with listing "
            "guidance, fee tracking, and Telegram support."
        ),
        "weight": 5,
        "auto_publish": True,
    },
]


# ============================================================
# CATALOG FUNCTIONS
# ============================================================

def get_products():
    """Return the complete 37-product master catalog."""
    return PRODUCTS.copy()


def product_count():
    """Total products in MONEY MAKER."""
    return len(PRODUCTS)


def approved_products():
    """Products eligible for automatic Telegram promotion."""
    return [
        product
        for product in PRODUCTS
        if product.get("auto_publish", False)
        and product.get("weight", 0) > 0
    ]


def approved_product_count():
    return len(approved_products())


def random_product():
    """
    Weighted selection.

    CASHAPP TRANSFER SAUCE has the highest weight,
    so it appears more frequently than ordinary products.
    """
    pool = approved_products()

    if not pool:
        raise RuntimeError("No products enabled for automatic publishing.")

    weights = [product["weight"] for product in pool]

    return random.choices(
        population=pool,
        weights=weights,
        k=1,
    )[0]


def search_products(query):
    """Search the complete master catalog."""
    query = query.lower().strip()

    return [
        product
        for product in PRODUCTS
        if query in product["name"].lower()
        or query in product["description"].lower()
    ]


# ============================================================
# TELEGRAM COPY
# ============================================================

def telegram_product_text(product):

    name = product["name"]
    price = product["price"]
    description = product["description"]

    templates = [

        f"""⚡ PRODUCT SPOTLIGHT

{name}

💵 ${price}

{description}

🟢 AVAILABLE NOW

👇 VIEW IN MONEY MAKER""",

        f"""💸 MONEY MAKER DROP

{name}

CURRENT PRICE
${price}

{description}

🌎 Available online

👇 CHECK THE STORE""",

        f"""🔥 CURRENT DROP

{name}

💰 ${price}

{description}

See the current listing in the official MONEY MAKER store.

👇 OPEN MONEY MAKER""",

        f"""⚡ MONEY MAKER PRODUCT

{name}

PRICE
${price}

{description}

Explore the complete product information in MONEY MAKER.

👇 VIEW PRODUCT""",
    ]

    return random.choice(templates)


# ============================================================
# LOCAL TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 65)
    print(" MONEY MAKER — MASTER TELEGRAM CATALOG")
    print("=" * 65)

    print(f"Master catalog       : {product_count()}")
    print(f"Automatic promotion : {approved_product_count()}")

    print("=" * 65)

    for number, product in enumerate(PRODUCTS, 1):

        status = (
            "AUTO"
            if product.get("auto_publish", False)
            else "CATALOG ONLY"
        )

        print(
            f"{number:02d} | "
            f"{product['name']:<26} | "
            f"${product['price']:<4} | "
            f"{status}"
        )

    print("=" * 65)

    print()
    print("RANDOM TELEGRAM SELECTION")
    print()

    product = random_product()

    print(telegram_product_text(product))

    print()
    print("=" * 65)
    print("STATUS: READY")
    print("=" * 65)