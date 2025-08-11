class StringUtils:
    @staticmethod
    def capitalize(string: str) -> str:
     
        if len(string) == 0:
            return string
        return string[0].upper() + string[1:]

    @staticmethod
    def trim(string: str) -> str:
       
        return string.lstrip()

    @staticmethod
    def to_list(string: str, delimiter: str = ",") -> list:
      
        if len(string) == 0:
            return []
        return string.split(delimiter)

    @staticmethod
    def contains(string: str, symbol: str) -> bool:
      
        return symbol in string

    @staticmethod
    def delete_symbol(string: str, symbol: str) -> str:
      
        return string.replace(symbol, "")

    @staticmethod
    def starts_with(string: str, symbol: str) -> bool:
      
        return string.startswith(symbol)

    @staticmethod
    def end_with(string: str, symbol: str) -> bool:
       
        return string.endswith(symbol)

    @staticmethod
    def is_empty(string: str) -> bool:
        
        return len(string.strip()) == 0

    @staticmethod
    def list_to_string(lst: list, delimiter: str = ", ") -> str:
      
        return delimiter.join(map(str, lst))

    