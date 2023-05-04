from flask import Flask

from app.controller.user_bp import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

app.secret_key = "Thekeysisjustakey"
