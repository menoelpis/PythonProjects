from user import User
import json

user = User("Daniel")

user.add_movie("Benhur", "History")
user.add_movie("The Passion of Christ", "History")

with open('my_file.txt', 'w') as f:
  json.dump(user.json(), f)