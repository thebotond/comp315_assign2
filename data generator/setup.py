#No need to run this unless you want to set up new directories with new image files
#This script creates directories for each category and a subdirectory for each product in their respective category (parent) directory
import os

categories = ["Electronics", "Clothing", "Home & Garden", "Beauty", "Toys"]
subcategories = {
    "Electronics": ["Desktop PC", "Laptop", "Mobile Phone", "Television"],
    "Clothing": ["T-shirt", "Trousers", "Shoes", "Jacket"],
    "Home & Garden": ["Barbecue Grill", "Flower Pot", "Rainwater Collector"],
    "Beauty": ["Deodorant", "Shampoo", "Shower Gel"],
    "Toys": ["Tabletop Game", "Action Figure", "Doll"]
}

def create_folders():
    for category in categories:
        os.makedirs(category_folder, exist_ok=True)
        if category in subcategories:
            for subcategory in subcategories[category]:
                subcategory_folder = os.path.join(category_folder, subcategory.replace(" & ", "_"))
                os.makedirs(subcategory_folder, exist_ok=True)

if __name__ == "__main__":
    create_folders()
