import hashlib
import json


DB_NAME = "users.json"


class User:
    def __init__(self):
        pass

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def create_account(self, email, password):
        with open(DB_NAME, "r", encoding="UTF-8") as db:
            users = json.load(db)
            for user in users:
                if user["login"] == email:
                    return False

        with open(DB_NAME, "w", encoding="UTF-8") as db:
            hashed_password = self._hash_password(password)
            user = {'login': email, 'password': hashed_password,
                    'genres': [], 'authors': [], 'rated_songs': [{'author': '', 'name': '', 'rate': 0, 'review': ''}]}
            users.append(user)
            json.dump(users, db, ensure_ascii=False, indent=4)
        return True

    def auth(self, email, password):
        with open(DB_NAME, "r", encoding="UTF-8") as db:
            users = json.load(db)
            for user in users:
                if user["login"] == email:
                    flag = True
                    h_password = self._hash_password(password)
                    if h_password == user["password"]:
                        return True
                    else:
                        return False
            if flag == False:
                return False


# a = User()
# print(a.create_account('kasot@ya.ru', 'aasadр'))
# print(a.auth('kasot@ya.ru', 'aasadрp'))
