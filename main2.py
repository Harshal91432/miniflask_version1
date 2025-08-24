from flask import Flask


app = Flask(__name__)


#####################################
#How to create Path parameter in flask?
####################################

@app.route("/user/<username>")
def show_user_profile(username):
    # show user profile based on username
    return f"User {username} profile....."

#####################################
#How to create Path parameter in flask with datatype?
####################################

@app.route("/story/<int:story_number>")
def show_story(story_number):
    # Logic to show story with given "story number" (which is a integer)
    return f"DETAIL STORY - story number {story_number}"



