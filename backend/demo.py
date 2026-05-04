import uuid

def main():
    uid = uuid.uuid4()
    uid_int = uid.int
    uid_hex = uid.hex
    my_dict = {}
    my_dict[uid_hex] = "uid"
    my_dict[str(uid)] = "shmuaidi"
    print(uid)
    print(uid_int)
    print(uid_hex)
    print(my_dict)

if __name__ == "__main__":
    main()