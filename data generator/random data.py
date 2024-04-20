import random
import os
import json

categories = ["Electronics", "Clothing", "Home & Garden", "Beauty", "Toys"]

prod_is = {
    "Electronics": ["is innovative", "is high-end", "is reliable"],
    "Clothing": ["is comfortable", "is fashionable"],
    "Home & Garden": ["is durable", "is reliable", "is award-winning"],
    "Beauty": ["is luxurious", "is effective", "is natural"],
    "Toys": ["is fun for children", "is creative", "is educational"]
}

prod_has = {
    "Electronics": [" and has a smart design.", " and has a compact design."],
    "Clothing": [" and has a stylish design.", " and has a simple design."],
    "Home & Garden": [" and is on sale", "."],
    "Beauty": [" and is on sale.", "."],
    "Toys": [" and is on sale.", "."]
}

#product attributes
#category: name & lower bound and upper bound for random price
products_by_category = {
    "Electronics": [("Desktop PC", 500, 3000),
                    ("Laptop", 200, 2500),
                    ("Mobile Phone", 100, 2000),
                    ("Television", 500, 2000)],
    "Clothing": [("T-shirt", 5, 25),
                 ("Trousers", 15, 75),
                 ("Shoes", 25, 200),
                 ("Jacket", 30, 250)],
    "Home & Garden": [("Barbecue Grill", 75, 1500),
                      ("Flower Pot", 5, 40),
                      ("Rainwater Collector", 55, 100)],
    "Beauty": [("Deodorant", 1, 10),
               ("Shampoo", 4, 35),
               ("Shower Gel", 2, 15)],
    "Toys": [("Tabletop Game", 15, 200),
             ("Action Figure", 1, 20),
             ("Doll", 1, 20)]
}

#keep track of products
product_counts = {}
prod_id = 0

#keep track of image links
used_image_links = set()

# Generate data
def generate_random_product():
        #random cat
        category = random.choice(categories)
        global prod_id
        product_id = prod_id
        #print(product_id)

        #random product name, min price, and max price
        name, min_price, max_price = random.choice(products_by_category[category])

        #unique products
        product_counts.setdefault(name, 0)
        product_counts[name] += 1

        if product_counts[name] <= 10: #up to 10 of the same product
            product_number = product_counts[name]
            product_name = f"{name} {product_number}"
            
            #generate unique image link
            image_link = generate_unique_image_link(category, name)

            price = round(random.uniform(min_price, max_price), 2)
            description = f"{product_name} {random.choice(prod_is[category])}{random.choice(prod_has[category])}"
            quantity = random.randint(0, 10)
            rating = round(random.uniform(1, 5), 2)
            prod_id += 1

            return {
                "id": product_id,
                "name": product_name,
                "price": price,
                "desc": description,
                "cat": category,
                "qty": quantity,
                "rating": rating,
                "image_link": image_link.replace("\\", "/")
                }

def generate_unique_image_link(category, name):
    while True:
        folder_path = os.path.join(category, name)
        images = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
        return os.path.join(folder_path, random.choice(images))

#generate products
random_products = [generate_random_product() for _ in range(500000)]
random_products = [product for product in random_products if product]  #remove None values

#write to JSON
with open('random_products.json', 'w') as f:
    json.dump(random_products, f, indent=4)
