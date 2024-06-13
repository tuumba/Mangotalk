from flask import Flask,g, render_template, request, session,redirect,url_for
from models import ChatMessage
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mangotok.db'
db = SQLAlchemy(app)

def init_db():
    pass

@app.cli.command('initdb')
def init_db_command():
    with app.app_context():
        init_db()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/chats')
def chats():
    return render_template('chats.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

# @app.route('/chat1/<int:user_id>')
# def chat(user_id):
#     # 채팅 메시지 불러오기
#     chat_messages = ChatMessage.query.filter(
#         (ChatMessage.sender_id == session['user_id'] and ChatMessage.receiver_id == user_id)
#         or (ChatMessage.sender_id == user_id and ChatMessage.receiver_id == session['user_id'])
#     ).order_by(ChatMessage.created_at).all()

#     # 채팅 화면 렌더링
#     return render_template('chat1.html', user_id=user_id, chat_messages=chat_messages)

# @app.route('/chat1/<int:user_id>', methods=['POST'])
# def send_message(user_id):
#     # 메시지 저장
#     new_message = ChatMessage(
#         sender_id=session['user_id'],
#         receiver_id=user_id,
#         content=request.form['message'],
#     )
#     db.session.add(new_message)
#     db.session.commit()

#     # 채팅 화면 새로고침
#     return redirect(url_for('chat1', user_id=user_id))

if __name__ == '__main__':
    app.run()
