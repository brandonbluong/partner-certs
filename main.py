import personal.snyk_data as t3
import pandas as pd


# Clean raw_users
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

# Clean raw_sales_cert and raw_technical_cert
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

# Convert passed date column to datetime
total_certs_df["Passed Date"] = pd.to_datetime(
    total_certs_df["Passed Date"], format="%m/%d/%Y", infer_datetime_format=True
)

# Merge total_certs with clean_users with a left join
left_join_keys = ["User", "Account"]
right_join_keys = ["Full Name", "Company"]

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
print(merged_certs_df.dtypes)


# # merged_certs_df would be exported as excel file for chris garcia
# # merged_certs_df.to_excel("test_excel_for_chris.xlsx")
# # print("Successfully exported")

# # For NA CAM Managers
# na_certs_df = merged_certs_df

# # Filter out any certs before 8/1/2022 (Q3 2022)
# na_certs_df = na_certs_df[na_certs_df["Passed Date"] > "2022-08-01"]

# print(na_certs_df.shape, merged_certs_df.shape)

# # na_certs_df.to_excel("test_excel_for_na_managers.xlsx")

# print(t3.cam_manager)

# # # if __name__ == "__main__":
# # #     pass
