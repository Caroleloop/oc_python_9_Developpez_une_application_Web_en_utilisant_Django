from django import template

register = template.Library()


@register.filter
def instance_of(obj, class_name):
    """
    Filtre Django custom qui vérifie si l'objet est une instance d'une classe donnée
    en comparant le nom de la classe.

    Args:
        obj (object): L'objet à tester.
        class_name (str): Le nom de la classe (en string) à comparer.

    Returns:
        bool: True si l'objet est une instance de la classe spécifiée, False sinon.
    """
    return obj.__class__.__name__ == class_name
