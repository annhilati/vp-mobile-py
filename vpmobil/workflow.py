class Exceptions():
    """
    Enthält verschiedene Exceptions
    """

    class FetchingError(Exception):
        """
        Wenn angeforderte Daten nicht abgerufen werden können

        #### Attribute:
            message (str): Die Fehlermeldung
            status_code (int): Der HTTPS-Fehlercode
        """
        def __init__(self, message: str, status_code: int = None):
            self.message = message
            self.status_code = status_code
        def __str__(self):
            return f"{self.message} (Statuscode: {self.status_code})"
        
    class SchulnummerNotFoundError(FetchingError):
        """
        Wenn die angegebene Schulnummer nicht registriert ist

        #### Attribute:
            message (str): Die Fehlermeldung
        """

    class InvalidCredentialsError(FetchingError):
        """
        Wenn die angegebene Anmeldedaten ungültig sind

        #### Attribute:
            message (str): Die Fehlermeldung
        """

    class XMLParsingError(Exception):
        """
        Wenn XML-Daten nicht richtig geparst werden können

        #### Attribute:
            message (str): Die Fehlermeldung
        """
        def __init__(self, message: str):
            self.message = message

    class XMLNotFound(XMLParsingError):
        """
        Wenn ein XML-Element nicht gefunden werden kann

        #### Attribute:
            message (str): Die Fehlermeldung
        """
        def __init__(self, message: str):
            self.message = message
