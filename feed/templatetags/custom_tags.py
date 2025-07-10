from django import template

register = template.Library()


@register.filter(name="instanceof")
def instanceof(obj, class_name):
    """
    Filtre personnalisé Django qui vérifie si un objet est une instance d'une classe donnée
    en comparant le nom de la classe de l'objet à une chaîne de caractères.

    Args:
        obj (object): L'objet à tester.
        class_name (str): Le nom de la classe (en string) avec laquelle comparer.

    Returns:
        bool: True si le nom de la classe de l'objet correspond à class_name, sinon False.

    Note:
        Cette méthode compare uniquement le nom de la classe (obj.__class__.__name__),
        elle ne prend pas en compte l'héritage ou les sous-classes.
        Pour une vérification plus robuste, on pourrait importer la classe et utiliser isinstance().
    """
    return obj.__class__.__name__ == class_name
