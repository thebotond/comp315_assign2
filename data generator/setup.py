import os

categories = ["Electronics", "Clothing", "Home & Garden", "Beauty", "Toys"]
subcategories = {
    "Electronics": [("Desktop PC", 500, 3000),
                    ("Laptop", 200, 2500),
                    ("Mobile Phone", 100, 2000),
                    ("Television", 500, 2000),
                    ("VR Headset", 200, 800), #new
                    ("Monitor", 50, 250), #new
                    ("Earphones", 25, 50), #new 
                    ("Keyboard", 5, 100), #new
                    ("Tablet", 75, 500), #new
                    ("Smart Watch", 40, 300)], #new
    "Clothing": [("T-shirt", 5, 25),
                 ("Trousers", 15, 75),
                 ("Shoes", 25, 200),
                 ("Jacket", 30, 250),
                 ("Socks", 5, 25), #new
                 ("Sunglasses", 10, 200), #new
                 ("Belt", 10, 50), #new
                 ("Hat", 5, 75), #new
                 ("Ring", 20, 150), #new
                 ("Dress", 50, 250)], #new
    "Home & Garden": [("Barbecue Grill", 75, 1500),
                      ("Flower Pot", 5, 40),
                      ("Rainwater Collector", 55, 100),
                      ("Deck Chair", 20, 100), #new
                      ("Lawn mower", 60, 200), #new
                      ("Spade", 10, 35), #new
                      ("Trowel", 5, 20), #new
                      ("Garden Pool", 80, 800), #new
                      ("Hose", 8, 25)], #new
    "Beauty": [("Deodorant", 1, 10),
               ("Shampoo", 4, 35),
               ("Shower Gel", 2, 15)],
    "Toys": [("Tabletop Game", 15, 200),
             ("Action Figure", 1, 20),
             ("Doll", 1, 20)]
}

def create_folders():
    for category in categories:
        os.makedirs(category, exist_ok=True)
        if category in subcategories:
            for subcategory in subcategories[category]:
                #print(subcategory[0])
                subcategory_folder = os.path.join(category, subcategory[0])
                os.makedirs(subcategory_folder, exist_ok=True)

if __name__ == "__main__":
    create_folders()
