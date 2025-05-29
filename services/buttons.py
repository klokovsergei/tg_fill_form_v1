from models.user_data import UserData


def get_buttons_auto(user: UserData, block_names: list[str]) -> list[str]:
    buttons = []
    for name in block_names:
        block = getattr(user, name, None)
        if hasattr(block, 'is_fill') and getattr(block, 'is_fill'):
            buttons.append(f'yes_{name}')
        else:
            buttons.append(name)
    return buttons
