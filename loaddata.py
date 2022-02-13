import pandas as pd

print("Loading big matrix...")
big_matrix = pd.read_csv("data/big_matrix.csv")
print("Loading small matrix...")
small_matrix = pd.read_csv("data/small_matrix.csv")

print("Loading social network...")
social_network = pd.read_csv("data/social_network.csv")
social_network["friend_list"] = social_network["friend_list"].map(eval)

print("Loading item features...")
item_feat = pd.read_csv("data/item_categories.csv")
item_feat["feat"] = item_feat["feat"].map(eval)

print("All data loaded.")
print("1. Big matrix:")
print(big_matrix)
print("2. Small matrix:")
print(small_matrix)
print("3. Social network of users in big matrix:")
print(social_network)
print("4. Item features of items in big matrix")
print(item_feat)