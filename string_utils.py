class StringUtils:
    @staticmethod
    def capitalize(string: str) -> str:
       
        if len(string) == 0:
            return string
        return string[0].upper() + string[1:]

    @staticmethod
    def trim(string: str) -> str:
      
        return string.lstrip()

    