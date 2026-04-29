import csv
import random
from datetime import datetime, timedelta

NUM_USERS = 5000

acquisition_channels = ["organic", "referral", "paid_ads", "affiliate"]
countries = ["Ireland", "UK", "India"]
devices = ["iOS", "Android"]


def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

users = []

for user_id in range(1, NUM_USERS + 1):

    signup_date = random_date(start_date, end_date)

    acquisition = random.choices(
        acquisition_channels,
        weights=[30, 25, 30, 15]
    )[0]

    country = random.choice(countries)
    device = random.choice(devices)

    user_type = random.choices(
        ["active", "semi_active", "inactive"],
        weights=[50, 30, 20]
    )[0]

    if user_type == "inactive":
        kyc_status = "pending"
        kyc_completed_at = None

    else:
        if random.random() < 0.7:
            kyc_status = "approved"
            kyc_completed_at = signup_date + \
                timedelta(days=random.randint(1, 5))
        else:
            kyc_status = "rejected"
            kyc_completed_at = None

    users.append([
        user_id,
        signup_date.strftime("%Y-%m-%d %H:%M:%S"),
        acquisition,
        country,
        device,
        kyc_status,
        kyc_completed_at.strftime(
            "%Y-%m-%d %H:%M:%S") if kyc_completed_at else None
    ])

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "user_id",
        "signup_date",
        "acquisition_channel",
        "country",
        "device_type",
        "kyc_status",
        "kyc_completed_at"
    ])
    writer.writerows(users)

print("users.csv generated successfully!")
