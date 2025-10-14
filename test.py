def check_voting_eligibility(name, age, nationality, has_voters_card):
    if nationality.lower() != "nigerian":
        return f"{name}  Not eligible: Not a Nigerian citizen."
    elif age < 18:
        return f"{name}  Not eligible: Underage."
    elif not has_voters_card:
        return f"{name}  Not eligible: No valid voter’s card."
    else:
        return f"{name}  Eligible to vote."


# Example usage
people = [
    ("Alice", 20, "Nigerian", True),
    ("Bob", 16, "Nigerian", True),
    ("Charles", 25, "Ghanaian", True),
    ("Deborah", 22, "Nigerian", False),
]

eligible_voters = []

for person in people:
    result = check_voting_eligibility(*person)
    print(result)
    if "✅" in result:
        eligible_voters.append(person[0])

print("\n🗳️ List of eligible voters:", eligible_voters)
