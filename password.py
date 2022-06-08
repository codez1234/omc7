import base64
import hashlib
import secrets

ALGORITHM = "pbkdf2_sha256"


def hash_password(password, salt=None, iterations=320000):
    if salt is None:
        salt = secrets.token_hex(11)
        print(salt)
    assert salt and isinstance(salt, str) and "$" not in salt
    assert isinstance(password, str)
    pw_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations
    )
    b64_hash = base64.b64encode(pw_hash).decode("ascii").strip()
    return "{}${}${}${}".format(ALGORITHM, iterations, salt, b64_hash)


def verify_password(password, password_hash):
    if (password_hash or "").count("$") != 3:
        return False
    algorithm, iterations, salt, b64_hash = password_hash.split("$", 3)
    iterations = int(iterations)
    assert algorithm == ALGORITHM
    compare_hash = hash_password(password, salt, iterations)
    return secrets.compare_digest(password_hash, compare_hash)


# salt == EkAhjshyeYYPvI3z9r12AB, j8IXkF5SJrA8JfW3wJzyTu {by django}
# pbkdf2_sha256$320000$j8IXkF5SJrA8JfW3wJzyTu$tx3nhDkbouX8nsXcEK2pLDM6xamU1r1Ta8e+9lWoWXI= {by django}

# django uses {iterations = 320000, salt = secrets.token_hex(11)}

# ==========================================


# pbkdf2_sha256$260000$f046b4c4858e0ff40491944cfd11c53b$HfKyXBQb2iD1ROt4uulovBT/F01h6sDsnOTLobXkab0= {for iterations = 260000, salt = secrets.token_hex(16)}
# pbkdf2_sha256$320000$421c8cf8e2d82d2200e291302aec07e9$yI5PGY02pzVMf7Xt5Gq1+TdngGnPMxZATp+0Ce/+3ho= {for iterations = 320000, salt = secrets.token_hex(16)}
# salt == cfa342b664d731bf266f20e39401bc64, 421c8cf8e2d82d2200e291302aec07e9 {salt = secrets.token_hex(16)}

# salt == bca498bc2c8bc0583a29a6, 01e1af3e97a6d77b298c21 {salt = secrets.token_hex(11)}
# print(len("01e1af3e97a6d77b298c21"))
password = hash_password("Raj123")
print(password)

x = verify_password(
    "Power@omc@2022!", "pbkdf2_sha256$320000$tuDJdBGRNiP2f8QMEL5mvc$+chGxx+6ypgBZZe0fFhaWi1LWC3e2O5iA8mlN80f03k=")

print(x)
