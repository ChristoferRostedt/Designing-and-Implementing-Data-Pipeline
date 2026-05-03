class FileHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> list[str]:
        """Reads rows from the file, handling errors if the file is missing."""
        try:
            with open(self.filepath, 'r', encoding="UTF-8") as f:
                return [line.rstrip('\n') for line in f]
        except FileNotFoundError:
            return []

    def write(self, data: list[str]):
        """Writes serialized strings to the file."""
        with open(self.filepath, 'w', encoding="UTF-8") as f:
            for line in data:
                f.write(line + '\n')

class DataSecurity:
    @staticmethod
    def encrypt(text: str) -> str:
        """Simple XOR-based encryption for demonstration."""
        return "".join(chr(ord(c) ^ 42) for c in text)

    @staticmethod
    def decrypt(text: str) -> str:
        """Decrypts the XOR-encrypted string."""
        return "".join(chr(ord(c) ^ 42) for c in text)