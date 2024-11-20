# capa de servicio/lógica de negocio
# Comentario: Lo que hice aca fue importar funciones que se encontraban en la utilidad translator y ademas agregar card.py
from ..persistence import repositories
from ..utilities import translator
from ..utilities.translator import fromRequestIntoCard
from ..utilities.translator import fromTemplateIntoCard
from ..utilities.translator import fromRepositoryIntoCard
from django.contrib.auth import get_user
from ..utilities import card
from .services import transport 

def getAllImages(input=None):
    # obtiene un listado de datos "crudos" desde la API, usando a transport.py.
    json_collection = getAllImages(input) #Llama a la función getallimages que se encuentra en transport.py

    # recorre cada dato crudo de la colección anterior, lo convierte en una Card y lo agrega a images.
    images = []
    for raw_objects in json_collection:
        card = fromRequestIntoCard(raw_objects)
        images.append(card)
    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.
