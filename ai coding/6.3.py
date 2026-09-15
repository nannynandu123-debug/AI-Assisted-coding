MIN_ENTRANCE_SCORE = 60
MIN_ACADEMIC_MARKS = 60
MIN_INTERVIEW_SCORE = 50


def get_score(prompt):
	while True:
		try:
			score = float(input(prompt))
			if 0 <= score <= 100:
				return score
			print("Enter a score between 0 and 100.")
		except ValueError:
			print("Please enter a valid number.")


def predict_admission(entrance_score, academic_marks, interview_score):
	rejection_reasons = []

	if entrance_score < MIN_ENTRANCE_SCORE:
		rejection_reasons.append(
			f"entrance exam score is below {MIN_ENTRANCE_SCORE}"
		)
	if academic_marks < MIN_ACADEMIC_MARKS:
		rejection_reasons.append(
			f"academic marks are below {MIN_ACADEMIC_MARKS}"
		)
	if interview_score < MIN_INTERVIEW_SCORE:
		rejection_reasons.append(
			f"interview score is below {MIN_INTERVIEW_SCORE}"
		)

	return rejection_reasons


def main():
	print("Admission Selection Predictor")
	print("=" * 30)

	entrance_score = get_score("Enter entrance exam score (0-100): ")
	academic_marks = get_score("Enter academic marks percentage (0-100): ")
	interview_score = get_score("Enter interview score (0-100): ")

	rejection_reasons = predict_admission(
		entrance_score, academic_marks, interview_score
	)

	if not rejection_reasons:
		print("\nDecision: SELECTED")
		print("The student meets all admission criteria.")
	else:
		print("\nDecision: REJECTED")
		print("Reasons:")
		for reason in rejection_reasons:
			print(f"- {reason}")


if __name__ == "__main__":
	main()
