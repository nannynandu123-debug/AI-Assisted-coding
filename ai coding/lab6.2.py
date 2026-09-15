ELIGIBLE_LOCATIONS = {
	"tamil nadu",
	"kerala",
	"karnataka",
	"andhra pradesh",
	"telangana",
}
MINIMUM_SCORE = 75.0
MAXIMUM_FAMILY_INCOME = 500000.0


def get_score():
	while True:
		try:
			score = float(input("Enter your academic score (0-100): "))
			if 0 <= score <= 100:
				return score
			print("Score must be between 0 and 100.")
		except ValueError:
			print("Please enter a valid number.")


def get_income():
	while True:
		try:
			income = float(input("Enter your annual family income in rupees: "))
			if income >= 0:
				return income
			print("Income cannot be negative.")
		except ValueError:
			print("Please enter a valid number.")


def check_eligibility(score, family_income, location):
	reasons = []
	normalized_location = location.strip().lower()

	if score < MINIMUM_SCORE:
		reasons.append(f"academic score is below {MINIMUM_SCORE:.0f}")
	if family_income > MAXIMUM_FAMILY_INCOME:
		reasons.append(
			f"family income is above Rs. {MAXIMUM_FAMILY_INCOME:,.0f}"
		)
	if normalized_location not in ELIGIBLE_LOCATIONS:
		reasons.append("location is not covered by this scholarship")

	return reasons


def main():
	print("Scholarship Eligibility Checker")
	print("=" * 34)

	score = get_score()
	family_income = get_income()
	location = input("Enter your state or location: ")

	reasons = check_eligibility(score, family_income, location)

	if not reasons:
		print("\nCongratulations! You are eligible for the scholarship.")
	else:
		print("\nYou are not eligible based on the current criteria:")
		for reason in reasons:
			print(f"- {reason}")


if __name__ == "__main__":
	main()
