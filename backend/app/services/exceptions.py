# ユーザーが存在している
class UserAlreadyExistsError(Exception):
    """すでに同一の user_id が存在する場合の例外"""
    pass


# ユーザーの取得に失敗
class UserNotFoundError(Exception):
    pass

# パスワードが違う
class InvalidPasswordError(Exception):
    pass