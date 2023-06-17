from api.v1.authentication.models import User, UserRole

USER_ROLE : list[UserRole] = [
    UserRole(description='Admin'),
    UserRole(description='Profesional'),
    UserRole(description='Cliente'),
]

def get_user(username: str, role : UserRole, password:str, flag: bool, first_name:str = None) -> User:
    user = User(username = username,first_name=first_name, user_role = role, is_staff = flag, is_superuser = flag)
    user.set_password(password)
    return user


USERS : list[User] = [
    get_user('admin',USER_ROLE[0],'admin',True),
    get_user('tomtito',USER_ROLE[1],'tomtito',False),
    get_user('juan',USER_ROLE[1],'123',False),
    get_user('jorge',USER_ROLE[1],'321',False),
    get_user('karina',USER_ROLE[1],'kiki',False),
    get_user('juanpablo',USER_ROLE[1],'jp123',False),
    get_user('Agustin',USER_ROLE[1],'agosto',False),
    get_user('Jaime',USER_ROLE[1],'jaime',False),
    get_user('delirios',USER_ROLE[1],'deli',False),
    get_user('Pabla',USER_ROLE[1],'Diaz',False),
    get_user('bastian',USER_ROLE[1],'paz',False),
    get_user('toti',USER_ROLE[1],'toti',False),
    get_user('gato',USER_ROLE[1],'gato',False),
    get_user('ariel',USER_ROLE[1],'arielox',False),
    get_user('diaz',USER_ROLE[1],'buenos',False),
    get_user('gerardo',USER_ROLE[1],'gomes',False),
    get_user('matias',USER_ROLE[2],'campos',False,'Hasbro'),
    get_user('nico',USER_ROLE[2],'nico',False,'modoDiablo'),
    get_user('Manuel',USER_ROLE[2],'manu',False,'Lego'),
    get_user('mono',USER_ROLE[2],'mono',False,'Walmart'),
    get_user('totin',USER_ROLE[2],'totin',False,'Duoc'),
    get_user('cliente',USER_ROLE[2],'cliente',False,'DC'),
    get_user('javier',USER_ROLE[2],'javier',False,'Vans'),
    get_user('diego',USER_ROLE[2],'diego',False,'Nike'),
    get_user('gaspi',USER_ROLE[2],'gaspi',False,'Mineduc'),
    get_user('tomasito',USER_ROLE[2],'tom',False,'Baltica'),
    get_user('tom',USER_ROLE[2],'tom',False,'Kia'),
    get_user('jojo',USER_ROLE[2],'jojo',False,'Oneseg'),
    get_user('Alexis',USER_ROLE[2],'123',False,'iPhone'),
    get_user('ada',USER_ROLE[2],'celis',False,'MAC'),
    get_user('kiki',USER_ROLE[2],'kiki',False,'Tommy'),
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