from api.v1.authentication.models import User, UserRole

USER_ROLE : list[UserRole] = [
    UserRole(description='administrador'),
    UserRole(description='ferretero'),
    UserRole(description='cliente'),
]

def get_user(username: str, role : UserRole, password:str, flag: bool, first_name:str = None) -> User:
    user = User(username = username,first_name=first_name, user_role = role, is_staff = flag, is_superuser = flag)
    user.set_password(password)
    return user


USERS : list[User] = [
    get_user('admin',USER_ROLE[0],'admin',True),
    get_user('nico',USER_ROLE[1],'nico123',False),

]

ENTITY = {
    'USER_ROLE': USER_ROLE,
    'USERS' : USERS,
}

def save_entity(model_name : str):
    for generic in ENTITY[model_name]:
        generic.save()


def run_seed():
    try:
        for key in ENTITY.keys():
            print(key)
            save_entity(key)

        return True
    except: return False