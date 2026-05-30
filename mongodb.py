from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv('mongoDBURI')
client = MongoClient(uri, server_api=ServerApi('1'))

# Ping check
try:
    client.admin.command('ping')
    print("Connected to MongoDB!")
except Exception as e:
    print(f"Connection failed: {e}")
    exit()

# --- Setup ---
db = client["my_database"]
collection = db["my_collection"]

# --- WRITE: Insert one ---
doc = {"name": "Alice", "age": 30, "city": "London"}
result = collection.insert_one(doc)
print(f"Inserted ID: {result.inserted_id}")

# --- WRITE: Insert many ---
docs = [
    {"name": "Bob",     "age": 25, "city": "Manchester"},
    {"name": "Charlie", "age": 35, "city": "Birmingham"},
]
result = collection.insert_many(docs)
print(f"Inserted IDs: {result.inserted_ids}")

# --- READ: Find one ---
doc = collection.find_one({"name": "Alice"})
print(f"Found one: {doc}")

# --- READ: Find many (with filter) ---
print("All people over 24:")
for doc in collection.find({"age": {"$gt": 24}}):
    print(" ", doc)

# --- UPDATE: Update one ---
collection.update_one(
    {"name": "Alice"},
    {"$set": {"city": "Edinburgh"}}
)
print("Updated Alice's city.")

# --- DELETE: Delete one ---
collection.delete_one({"name": "Charlie"})
print("Deleted Charlie.")

# --- READ: Final state ---
print("Final collection:")
for doc in collection.find():
    print(" ", doc)

# --- List all databases ---
print("Databases:", client.list_database_names())

client.close()