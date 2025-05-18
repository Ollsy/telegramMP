def get_info_from_txt(name_file: str, len_id: int = None) -> dict:
    file = open(name_file, mode='r', encoding="UTF-8")

    data = {}

    for line_doc in file.readlines():
        line_doc = line_doc.replace("\n", "")
        if not line_doc:
           continue   
        line_list = line_doc.split()
        id_chat = line_list[0]
        name_chat = "".join(line_list[1:])
        if len_id is not None and len(id_chat) != len_id:
            print(Exception(f"неверная длина id {name_chat}, {id_chat}, {name_file}"))
   
        
        data[name_chat] = id_chat
    
    file.close()

    return data
    

def get_pair_id(clearlist_dict: dict, blacklist_dict: dict) -> dict:

    id_info = {}

    for clearlist_name in clearlist_dict:
        number_of_clear_name = ""
        for symbol in clearlist_name:
            if symbol.isdigit():
                number_of_clear_name += symbol

        for blacklist_name in blacklist_dict:
            if number_of_clear_name in blacklist_name:
                id_draft = int(blacklist_dict[blacklist_name])
                id_clear = int(clearlist_dict[clearlist_name])
                id_info[id_draft] = id_clear    
    return id_info


def get_chats_id_info(name_blacklist: str, name_clearlist: str) -> dict:
    clear = get_info_from_txt(name_clearlist, 14)
    draft = get_info_from_txt(name_blacklist, 10)
    info = get_pair_id(clear, draft)
    return info
