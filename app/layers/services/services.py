# capa de servicio/lógica de negocio
# Comentario: Lo que hice aca fue importar funciones que se encontraban en la utilidad translator y ademas agregar card.py
from ..persistence import repositories
from ..utilities import translator
from ..utilities.translator import fromRequestIntoCard
from ..utilities.translator import fromTemplateIntoCard
from ..utilities.translator import fromRepositoryIntoCard
from django.contrib.auth import get_user
from ..utilities import card
from ..transport import transport


def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = transport.getAllImages(input) #Llama a la función getallimages que se encuentra en transport.py
    if not json_collection:  # Verifica si la colección está vacía
        return []

       # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []
    for raw_objects in json_collection:
        card = fromRequestIntoCard(raw_objects)
        if input:
            if input.lower() in card.name.lower():
                images.append(card)
            elif input.lower() in card.name.lower():
                images.append(card)
        else:
            images.append(card)

    return images



def saveFavourite(request):
    if not request.user.is_authenticated:
        return None  # Si el usuario no está autenticado, no hace nada
    
    # Transformamos el request POST en una Card usando la función de utilidad
    fav = fromRequestIntoCard(request.POST)  # Transforma el request POST en una Card
    fav.user = request.user  # Asigna el usuario al favorito
    
    # Guardamos el favorito en el repositorio
    return repositories.saveFavourite(fav)  # Guarda el favorito en la base de datos

# Usado desde el template 'favourites.html'

def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []  # Si el usuario no está autenticado, retornamos una lista vacía
    
    user = get_user(request)  # Obtiene el usuario autenticado
    
    # Recupera todos los favoritos del repositorio
    favourite_list = repositories.getAllFavourites(user)  
    
    # Mapea los favoritos para transformarlos en objetos Card
    mapped_favourites = []
    for favourite in favourite_list:
        card = fromRepositoryIntoCard(favourite)  # Convierte el favorito en una Card
        mapped_favourites.append(card)
    
    return mapped_favourites


def deleteFavourite(request):
    favId = request.POST.get('id')  # Obtiene el ID del favorito a eliminar
    if favId:
        # Elimina el favorito del repositorio usando el ID
        return repositories.deleteFavourite(favId) 
    return None  # Si no se proporciona un ID, no hace nada

