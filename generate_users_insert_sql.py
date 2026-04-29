import csv

with open("users.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    with open("insert_users.sql", "w", encoding="utf-8") as sql_file:
        sql_file.write("USE fintech_product_analysis;\n\n")

        for row in reader:
            kyc_completed_at = (
                f"'{row['kyc_completed_at']}'"
                if row["kyc_completed_at"].strip()
                else "NULL"
            )

            insert_statement = f"""
INSERT INTO users (
    user_id,
    signup_date,
    acquisition_channel,
    country,
    device_type,
    kyc_status,
    kyc_completed_at
)
VALUES (
    {row['user_id']},
    '{row['signup_date']}',
    '{row['acquisition_channel']}',
    '{row['country']}',
    '{row['device_type']}',
    '{row['kyc_status']}',
    {kyc_completed_at}
);
"""
            sql_file.write(insert_statement)

print("insert_users.sql generated successfully!")
