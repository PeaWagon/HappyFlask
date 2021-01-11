from app.extensions import db
from app.services.github import GitHub

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    avatar_url = db.Column(db.String(80), nullable=True)
    github_id = db.Column(db.Integer(), nullable=True)

    def __init__(self, username, avatar_url, github_id):
        self.username = username
        self.avatar_url = avatar_url
        self.github_id = github_id

    @staticmethod
    def find_or_create_from_token(access_token):
        data = GitHub.get_user_from_token(access_token)

        """Find existing user or create new User instance"""
        try:
            instance = User.query.filter_by(username=data['login']).first()
        except KeyError:
            # {
            # 'message': 'Must specify access token via Authorization header',
            # 'documentation_url': 'https://docs.github.com/v3/#oauth2-token-sent-in-a-header'
            # }
            # note that the method used in this boilerplate doesn't work
            # and needs updating
            print(data)
            raise KeyError("Please fix me")

        if not instance:
            instance = User(data['login'], data['avatar_url'], data['id'])
            db.session.add(instance)
            db.session.commit()

        return instance

    def __repr__(self):
        return "<User: {}>".format(self.username)
