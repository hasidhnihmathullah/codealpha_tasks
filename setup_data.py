import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import Product

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(BASE_DIR, 'static', 'images', 'products')
os.makedirs(TARGET_DIR, exist_ok=True)

# 1. Locate and organize all 19 image files
image_names = [
    'watch1.jpg', 'watch2.avif', 'watch3.jpg', 'watch4.jpg', 'watch5.jpg',
    'earphones1.jpg', 'earphones2.jpg', 'earphones3.jpg', 'earphones4.jpg',
    'bag2.jpg', 'bag4.jpg', 'bag5.jpg', 'bag6.jpg', 'bag7.jpg',
    'bracelet1.jpg', 'bracelet2.jpg', 'bracelet4.jpg', 'bracelet5.jpg', 'bracelet6.jpg'
]

print("--- Organizing Static Images ---")
for img in image_names:
    dest_path = os.path.join(TARGET_DIR, img)
    if not os.path.exists(dest_path):
        # Search project directory for the image
        found = False
        for root, dirs, files in os.walk(BASE_DIR):
            if 'venv' in root:
                continue
            if img in files:
                src_path = os.path.join(root, img)
                shutil.copy2(src_path, dest_path)
                print(f"Copied {img} -> static/images/products/")
                found = True
                break
        if not found:
            print(f"[!] Warning: Could not find {img}. Make sure it is in your project folder.")
    else:
        print(f"Verified: {img} is present in static/images/products/")

# 2. Sync SQLite Database Products
print("\n--- Populating SQLite Database ---")
Product.objects.all().delete()

products_data = [
    # 1 - 5: Watches
    {"id": 1, "name": "Aura Stealth Minimalist Steel Watch", "price": 189.00, "category": "watches",
     "desc": "Ultra-sleek gunmetal stainless steel timepiece featuring a minimal dial and brushed link bracelet.", "img": "/static/images/products/watch1.jpg"},
    {"id": 2, "name": "Nektom Matrix Skeleton Chronograph", "price": 145.00, "category": "watches",
     "desc": "Industrial square steel casing with an intricate mechanical skeleton layout and stitched black leather strap.", "img": "/static/images/products/watch2.avif"},
    {"id": 3, "name": "Chronos Heritage Rose Gold Watch", "price": 249.00, "category": "watches",
     "desc": "Polished rose gold bezel with three complication sub-dials and crocodile-textured genuine leather strap.", "img": "/static/images/products/watch3.jpg"},
    {"id": 4, "name": "Vanguard Granular Cushion Chronograph", "price": 219.00, "category": "watches",
     "desc": "Subtle sand-textured dial housed in a brushed steel cushion case with a durable taupe leather band.", "img": "/static/images/products/watch4.jpg"},
    {"id": 5, "name": "Universe Point Octo Sports Watch", "price": 129.00, "category": "watches",
     "desc": "Modern octagonal geometric case, textured royal blue dial, and high-grade sports silicone strap.", "img": "/static/images/products/watch5.jpg"},

    # 6 - 9: Earphones
    {"id": 6, "name": "AirSound Pro 2 Active ANC Earbuds", "price": 249.00, "category": "earphones",
     "desc": "Active Noise Cancellation, Transparency Mode, personalized spatial audio, and wireless charging case.", "img": "/static/images/products/earphones1.jpg"},
    {"id": 7, "name": "ShadowBuds Stealth Wireless ANC", "price": 79.00, "category": "earphones",
     "desc": "Ergonomic matte black stem earbuds with noise isolation, dual mics, and up to 28 hours playtime.", "img": "/static/images/products/earphones2.jpg"},
    {"id": 8, "name": "OnePlus Buds Pro Dual-Tone Earbuds", "price": 149.00, "category": "earphones",
     "desc": "Dual-tone matte and metallic finish with smart adaptive noise cancellation and low-latency audio.", "img": "/static/images/products/earphones3.jpg"},
    {"id": 9, "name": "Obsidian Pebble True Wireless Earphones", "price": 69.00, "category": "earphones",
     "desc": "Glossy obsidian earbuds inside a compact rounded pebble case with 10mm dynamic bass drivers.", "img": "/static/images/products/earphones4.jpg"},

    # 10 - 14: Handbags
    {"id": 10, "name": "Ivory Structured Tote with Gold Chain Charm", "price": 185.00, "category": "handbags",
     "desc": "Premium cream-white leather tote bag with rolled top handles, polished gold chain pendant, and spacious dual compartments.", "img": "/static/images/products/bag2.jpg"},
    {"id": 11, "name": "Maison Olive Quilted Leather Flap Bag", "price": 265.00, "category": "handbags",
     "desc": "Luxurious olive green quilted leather handbag with arched handle, gold-tone hardware, and iconic turn-lock closure.", "img": "/static/images/products/bag4.jpg"},
    {"id": 12, "name": "Lumina Pearl Gloss Hardcase Handbag", "price": 210.00, "category": "handbags",
     "desc": "Futuristic structured ivory gloss finish paired with sculpted double gold handles and minimalist front emblem plaque.", "img": "/static/images/products/bag5.jpg"},
    {"id": 13, "name": "Noir Royale Top-Handle Bag with Silk Twilly", "price": 295.00, "category": "handbags",
     "desc": "Pebbled black calfskin leather satchel featuring a gold twist lock and silk equestrian scarf-wrapped top handle.", "img": "/static/images/products/bag6.jpg"},
    {"id": 14, "name": "Crimson Scarlet Satchel with Silk Scarf Bow", "price": 230.00, "category": "handbags",
     "desc": "Rich crimson red leather structured handbag with gold bar clasp accent and patterned satin bow ribbon handle.", "img": "/static/images/products/bag7.jpg"},

    # 15 - 19: Bracelets
    {"id": 15, "name": "Sterling Silver Trio Stack Chain Set", "price": 95.00, "category": "bracelets",
     "desc": "Layered 3-piece silver bracelet set featuring a classic curb link, twisted rope chain, and sleek round snake chain.", "img": "/static/images/products/bracelet1.jpg"},
    {"id": 16, "name": "Minimalist Steel Paperclip Link Bracelet", "price": 55.00, "category": "bracelets",
     "desc": "Modern elongated paperclip chain links crafted in hypoallergenic high-polish 316L stainless steel.", "img": "/static/images/products/bracelet2.jpg"},
    {"id": 17, "name": "Trinity Cross Silicone & Steel Bangle Set", "price": 68.00, "category": "bracelets",
     "desc": "Triple-stacked black waterproof silicone wristbands fitted with gold, silver, and gunmetal cross emblem plates.", "img": "/static/images/products/bracelet4.jpg"},
    {"id": 18, "name": "Stealth Curve Polished Plate Bangle", "price": 49.00, "category": "bracelets",
     "desc": "Matte black sport silicone band with an ergonomic curved stainless steel mirror-finish identification bar.", "img": "/static/images/products/bracelet5.jpg"},
    {"id": 19, "name": "Artisan Leather Cuff with Sterling Silver Bar", "price": 62.00, "category": "bracelets",
     "desc": "Genuine black calfskin strap bracelet with a high-shine curved silver bar accent plate and secure locking clasp.", "img": "/static/images/products/bracelet6.jpg"},
]

for item in products_data:
    Product.objects.create(
        id=item["id"],
        name=item["name"],
        price=item["price"],
        description=item["desc"],
        image_url=item["img"]
    )

print(f"Successfully loaded {Product.objects.count()} verified products into SQLite!")