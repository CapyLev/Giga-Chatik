import hashlib
import secrets


class Hasher:
    @staticmethod
    async def hash_password(password: str) -> str:
        salt = secrets.token_hex(16)
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        return f"{salt}${hashed_password}"

    @staticmethod
    async def verify_password(raw_password: str, hashed_password: str) -> bool:
        try:
            salt, original_hash = hashed_password.split("$", 1)
        except ValueError:
            return False

        calculated_hash = hashlib.sha256((raw_password + salt).encode()).hexdigest()
        return calculated_hash == original_hash
