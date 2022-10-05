import pandas as pd

raw_users_df = pd.read_csv("Personal/raw_users.csv")
drop_columns = [
    "Account | Partner Type",
    "Job Role",
    "Administrative Privileges",
    "Last Login - Timestamp",
]

rename_columns = {
    "Job Title": "Title",
    "Account": "Company",
    "Account | SFDC Account Owner Name for CAM Name": "CAM Manager",
    "Mailing City": "City",
    "Mailing State": "US State",
    "Mailing Country": "Country",
}

clean_users_df = raw_users_df.drop(drop_columns, axis=1).rename(rename_columns, axis=1)
print(clean_users_df.columns)
print(clean_users_df.head())

# if __name__ == "__main__":
#     pass
