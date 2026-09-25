print("=== STUDY ANALYZER ===")

sessions = []

while True:
    subject = input("Enter subject (or 'done' to finish): ")

    if subject.lower() == "done":
        break

    hours = float(input("Hours studied: "))
    score = float(input("Score: "))

    sessions.append({
        "subject": subject,
        "hours": hours,
        "score": score
    })

print("\n=== RESULTS ===")

total_hours = sum(session["hours"] for session in sessions)

print(f"Total study time: {total_hours:.1f} hours")

if sessions:
    average_score = sum(
        session["score"] for session in sessions
    ) / len(sessions)

    print(f"Average score: {average_score:.1f}")

    most_studied = max(
        sessions,
        key=lambda session: session["hours"]
    )

    print(
        f"Most studied subject: "
        f"{most_studied['subject']}"
    )
else:
    print("No study sessions were added.")
