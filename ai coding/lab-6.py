import hashlib
import json
import os
from getpass import getpass


DATA_FILE = "users.json"


def load_users():
	if not os.path.exists(DATA_FILE):
		return []

	with open(DATA_FILE, "r", encoding="utf-8") as file:
		return json.load(file)


def hash_password(password, salt=None):
	salt = salt or os.urandom(16).hex()
	password_hash = hashlib.pbkdf2_hmac(
		"sha256",
		password.encode("utf-8"),
		salt.encode("utf-8"),
		100_000,
	).hex()
	return salt, password_hash


def add_user():
	name = input("Name: ").strip()
	email = input("Email: ").strip()
	password = getpass("Password: ")

	users = load_users()
	if any(user["email"] == email for user in users):
		print("That email is already registered.")
		return

	salt, password_hash = hash_password(password)
	users.append(
		{
			"name": name,
			"email": email,
			"salt": salt,
			"password_hash": password_hash,
		}
	)

	with open(DATA_FILE, "w", encoding="utf-8") as file:
		json.dump(users, file, indent=4)

	print(f"User saved to {DATA_FILE}.")


def list_users():
	users = load_users()
	if not users:
		print("No users stored yet.")
		return

	for user in users:
		print(f"Name: {user['name']} | Email: {user['email']}")


if __name__ == "__main__":
	print("1. Add user")
	print("2. List users")
	choice = input("Choose an option: ").strip()

	if choice == "1":
		add_user()
	elif choice == "2":
		list_users()
	else:
		print("Invalid option.")
