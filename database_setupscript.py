# Database setup script

from pymongo import MongoClient
import uuid

client = MongoClient("mongodb://localhost:27017/")
db = client["DATABASEPROJECT"]

print("Dropping existing database") 
client.drop_database("DATABASEPROJECT")

print("Recreating collections...")

collections = [
    "users", "profiles", "wishlist", "viewing_history", "subscription_plans",
    "content", "episodes", "seasons", "genres", "content_genres", "media_files"
]

for col in collections: 
    db.create_collection(col)
    
    print("Creating indexes")
    db.users.create_index("email", unique=True)
    
    print("Inserting subscription plans")
    seed_plans = [
        {"_id": str(uuid.uuid4()), "plan_name": "Basic", "monthly_price": 9.99, "max_profiles": 1},
    {"_id": str(uuid.uuid4()), "plan_name": "Standard", "monthly_price": 14.99, "max_profiles": 3},
    {"_id": str(uuid.uuid4()), "plan_name": "Premium", "monthly_price": 19.99, "max_profiles": 5},
    ]
    db.subscription_plans.insert_many(seed_plans)
    
print("Inserting genres...")
seed_genres = [
    {"_id": str(uuid.uuid4()), "genre_name": "Comedy"},
    {"_id": str(uuid.uuid4()), "genre_name": "Sci-Fi"},
    {"_id": str(uuid.uuid4()), "genre_name": "Drama"},
]
db.genres.insert_many(seed_genres)

print("Database setup complete.")
