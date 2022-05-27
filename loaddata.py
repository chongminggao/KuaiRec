import pandas as pd

print("Loading big matrix...")
big_matrix = pd.read_csv("data/big_matrix.csv")
print("Loading small matrix...")
small_matrix = pd.read_csv("data/small_matrix.csv")

print("Loading social network...")
social_network = pd.read_csv("data/social_network.csv")
social_network["friend_list"] = social_network["friend_list"].map(eval)

print("Loading item features...")
item_categories = pd.read_csv("data/item_categories.csv")
item_categories["feat"] = item_categories["feat"].map(eval)

print("Loading user features...")
user_features = pd.read_csv("data/user_features.csv")

print("Loading items' daily features...")
item_daily_feat = pd.read_csv("data/item_daily_features.csv")

print("All data loaded.")
print("1. Big matrix:")
print(big_matrix)
print("2. Small matrix:")
print(small_matrix)
print("3. Social network of users in big matrix:")
print(social_network)
print("4. Items' basic features of all items in big matrix")
print(item_categories)
print("5. User features of all users in big matrix. \nNote: this table is added in KuaiRec v2.0")
print(user_features)
print("6. Item daily features. \nNote: this table is added in KuaiRec v2.0")
print(item_daily_feat)

