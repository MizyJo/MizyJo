"""
URL configuration for assuranceAro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from vitrine.views import index, service, tarifs, about, contact, accueil, dashboard_admin, \
    auth_admin, admin_login, page2, page1, ajout_departement, admin_accueil, logout_views, add_service, \
    add_actualite, add_departement, get_service, edit_service, get_departement, get_actualite, \
    edit_departement, edit_actualite, supprimer_donnee_service, \
    supprimer_donnee_departement, supprimer_donnee_actualite, new_users, register_user, historique, ajout_apropos, \
    add_apropos, autre, users, groupes, attribute_groupe, affiche_groupe, delete_groupe_users, statut, delete_users, \
    create_groupe, add_group, ens_group, get_groupe, edit_group, delete_groupe, dash_view, graphe, permission, \
    attribuer_permission, view_permissions, delete_permission, ajout_agence, add_agence, get_agence, edit_agence, \
    agence, titre, equipe, add_equipe, get_apropos, edit_apropos, delete_agence, delete_apropos, delete_equipe, \
    get_departement_inactive, replace_departement, get_service_inactive, replace_service, get_actualite_inactive, \
    get_agence_inactive, get_apropos_inactive, get_equipe_inactive, replace_agence, replace_actualite, replace_apropos, \
    replace_equipe, changer_promotion, superuser, save_superuser

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('lsdfkmjdsmkhllmksjdf345jmlkj54MLJLKJhlhjh', superuser, name="superuser"),
    path('sdmfjdslkfjlmkjijgmlkjgidgjdfsgidsfjmsdlfkjgdflkgj', save_superuser, name="save_superuser"),
    path('', index),
    path('service', service, name="service"),
    path('agence', agence, name="agence"),
    path('tarif', tarifs, name="tarif"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('accueil', accueil, name="accueil"),
    path('administrateur', auth_admin, name="administrateur"),
    path('dashboard', dashboard_admin, name="dashboard"),
    path('admin_login', admin_login, name="admin_admin"),
    path('ajout_actualite', page1, name='ajout_actualite'),
    path('ajout_service', page2, name='ajout_service'),
    path('ajout_departement', ajout_departement, name='ajout_departement'),
    path('ajout_apropos', ajout_apropos, name='ajout_apropos'),
    path('admin_accueil', admin_accueil, name="admin_accueil"),
    path('logout', logout_views, name="logout"),
    path('add_apropos', add_apropos, name="add_apropos"),
    path('add_service', add_service, name="add_service"),
    path('add_actualite', add_actualite, name="add_actualite"),
    path('add_departement', add_departement, name="add_departement"),
    path('get_service', get_service, name="get_service"),
    path('edit_service', edit_service, name="edit_service"),
    path('get_departement', get_departement, name="get_departement"),
    path('edit_departement', edit_departement, name="edit_departement"),
    path('get_actualite', get_actualite, name="get_actualite"),
    path('edit_actualite', edit_actualite, name="edit_actualite"),
    path('get_agence', get_agence, name="get_agence"),
    path('edit_agence', edit_agence, name="edit_agence"),
    path('get_apropos', get_apropos, name="get_apropos"),
    path('edit_apropos', edit_apropos, name="eedit_apropos"),
    path('delete_service', supprimer_donnee_service, name="delete_service"),
    path('delete_departement', supprimer_donnee_departement, name="delete_deparrtement"),
    path('delete_actualite', supprimer_donnee_actualite, name="delete_actualite"),
    path('delete_agence/<int:id>', delete_agence, name="delete_agence"),
    path('new_users', new_users, name="new_users"),
    path('register_users', register_user, name="register_users"),
    path('historique', historique, name="historique"),
    path('ajout_autre', autre, name="ajout_autre"),
    path('users', users, name="users"),
    path('groupe', groupes, name="groupes"),
    path('attr_groupe', attribute_groupe, name="attribute_groupe"),
    path('affiche_groupe', affiche_groupe, name="affiche_groupe"),
    path('delete_groupe/<int:id_group>/<int:id_users>', delete_groupe_users, name="delete_groupe_users"),
    path('statut/<int:id>', statut, name='statut'),
    path('delete_users/<int:id>', delete_users, name="delete_users"),
    path('create_groupe', create_groupe, name="create_groupe"),
    path('add_groupe', add_group, name="add_groupe"),
    path('edit_or_delete_groupe', ens_group, name="edit_or_delete_groupe"),
    path('get_groupe', get_groupe, name="get_groupe"),
    path('edit_groupe', edit_group, name="edit_groupe"),
    path('delete_groupe_by_id/<int:id>', delete_groupe, name="delete_groupe_by_id"),
    path('stat', dash_view, name="dash_view"),
    path('graphe', graphe, name="graphe"),
    path('permission', permission, name="permission"),
    path('attribuer_permission', attribuer_permission, name="atttribuer_permission"),
    path('view_permissions', view_permissions, name="view_permissions"),
    path('delete_permission/<int:id_permission>/<int:id_user>', delete_permission, name="delete_permission"),
    path('ajout_agence', ajout_agence, name="ajout_agence"),
    path('add_agence', add_agence, name="add_agence"),
    path('titre', titre, name="titre"),
    path('equipe', equipe, name="equipe"),
    path('add_equipe', add_equipe, name="add_equipe"),
    path('delete_apropos/<int:id>', delete_apropos, name="delete_apropos"),
    path('delete_equipe/<int:id>', delete_equipe, name="delete_equipe"),
    path('get_departement_inactive', get_departement_inactive, name="get_departement_inactive"),
    path('replace_departement/<int:id_active>/<int:id_inactive>', replace_departement, name="replace_departement"),
    path('get_service_inactive', get_service_inactive, name="get_service_inactive"),
    path('replace_service/<int:id_active>/<int:id_inactive>', replace_service, name="replace_service"),
    path('get_actualite_inactive', get_actualite_inactive, name="get_actualite_inactive"),
    path('get_agence_inactive', get_agence_inactive, name="get_agence_inactive"),
    path('get_apropos_inactive', get_apropos_inactive, name="get_apropos_inactive"),
    path('get_equipe_inactive', get_equipe_inactive, name="get_equipe_inactive"),
    path('replace_agence/<int:id_active>/<int:id_inactive>', replace_agence, name="replace_agence"),
    path('replace_actualite/<int:id_active>/<int:id_inactive>', replace_actualite, name="replace_actualite"),
    path('replace_apropos/<int:id_active>/<int:id_inactive>', replace_apropos, name="replace_apropos"),
    path('replace_equipe/<int:id_active>/<int:id_inactive>', replace_equipe, name="replace_equipe"),
    path('changer_promotion/<int:service_id>', changer_promotion, name="changer_promotion"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
