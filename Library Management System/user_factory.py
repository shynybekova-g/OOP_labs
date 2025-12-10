from models import Reader, Staff

class UserFactory:
    @staticmethod
    def create_user(user_type: str, person_id: str, name: str):
        t = user_type.strip().lower()
        if t == 'reader':
            return Reader(person_id, name)
        elif t == 'staff':
            return Staff(person_id, name)
        else:
            raise ValueError('Unknown user_type: ' + user_type)
