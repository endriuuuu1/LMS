import uuid

def main():
    uid = uuid.uuid4()
    uid_int = uid.int
    print(uid)
    print(uid_int)

if __name__ == "__main__":
    main()