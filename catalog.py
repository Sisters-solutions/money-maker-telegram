import random


# ============================================================
# MONEY MAKER — TELEGRAM CATALOG
# Only products approved for automatic promotion go here.
# ============================================================

PRODUCTS = [
    {
        "name": "CASHAPP TRANSFER SAUCE",
        "price": 200,
        "description": (
            "Beginner-friendly Cash App transfer workflow "
            "with step-by-step instructions and Telegram support."
        ),
    },

    # Añadiremos aquí las demás ofertas legítimas del catálogo
    # después de extraerlas del HTML completo.
]


def get_products():
    return PRODUCTS.copy()


def product_count():
    return len(PRODUCTS)


def random_product():
    if not PRODUCTS:
        raise RuntimeError("No approved products in catalog.")

    return random.choice(PRODUCTS)


def search_products(query):
    query = query.lower().strip()

    return [
        product
        for product in PRODUCTS
        if query in product["name"].lower()
        or query in product["description"].lower()
    ]


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
    ]

    return random.choice(templates)


if __name__ == "__main__":
    print("=" * 60)
    print(" MONEY MAKER — TELEGRAM CATALOG")
    print("=" * 60)
    print(f"Approved products: {product_count()}")

    for number, product in enumerate(PRODUCTS, 1):
        print(
            f"{number:02d} | "
            f"{product['name']} | "
            f"${product['price']}"
        )

    print("=" * 60)

    if PRODUCTS:
        print()
        print(telegram_product_text(random_product()))

    print()
    print("STATUS: READY")