# Classe renommée en PascalCase pour respecter PEP 8
class MyClass:
    """
    A class to represent an entity with a full name.

    :param full_name: The full name of the entity.
    :type full_name: str
    """

    # Constructeur avec espaces autour de '='
    def __init__(self, full_name):
        """
        Initialize the MyClass object with a full name.

        :param full_name: The full name of the entity.
        :type full_name: str
        """
        self.full_name = full_name

    # Méthode renommée en snake_case
    def display_name(self):
        """
        Display the full name of the entity.

        :return: None
        :rtype: None
        """
        # Utilisation de print pour afficher un message formaté
        print("Le nom complet est :", self.full_name)


# Classe renommée en PascalCase pour respecter PEP 8
class OtherClass:
    """
    A class to represent an entity with a first name and a last name.

    :param first_name: The first name of the entity.
    :type first_name: str
    :param name: The last name of the entity.
    :type name: str
    """

    def __init__(self, first_name, name):
        """
        Initialize the OtherClass object with a first name and a last name.

        :param first_name: The first name of the entity.
        :type first_name: str
        :param name: The last name of the entity.
        :type name: str
        """
        # Espaces ajoutés autour de '=' pour respecter PEP 8
        self.first_name = first_name
        self.name = name

    def display_name(self):
        """
        Display the full name (first name and last name) of the entity.

        :return: None
        :rtype: None
        """
        # Utilisation des f-strings pour formater le message
        print(f"Nom complet : {self.first_name} {self.name}")
