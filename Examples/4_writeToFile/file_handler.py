class  FileHandler: 
    filepath : str #indicated filepath is expected to be a string
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        return None
    
    def read(self) -> list[str]: 
        rows:list[str] = []
        try: 
            filehandle = open(self.filepath, 'r', encoding="UTF-8")
            row = filehandle.readline()
            while row != '': 
                rows.append(row.rstrip('\n'))
                row = filehandle.readline()
        except Exception: 
            print (f"File not found")
            exit (-1)
        return rows 
    
    def write(self, rows:list[str]) -> None:
        try:
            filehandle = open(self.filepath, 'w', encoding="UTF-8")
            for row in rows:
                filehandle.write(f"{row}\n")
            filehandle.close()
        except Exception:
            print(f"Failed to write file '{self.filepath}'")
            exit(-1)
        return None