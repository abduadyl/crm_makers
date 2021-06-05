
def unique_title_generator(instance):
    new_title = f"{instance.course}-{''.join([num if num.isdigit() else '' for num in instance.title])}"
    return new_title
