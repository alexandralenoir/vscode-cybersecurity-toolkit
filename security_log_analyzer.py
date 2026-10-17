# Simple Security Log Analyzer

login_logs = [
    "alex - SUCCESS",
    "admin - FAILED",
    "admin - FAILED",
    "alex - SUCCESS",
    "guest - FAILED",
    "admin - FAILED",
    "guest - FAILED",
    "guest - FAILED"
]

failed_attempts = {}

for log in login_logs:
    parts = log.split(" - ")
    username = parts[0]
    result = parts[1]

    if result == "FAILED":
        if username in failed_attempts:
            failed_attempts[username] += 1
        else:
            failed_attempts[username] = 1


print("Security Log Report")
print("-------------------")

for username in failed_attempts:
    print(username, "had", failed_attempts[username],
          "failed login attempts.")

    if failed_attempts[username] >= 3:
        print("Warning: Check this account!")