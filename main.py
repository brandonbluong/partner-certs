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
duplicate_key = ["Full Name", "Company", "CAM Manager"]
clean_users_df = (
    raw_users_df.drop(drop_columns, axis=1)
    .rename(rename_columns, axis=1)
    .drop_duplicates(duplicate_key)
)
raw_sales_certs_df = pd.read_csv("Personal/raw_sales_certs.csv")
clean_sales_certs_df = raw_sales_certs_df.rename(
    {"Passed": "Passed Date"}, axis=1
).assign(**{"Certification Type": "Sales"})


raw_technical_certs_df = pd.read_csv("Personal/raw_technical_certs.csv")
clean_technical_certs_df = raw_technical_certs_df.rename(
    {"Passed": "Passed Date"}, axis=1
).assign(**{"Certification Type": "Technical"})

# Combine sales and tech clean dfs
total_certs_df = pd.concat([clean_sales_certs_df, clean_technical_certs_df])

left_join_keys = ["User", "Account"]
right_join_keys = ["Full Name", "Company"]

# # print(total_certs_df.columns)
# # print(clean_users_df.columns)

merged_certs_df = total_certs_df.merge(
    clean_users_df, how="left", left_on=left_join_keys, right_on=right_join_keys
)

merged_certs_df = merged_certs_df[
    [
        "Full Name",
        "Email",
        "Title",
        "Company",
        "CAM Manager",
        "Certification Type",
        "Passed Date",
        "City",
        "US State",
        "Country",
    ]
]

print(total_certs_df.shape, merged_certs_df.shape)
print(merged_certs_df.columns)

# # merged_certs = total_certs_df.merge(clean_users_df,
# #     on=)
# # print(merged_certs)

# # if __name__ == "__main__":
# #     pass
