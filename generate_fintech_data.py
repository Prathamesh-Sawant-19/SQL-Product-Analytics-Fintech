import csv
import random
from datetime import datetime, timedelta

random.seed(42)

NUM_USERS = 5000

acquisition_channels = ["organic", "referral", "paid_ads", "affiliate"]
countries = ["Ireland", "UK", "India"]
devices = ["iOS", "Android"]

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)

users = []
events = []
sessions = []
transactions = []
support_tickets = []

event_id = 1
session_id = 1
transaction_id = 1
ticket_id = 1


def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def write_csv(filename, headers, rows):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


for user_id in range(1, NUM_USERS + 1):
    signup_date = random_date(start_date, end_date)

    acquisition = random.choices(
        acquisition_channels,
        weights=[30, 25, 30, 15]
    )[0]

    country = random.choices(
        countries,
        weights=[45, 35, 20]
    )[0]

    device = random.choices(
        devices,
        weights=[55, 45]
    )[0]

    user_type = random.choices(
        ["active", "semi_active", "inactive"],
        weights=[50, 30, 20]
    )[0]

    if user_type == "inactive":
        kyc_status = random.choices(
            ["pending", "rejected"], weights=[70, 30])[0]
        kyc_completed_at = None
    else:
        kyc_chance = 0.72

        if acquisition == "referral":
            kyc_chance += 0.08
        elif acquisition == "paid_ads":
            kyc_chance -= 0.08

        if device == "iOS":
            kyc_chance += 0.03

        if random.random() < kyc_chance:
            kyc_status = "approved"
            kyc_completed_at = signup_date + \
                timedelta(days=random.randint(1, 5))
        else:
            kyc_status = random.choice(["pending", "rejected"])
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

    # Sessions
    if user_type == "active":
        num_sessions = random.randint(8, 18)
    elif user_type == "semi_active":
        num_sessions = random.randint(3, 8)
    else:
        num_sessions = random.randint(1, 3)

    user_session_ids = []

    for _ in range(num_sessions):
        session_start = signup_date + \
            timedelta(days=random.randint(0, 90), hours=random.randint(0, 23))
        session_duration = random.randint(2, 45)
        session_end = session_start + timedelta(minutes=session_duration)

        sessions.append([
            session_id,
            user_id,
            session_start.strftime("%Y-%m-%d %H:%M:%S"),
            session_end.strftime("%Y-%m-%d %H:%M:%S"),
            device
        ])

        user_session_ids.append(session_id)
        session_id += 1

    # Events
    first_session = user_session_ids[0]

    events.append([event_id, user_id, signup_date.strftime(
        "%Y-%m-%d %H:%M:%S"), "app_open", first_session])
    event_id += 1

    events.append([event_id, user_id, (signup_date + timedelta(minutes=5)
                                       ).strftime("%Y-%m-%d %H:%M:%S"), "onboarding_started", first_session])
    event_id += 1

    if kyc_status in ["approved", "rejected"]:
        events.append([event_id, user_id, (signup_date + timedelta(hours=2)
                                           ).strftime("%Y-%m-%d %H:%M:%S"), "kyc_submitted", first_session])
        event_id += 1

    if kyc_status == "approved":
        events.append([event_id, user_id, kyc_completed_at.strftime(
            "%Y-%m-%d %H:%M:%S"), "kyc_approved", first_session])
        event_id += 1

        bank_added_time = kyc_completed_at + \
            timedelta(hours=random.randint(1, 24))
        events.append([event_id, user_id, bank_added_time.strftime(
            "%Y-%m-%d %H:%M:%S"), "bank_added", random.choice(user_session_ids)])
        event_id += 1

        activation_chance = 0.58

        if acquisition == "referral":
            activation_chance += 0.10
        elif acquisition == "paid_ads":
            activation_chance -= 0.10

        if device == "iOS":
            activation_chance += 0.05

        if user_type == "active":
            activation_chance += 0.15
        elif user_type == "semi_active":
            activation_chance -= 0.05

        if random.random() < activation_chance:
            first_attempt_time = bank_added_time + \
                timedelta(days=random.randint(0, 7))
            first_success_time = first_attempt_time + \
                timedelta(minutes=random.randint(5, 120))

            events.append([event_id, user_id, first_attempt_time.strftime(
                "%Y-%m-%d %H:%M:%S"), "first_transaction_attempted", random.choice(user_session_ids)])
            event_id += 1

            events.append([event_id, user_id, first_success_time.strftime(
                "%Y-%m-%d %H:%M:%S"), "first_transaction_success", random.choice(user_session_ids)])
            event_id += 1

            if user_type == "active":
                num_transactions = random.randint(3, 8)
            else:
                num_transactions = random.randint(1, 3)

            for tx_num in range(num_transactions):
                transaction_time = first_success_time + \
                    timedelta(days=random.randint(0, 90))
                amount = round(random.choice([
                    random.uniform(5, 20),
                    random.uniform(50, 500),
                    random.uniform(500, 2000)
                ]), 2)

                status = random.choices(
                    ["success", "failed"], weights=[85, 15])[0]
                fee_revenue = round(
                    amount * 0.015, 2) if status == "success" else 0.00

                transactions.append([
                    transaction_id,
                    user_id,
                    transaction_time.strftime("%Y-%m-%d %H:%M:%S"),
                    amount,
                    status,
                    fee_revenue
                ])

                transaction_id += 1

    # Support tickets
    ticket_probability = 0.18

    if kyc_status in ["pending", "rejected"]:
        ticket_probability += 0.15

    if user_type == "inactive":
        ticket_probability += 0.10

    if random.random() < ticket_probability:
        category = random.choices(
            ["KYC Issue", "Payment Failure", "Account Access"],
            weights=[45, 35, 20]
        )[0]

        ticket_time = signup_date + timedelta(days=random.randint(1, 30))
        resolution_time = round(random.uniform(2, 72), 2)

        support_tickets.append([
            ticket_id,
            user_id,
            ticket_time.strftime("%Y-%m-%d %H:%M:%S"),
            category,
            resolution_time
        ])

        ticket_id += 1


write_csv("users.csv", [
    "user_id",
    "signup_date",
    "acquisition_channel",
    "country",
    "device_type",
    "kyc_status",
    "kyc_completed_at"
], users)

write_csv("sessions.csv", [
    "session_id",
    "user_id",
    "session_start",
    "session_end",
    "device_type"
], sessions)

write_csv("events.csv", [
    "event_id",
    "user_id",
    "event_time",
    "event_name",
    "session_id"
], events)

write_csv("transactions.csv", [
    "transaction_id",
    "user_id",
    "transaction_time",
    "amount",
    "status",
    "fee_revenue"
], transactions)

write_csv("support_tickets.csv", [
    "ticket_id",
    "user_id",
    "ticket_time",
    "category",
    "resolution_time_hours"
], support_tickets)

print("All CSV files generated successfully!")
print(f"Users: {len(users)}")
print(f"Sessions: {len(sessions)}")
print(f"Events: {len(events)}")
print(f"Transactions: {len(transactions)}")
print(f"Support tickets: {len(support_tickets)}")
