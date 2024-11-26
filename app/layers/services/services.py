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

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    if not request.user.is_authenticated:
        return None
    fav = fromRequestIntoCard(request.POST) # transformamos un request del template en una Card.
    fav.user = request.user # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = getAllFavourites(user) # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = fromRepositoryIntoCard(favourite) # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.
