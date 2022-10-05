import pandas as pd

raw_users_df = pd.read_csv("Personal/raw_users.csv")
drop_columns = [
    "Account | Partner Type",
    "Job Role",
    "Administrative Privileges",
    "Last Login - Timestamp",
]

clean_users_df = raw_users_df.drop(drop_columns, axis=1)
print(clean_users_df.columns)
print(clean_users_df.head())

# if __name__ == "__main__":
#     pass
