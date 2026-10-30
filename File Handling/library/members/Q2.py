def add_member(member_list, member_id, name):
    member_list.append({"id": member_id, "name": name})

def display_members(member_list):
    for member in member_list:
        print(member)