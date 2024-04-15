import json
import os
from datetime import datetime, timedelta

from django.contrib.auth.models import User, Group, Permission
from django.db.models import Count
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required, permission_required
from assuranceAro import settings
from vitrine.models import Service, Article, Prix, Departement, Apropos, Agence, Autre, Equipe


# Create your views here.
def index(request):
    active_page = 'accueil'
    article = Article.objects.all()
    autre = Autre.objects.get(pk=1)
    equipe = Equipe.objects.all()
    print(autre)
    return render(request, 'index.html', {'active_page': active_page, 'article': article, 'autre': autre, 'equipe': equipe})


def service(request):
    service = Service.objects.all()
    active_page = 'service'
    base_dir = settings.BASE_DIR
    return render(request, 'service.html', {'active_page': active_page, 'service': service, 'base_dir': base_dir})


def agence(request):
    agence = Agence.objects.all()
    active_page = 'departement'
    return render(request, 'departement.html', {'active_page': active_page, 'agence': agence})


def tarifs(request):
    prix = Prix.objects.all()
    return render(request, 'tarif.html', {'prix': prix})


def about(request):
    active_page = 'about'
    apropos = Apropos.objects.all()
    return render(request, 'about.html', {'active_page': active_page, 'apropos':  apropos})


def contact(request):
    active_page = 'contact'
    return render(request, 'contact.html', {'active_page': active_page})


def accueil(request):
    active_page = 'accueil'
    article = Article.objects.all()
    autre = Autre.objects.get(pk=1)
    equipe = Equipe.objects.all()
    print(autre)
    return render(request, 'index.html', {'active_page': active_page, 'article': article, 'autre': autre, 'equipe': equipe})


def administrateur(request):
    return render(request, 'admin/admin.html')


def auth_admin(request):
    return render(request, 'admin/admin.html')


@login_required
def dashboard_admin(request):
    if request.user.is_authenticated:
        # L'utilisateur est connecté, exécutez le code pour la vue
        # par exemple, redirigez-le vers une autre page
        service = Service.objects.filter(is_active=True)
        departement = Departement.objects.filter(is_active=True)
        agence = Agence.objects.all()
        actualite = Article.objects.filter(is_active=True)
        apropos = Apropos.objects.all()
        equipe = Equipe.objects.all()
        active_page = "dashboard"
        return render(request, 'admin/dashboard.html',
                      {'active_page': active_page, 'service': service, 'departement': departement, 'agence': agence,
                       'article': actualite,
                       'apropos': apropos,
                       'equipe': equipe})
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return redirect(reverse('admin_login'))


@csrf_protect
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('pseudo')
        password = request.POST.get('password')
        print(username + password)
        user = authenticate(username=username, password=password)
        try:
            utilisateur = User.objects.get(username=username)
        except User.DoesNotExist:
            utilisateur = None
        print(utilisateur)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard'))

        else:
            if utilisateur is not None:
                if utilisateur.is_active == False:
                    return render(request, 'admin/admin.html',
                                  {'error_message': "Votre compte est désactivé"})
            else:
                return render(request, 'admin/admin.html',
                              {'error_message': "Nom d'utilisateur ou mot de passe incorrrècte"})
            # Gérer l'échec de l'authentification pour l'administrateur
    else:
        return render(request, 'admin/admin.html')


@permission_required('vitrine.add_article')
def page1(request):
    if request.user.is_authenticated:
        # L'utilisateur est connecté, exécutez le code pour la vue
        # par exemple, redirigez-le vers une autre page
        active_page = "ajout_actualite"
        return render(request, "admin/ajout_actualite.html", {'active_page': active_page})
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return redirect(reverse('administrateur'))


@permission_required('vitrine.add_service')
def page2(request):
    if request.user.is_authenticated:
        # L'utilisateur est connecté, exécutez le code pour la vue
        # par exemple, redirigez-le vers une autre page
        active_page = 'ajout_service'
        return render(request, "admin/ajout_service.html", {'active_page': active_page})
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return redirect(reverse('administrateur'))


@permission_required('vitrine.add_prix')
def ajout_prix(request):
    if request.user.is_authenticated:
        service = Service.objects.all()
        active_page = 'ajout_prix'
        return render(request, 'admin/ajout_prix.html', {'active_page': active_page, 'service': service})
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return redirect(reverse('administrateur'))


@permission_required('vitrine.add_departement')
def ajout_departement(request):
    if request.user.is_authenticated:
        # L'utilisateur est connecté, exécutez le code pour la vue
        # par exemple, redirigez-le vers une autre page
        active_page = 'ajout_departement'
        return render(request, 'admin/ajout_departement.html', {'active_page': active_page})
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return redirect(reverse('administrateur'))


def ajout_apropos(request):
    if request.user.is_authenticated:
        active_page = "ajout_apropos"
        return render(request, 'admin/ajout_apropos.html', {'active_page': active_page})
    else:
        redirect(reverse('administrateur'))


def admin_accueil(request):
    if request.user.is_authenticated:
        # L'utilisateur est connecté, exécutez le code pour la vue
        # par exemple, redirigez-le vers une autre page
        active_page = 'admin_accueil'
        return render(request, 'admin/dashboard.html', {'active_page': active_page})
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return redirect(reverse('administrateur'))


def logout_views(request):
    logout(request)
    # Redirigez l'utilisateur vers une autre page (par exemple, la page d'accueil)
    return redirect('/administrateur')


def delete_users(request, id):
    users = get_object_or_404(User, pk=id)
    users.delete()
    all_users = User.objects.all()
    return render(request, "admin/users.html",
                  {"active_page": "users", 'success_message': "Suppression d''utilisateur réussi avec succès",
                   'users': all_users})


@permission_required('vitrine.add_apropos')
def add_apropos(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        icone = request.POST.get('icone')
        if titre == "" or description == "" or icone == "":
            error_message = "Tous les champs sont obligatoire"
            return render(request, "admin/ajout_apropos.html", {'error_message': error_message})
        else:
            apropos = Apropos.objects.create(titre=titre, description=description, icone=icone)
            apropos.save()
            return render(request, 'admin/ajout_apropos.html', {'success_message': "A-propos ajouté avec succès"})


@permission_required('vitrine.add_service')
def add_service(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        icone = request.POST.get('icone')
        photo = request.FILES.get('photo')
        print(nom + description + icone)
        if nom == "" or description == "" or icone == "" or photo is None:
            error_message = "Les champs sont obligatoire."
            return render(request, 'admin/ajout_service.html', {'error_message': error_message})
        else:
            Service.objects.create(nom=nom, description=description, icone=icone, photo=photo)
            success_message = "Service ajouté avec succès"
            return render(request, 'admin/ajout_service.html', {'success_message': success_message})
    else:
        # Affichez le formulaire vide
        error_message = "methode post obligatoire"
        return render(request, 'admin/ajout_service.html', {'message': error_message})


@permission_required('vitrine.add_article')
def add_actualite(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        datetime = timezone.now()
        if image and titre != "" and description != "":
            # Spécifiez le répertoire de destination dans le dossier static de votre application
            destination_directory = os.path.join('vitrine/static/img/actualite', image.name)
            # Écrivez le contenu du fichier téléchargé dans un fichier dans le dossier static
            with open(destination_directory, 'wb') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            # Enregistrez l'URL du fichier dans la base de données
            image_url = 'img/actualite/' + image.name
            votre_objet = Article.objects.create(titre=titre, description=description, image_url=image_url,
                                                 date=datetime)
            votre_objet.save()
            return render(request, 'admin/ajout_actualite.html',
                          {'success_message': "Ajout de l'actualité avec succès"})
        else:
            return render(request, 'admin/ajout_actualite.html',
                          {'error_message': "Vérifier bien votre image et votre saisie"})
    else:
        redirect(reverse('dashboard'))


@permission_required('vitrine.add_departement')
def add_departement(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        if image and nom != "" and description != "":
            destination_directory = os.path.join('vitrine/static/img/departement', image.name)
            with open(destination_directory, 'wb') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            # Enregistrez l'URL du fichier dans la base de données
            image_url = 'img/departement/' + image.name
            votre_objet = Departement.objects.create(nom=nom, description=description, image_url=image_url)
            votre_objet.save()
            return render(request, 'admin/ajout_departement.html',
                          {'success_message': "Ajout du département avec succès"})
        else:
            return render(request, 'admin/ajout_departement.html',
                          {'error_message': "Vérifier bien votre image et votre saisie"})
    else:
        return redirect('/')


@permission_required('vitrine.add_prix')
def add_prix(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prix = request.POST.get('prix')
        icone = request.POST.get('icone')
        print(nom + prix + icone)
        # Ajoutez vos conditions de validation
        if nom == "" or prix == "" or icone == "":
            error_message = "Les champs sont obligatoire."
            service = Service.objects.all()
            return render(request, 'admin/ajout_prix.html', {'error_message': error_message, 'service': service})
        else:
            # Traitement supplémentaire si les données sont valides
            Prix.objects.create(nom=nom, prix=prix, icone=icone)
            service = Service.objects.all()
            success_message = "Prix ajouté avec succès"
            return render(request, 'admin/ajout_prix.html', {'success_message': success_message, 'service': service})
    else:
        # Affichez le formulaire vide
        error_message = "methode post obligatoire"
        return render(request, 'admin/ajout_prix.html', {'message': error_message})


def get_service(request):
    if request.method == 'GET':
        # Récupérer l'identifiant de la donnée à partir des paramètres de la requête
        donnee_id = request.GET.get('id')
        # Récupérer l'instance de l'objet à partir de l'identifiant
        instance = get_object_or_404(Service, id=donnee_id)
        # Préparer les données à renvoyer sous forme de JSON
        data = {
            'nom': instance.nom,
            'description': instance.description,
            'icone': instance.icone,
            'id': instance.id,
            # Ajoutez d'autres champs si nécessaire
        }
        # Renvoyer les données sous forme de JSON
        return JsonResponse(data)
    else:
        # Si la méthode de la requête n'est pas GET, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


def edit_service(request):
    if request.method == 'POST':
        id_donnee = request.POST.get('idDonnee')
        photo = request.FILES.get('photo')
        instance = get_object_or_404(Service, id=id_donnee)
        instance.nom = request.POST.get('nom')
        instance.description = request.POST.get('description')
        instance.icone = request.POST.get('icone')
        instance.photo = photo
        instance.update_at = timezone.now()
        instance.save()
        # Répondre avec un JSON pour indiquer que la modification a réussi
        return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


def get_departement(request):
    if request.method == 'GET':
        # Récupérer l'identifiant de la donnée à partir des paramètres de la requête
        donnee_id = request.GET.get('id')
        # Récupérer l'instance de l'objet à partir de l'identifiant
        instance = get_object_or_404(Departement, id=donnee_id)
        # Préparer les données à renvoyer sous forme de JSON
        print(instance)
        data = {
            'nom': instance.nom,
            'description': instance.description,
            'id': instance.id,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


def get_actualite(request):
    if request.method == 'GET':
        # Récupérer l'identifiant de la donnée à partir des paramètres de la requête
        donnee_id = request.GET.get('id')
        # Récupérer l'instance de l'objet à partir de l'identifiant
        instance = get_object_or_404(Article, id=donnee_id)
        # Préparer les données à renvoyer sous forme de JSON
        data = {
            'titre': instance.titre,
            'description': instance.description,
            'id': instance.id,
        }
        # Renvoyer les données sous forme de JSON
        return JsonResponse(data)
    else:
        # Si la méthode de la requête n'est pas GET, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


def get_agence(request):
    if request.method == 'GET':
        # Récupérer l'identifiant de la donnée à partir des paramètres de la requête
        donnee_id = request.GET.get('id')
        # Récupérer l'instance de l'objet à partir de l'identifiant
        instance = get_object_or_404(Agence, id=donnee_id)
        print(instance)
        # Préparer les données à renvoyer sous forme de JSON
        data = {
            'id': instance.id,
            'nom': instance.nom,
            'rue': instance.rue,
            'telephone': instance.telephone,

        }
        # Renvoyer les données sous forme de JSON
        return JsonResponse(data)
    else:
        # Si la méthode de la requête n'est pas GET, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('auth.change_group')
def get_groupe(request):
    if request.method == 'GET':
        # Récupérer l'identifiant de la donnée à partir des paramètres de la requête
        donnee_id = request.GET.get('id')
        # Récupérer l'instance de l'objet à partir de l'identifiant
        instance = get_object_or_404(Group, id=donnee_id)
        print(instance)
        permissions = instance.permissions.all()
        allPermission = Permission.objects.all()
        # Préparer les données à renvoyer sous forme de JSON
        permissions_possedees_data = [{'id': permission.id, 'nom': permission.name} for permission in permissions]
        toutes_permissions_data = [{'id': permission.id, 'nom': permission.name} for permission in allPermission]

        data = {
            'id': instance.id,
            'nom': instance.name,
            'permission': permissions_possedees_data,
            'allPermission': toutes_permissions_data,
        }
        # Renvoyer les données sous forme de JSON
        return JsonResponse(data)
    else:
        # Si la méthode de la requête n'est pas GET, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('auth.change_group')
def edit_group(request):
    if request.method == 'POST':
        id_donnee = request.POST.get('idDonnee')
        instance = get_object_or_404(Group, id=id_donnee)
        nom = request.POST.get('nom')
        permissions_id = request.POST.getlist('permission')
        permissions = Permission.objects.filter(pk__in=permissions_id)
        instance.name = nom
        instance.permissions.clear()
        instance.permissions.add(*permissions)
        instance.save()
        # Répondre avec un JSON pour indiquer que la modification a réussi
        return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('vitrine.change_agence')
def edit_agence(request):
    if request.method == 'POST':
        id_donnee = request.POST.get('idDonneeAgence')
        instance = get_object_or_404(Agence, id=id_donnee)
        instance.nom = request.POST.get('nom')
        instance.rue = request.POST.get('rue')
        instance.telephone = request.POST.get('telephone')
        instance.update_at = datetime.now()
        if request.FILES.get("photo"):
            instance.photo = request.FILES.get("photo")
        instance.save()
        # Répondre avec un JSON pour indiquer que la modification a réussi
        return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('vitrine.change_article')
def edit_actualite(request):
    if request.method == 'POST':
        id_donnee = request.POST.get('idDonneeActualite')
        image = request.FILES.get('image')
        instance = get_object_or_404(Article, id=id_donnee)
        if image:
            # Spécifiez le répertoire de destination dans le dossier static de votre application
            destination_directory = os.path.join('vitrine/static/img/actualite', image.name)
            # Écrivez le contenu du fichier téléchargé dans un fichier dans le dossier static
            with open(destination_directory, 'wb') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            # Enregistrez l'URL du fichier dans la base de données
            image_url = 'img/actualite/' + image.name
            instance.titre = request.POST.get('titre')
            instance.description = request.POST.get('description')
            instance.image_url = image_url
            instance.date = timezone.now()
            instance.save()
            return JsonResponse({'success': True})
        else:
            instance.titre = request.POST.get('titre')
            instance.description = request.POST.get('description')
            instance.date = timezone.now()
            instance.save()
            print('tsisy sary')
            # Répondre avec un JSON pour indiquer que la modification a réussi
            return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('vitrine.change_departement')
def edit_departement(request):
    if request.method == 'POST':
        id_donnee = request.POST.get('idDonneeDepartement')
        image = request.FILES.get('image')
        instance = get_object_or_404(Departement, id=id_donnee)
        if image:
            # Spécifiez le répertoire de destination dans le dossier static de votre application
            destination_directory = os.path.join('vitrine/static/img/Departement', image.name)
            # Écrivez le contenu du fichier téléchargé dans un fichier dans le dossier static
            with open(destination_directory, 'wb') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
            # Enregistrez l'URL du fichier dans la base de données
            image_url = 'img/departement/' + image.name
            instance.nom = request.POST.get('nom')
            instance.description = request.POST.get('description')
            instance.image_url = image_url
            instance.save()
            return JsonResponse({'success': True})
        else:
            instance.nom = request.POST.get('nom')
            instance.description = request.POST.get('description')
            instance.save()
            # Répondre avec un JSON pour indiquer que la modification a réussi
            return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('vitrine.delete_prix')
def supprimer_donnee_prix(request):
    if request.method == 'POST':
        # Récupérer l'identifiant de la donnée à supprimer depuis les données de la requête POST
        id_donnee = request.POST.get('id_prix')
        # Supprimer l'instance de l'objet
        instance = get_object_or_404(Prix, id=id_donnee)
        instance.is_active = False
        # Répondre avec un JSON pour indiquer que la suppression a réussi
        return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('vitrine.delete_service')
def supprimer_donnee_service(request):
    if request.method == 'POST':
        # Récupérer l'identifiant de la donnée à supprimer depuis les données de la requête POST
        id_donnee = request.POST.get('id_service')
        # Supprimer l'instance de l'objet
        instance = get_object_or_404(Service, id=id_donnee)
        instance.delete()
        # Répondre avec un JSON pour indiquer que la suppression a réussi
        return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('vitrine.delete_departement')
def supprimer_donnee_departement(request):
    if request.method == 'POST':
        # Récupérer l'identifiant de la donnée à supprimer depuis les données de la requête POST
        id_donnee = request.POST.get('id_departement')
        # Supprimer l'instance de l'objet
        instance = get_object_or_404(Departement, id=id_donnee)
        instance.delete()
        # Répondre avec un JSON pour indiquer que la suppression a réussi
        return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('vitrine.delete_article')
def supprimer_donnee_actualite(request):
    if request.method == 'POST':
        # Récupérer l'identifiant de la donnée à supprimer depuis les données de la requête POST
        id_donnee = request.POST.get('id_actualite')
        # Supprimer l'instance de l'objet
        instance = get_object_or_404(Article, id=id_donnee)
        instance.delete()
        # Répondre avec un JSON pour indiquer que la suppression a réussi
        return JsonResponse({'success': True})
    else:
        # Si la méthode de la requête n'est pas POST, renvoyer une erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@permission_required('auth.add_user')
def new_users(request):
    if request.user.is_authenticated and request.user.is_superuser:
        # L'utilisateur est connecté, exécutez le code pour la vue
        # par exemple, redirigez-le vers une autre page
        active_page = 'new_users'
        group = Group.objects.all()
        return render(request, "admin/new_users.html", {'active_page': active_page, 'group': group})
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return redirect(reverse('administrateur'))


@permission_required('auth.add_user')
def register_user(request):
    group = Group.objects.all()
    if request.method == 'POST':
        username = request.POST.get('pseudo')
        first_name = request.POST.get('nom')
        last_name = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confpass = request.POST.get('confpass')
        groupe = request.POST.get('group')
        nom_group = Group.objects.get(name=groupe)

        print(password + confpass)
        # Valider les données soumises
        if not (username and email and password and confpass) and password != confpass:
            # Gérer les erreurs de validation
            return render(request, 'admin/new_users.html',
                          {'error_message': 'Veuillez remplir tous les champs.', 'group': group})
        elif User.objects.filter(username=username).exists():
            # Gérer l'erreur de nom d'utilisateur déjà pris
            return render(request, 'admin/new_users.html',
                          {'error_message': 'Ce nom d\'utilisateur est déjà pris.', 'group': group})
        elif User.objects.filter(email=email).exists():
            # Gérer l'erreur d'e-mail déjà enregistré
            return render(request, 'admin/new_users.html',
                          {'error_message': 'Cet e-mail est déjà associé à un compte.', 'group': group})
        else:
            # Enregistrer l'utilisateur dans la base de données
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                            last_name=last_name)
            user.save()
            user.groups.add(nom_group)
            # Redirection vers une page de succès ou d'accueil
            return render(request, 'admin/new_users.html',
                          {'success_message': "Utilisateur ajouté avec succès", 'group': group})
    else:
        return render(request, 'admin/new_users.html', {'group': group})


@permission_required('auth.view_user')
def historique(request):
    if request.user.is_authenticated and request.user.is_superuser:
        active_page = "historique"
        users = User.objects.order_by('-last_login')[:10]
        return render(request, "admin/historique.html", {'historique': users, 'active_page': active_page})

    else:
        redirect(reverse('administrateur'))


@permission_required('vitrine.add_autre')
def autre(request):
    if request.user.is_authenticated:
        autre = Autre.objects.get(pk=1)
        active_page = "ajout_autre"
        print(autre)
        return render(request, 'admin/autre.html', {'active_page': active_page, 'autre': autre})
    else:
        redirect(reverse('administrateur'))


@permission_required('auth.change_user')
def users(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        active_page = "users"
        return render(request, "admin/users.html", {'active_page': active_page, 'users': users})
    else:
        redirect(reverse('administrateur'))


@permission_required('auth.view_group')
def groupes(request):
    if request.user.is_authenticated:
        users = User.objects.all()
        first_users = User.objects.all().first()
        groupe_users = first_users.groups.all()
        groupe = Group.objects.all()
        return render(request, "admin/groupes.html",
                      {'active_page': "groupes", 'users': users, 'groupe': groupe, 'groupe_users': groupe_users})
    else:
        return redirect(reverse('administrateur'))


@permission_required('auth.change_group')
def attribute_groupe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            users_id = request.POST.get('nomUsers')
            users = User.objects.get(pk=users_id)
            groupe_ids = request.POST.getlist('nomGroupe')
            if groupe_ids and users_id:
                groupe = Group.objects.filter(pk__in=groupe_ids)
                users.groups.add(*groupe)
                groupes = Group.objects.all()
                user = User.objects.all()
                groupes_user = users.groups.all()
                attribute_message = "Attribution éfféctué avec succès"
                return render(request, "admin/groupes.html",
                              {'users': user, 'groupe': groupes, 'attribute_message': attribute_message,
                               'default_user': users, 'groupe_users': groupes_user})
            else:
                groupes = Group.objects.all()
                user = User.objects.all()
                error_message = "Une erreur s'est produite. N'oublier pas de séléctionner au moins un groupe"
                return render(request, "admin/groupes.html",
                              {'users': user, 'groupe': groupes, 'error_message': error_message})
        else:
            redirect(reverse('groupe'))
    else:
        redirect(reverse('administrateur'))


@permission_required('auth.change_group')
def affiche_groupe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            users_id = request.POST.get('nom')
            users = User.objects.get(pk=users_id)
            groupe_users = users.groups.all()
            groupes = Group.objects.all()
            user = User.objects.all()
            return render(request, "admin/groupes.html",
                          {'users': user, 'groupe': groupes, 'groupe_users': groupe_users, 'default_user': users,
                           'active_page': "groupes"})


@permission_required('auth.delete_group')
def delete_groupe_users(request, id_group, id_users):
    utilisateurs = User.objects.get(pk=id_users)
    groupe_utilisateurs = Group.objects.get(id=id_group)
    utilisateurs.groups.remove(groupe_utilisateurs)
    users = User.objects.get(pk=id_users)
    groupe_users = users.groups.all()
    groupes = Group.objects.all()
    user = User.objects.all()
    success_message = "Suppréssion réussi avec succès"
    return render(request, "admin/groupes.html",
                  {'users': user, 'groupe': groupes, 'groupe_users': groupe_users, 'default_user': users,
                   'active_page': "groupes", 'success_message': success_message})


@permission_required('auth.change_user')
def statut(request, id):
    if request.user.is_authenticated:
        users = User.objects.get(pk=id)
        if users.is_active == True:
            users.is_active = False
            users.save()
        else:
            users.is_active = True
            users.save()
        return redirect(reverse('users'))
    else:
        return redirect(reverse('administrateur'))


@permission_required('auth.add_group')
def create_groupe(request):
    if request.user.is_authenticated:
        permission = Permission.objects.all()
        return render(request, 'admin/new_groupe.html', {'active_page': "create_groupes", 'permission': permission})
    else:
        return redirect(reverse('administrateur'))


@permission_required('auth.add_group')
def add_group(request):
    permission = Permission.objects.all()
    if request.user.is_authenticated:
        if request.method == "POST":
            nom_groupe = request.POST.get('nom')
            id_permission = request.POST.getlist('permission')
            if nom_groupe != "":
                nouveau_groupe, cree = Group.objects.get_or_create(name=nom_groupe)
                for permission in id_permission:
                    perm = Permission.objects.get(pk=permission)
                    nouveau_groupe.permissions.add(permission)
                return render(request, 'admin/new_groupe.html', {'active_page': 'create_groupes',
                                                                 'permission': Permission.objects.all(),
                                                                 'success_message': 'Nouveau groupe créé avec succès'})
            else:
                return render(request, 'admin/new_groupe.html',
                              {'active_page': 'create_groupes', 'permission': permission,
                               'error_message': 'Tous les champs sont obligatoire'})
        else:
            redirect(reverse('create_groupe'))
    else:
        redirect(reverse("administrateur"))


@permission_required('auth.edit_group')
def ens_group(request):
    if request.user.is_authenticated:
        groupes = Group.objects.all()
        return render(request, 'admin/gestion_groupe.html', {'active_page': 'edit_groupes', 'groupes': groupes})
    else:
        redirect(reverse('administrateur'))


@permission_required('auth.delete_group')
def delete_groupe(request, id):
    if request.user.is_authenticated:
        groupe = Group.objects.get(pk=id)
        groupe.delete()
        groupes = Group.objects.all()
        return render(request, 'admin/gestion_groupe.html', {'active_page': 'edit_groupes', 'groupes': groupes,
                                                             'success_message': "Suppression éfféctué avec succès"})


def dash_view(request):
    if request.user.is_authenticated:

        annee_en_cours = datetime.now().year

        # Filtrez les données par année en cours
        data_service = list(
            Service.objects.filter(date__year=annee_en_cours).values('date__month').annotate(total=Count('id')))
        data_actualite = list(
            Article.objects.filter(date__year=annee_en_cours).values('date__month').annotate(total=Count('id')))
        data_departement = list(
            Departement.objects.filter(date__year=annee_en_cours).values('date__month').annotate(total=Count('id')))
        data_prix = list(
            Prix.objects.filter(date__year=annee_en_cours).values('date__month').annotate(total=Count('id')))

        return render(request, 'admin/stat.html', {
            'data_service': data_service, 'data_actualite': data_actualite, 'data_departement': data_departement,
            'data_prix': data_prix, 'active_page': 'stat'
        })
    else:
        return redirect('/administrateur')


def graphe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            graphe = request.POST.get('graphe')
            if graphe == "parMois":
                # Obtenez l'année actuelle
                annee_en_cours = datetime.now().year

                # Filtrez les données par année en cours
                service = list(
                    Service.objects.filter(date__year=annee_en_cours).values('date__month').annotate(total=Count('id')))
                actualite = list(
                    Article.objects.filter(date__year=annee_en_cours).values('date__month').annotate(total=Count('id')))
                departement = list(Departement.objects.filter(date__year=annee_en_cours).values('date__month').annotate(
                    total=Count('id')))
                prix = list(
                    Prix.objects.filter(date__year=annee_en_cours).values('date__month').annotate(total=Count('id')))
                print(departement)
                return render(request, 'admin/stat.html', {
                    'data_service': service, 'data_actualite': actualite,
                    'data_departement': departement,
                    'data_prix': prix, 'active_page': 'stat'
                })
            elif graphe == "3mois":
                # Calculer la date d'il y a trois mois
                date_trois_mois_avant = datetime.now() - timedelta(days=90)

                # Filtrer les contenus en fonction de la date calculée
                service = Service.objects.filter(date__gte=date_trois_mois_avant)
                actualite = Article.objects.filter(date__gte=date_trois_mois_avant)
                departement = Departement.objects.filter(date__gte=date_trois_mois_avant)

                # Grouper les contenus par mois et compter le nombre de contenus pour chaque mois
                service_par_mois = service.values('date__month').annotate(total=Count('id'))
                actualite_par_mois = actualite.values('date__month').annotate(total=Count('id'))
                departement_par_mois = departement.values('date__month').annotate(total=Count('id'))

                # Retourner les données sous forme de JSON
                data_service = [{'mois': service['date__month'], 'nombre_contenus': service['total']} for service in
                                service_par_mois]
                data_actualite = [{'mois': service['date__month'], 'nombre_contenus': service['total']} for service
                                  in actualite_par_mois]
                data_departement = [{'mois': service['date__month'], 'nombre_contenus': service['total']} for
                                    service in departement_par_mois]

                print(data_service)
                print(data_actualite)
                print(data_departement)

                return render(request, 'admin/fichier_stat/3mois.html', {
                    'service': data_service, 'actualite': data_actualite, 'departement': data_departement,
                    'active_page': 'stat', 'graphe_select': '3mois'
                })
            elif graphe == "3annes":
                date_actuelle = datetime.now()
                # Calculer la date d'il y a trois ans à partir de la date actuelle
                date_trois_ans_avant = date_actuelle - timedelta(days=365 * 3)
                # Filtrer les contenus en fonction de la date calculée
                service = Service.objects.filter(date__gte=date_trois_ans_avant)
                actualite = Article.objects.filter(date__gte=date_trois_ans_avant)
                departement = Departement.objects.filter(date__gte=date_trois_ans_avant)

                # Grouper les contenus par année et compter le nombre de contenus pour chaque année
                service_par_annee = service.values('date__year').annotate(total=Count('id'))
                actualite_par_annee = actualite.values('date__year').annotate(total=Count('id'))
                departement_par_annee = departement.values('date__year').annotate(total=Count('id'))
                # Retourner les données sous forme de JSON
                data_service = [{'annee': contenu['date__year'], 'nombre_contenus': contenu['total']} for contenu in
                                service_par_annee]
                data_actualite = [{'annee': contenu['date__year'], 'nombre_contenus': contenu['total']} for contenu in
                                  actualite_par_annee]
                data_departement = [{'annee': contenu['date__year'], 'nombre_contenus': contenu['total']} for contenu in
                                    departement_par_annee]
                print(data_service)
                print(data_actualite)
                print(data_departement)
                return render(request, 'admin/fichier_stat/3ans.html', {
                    'active_page': 'stat',
                    'graphe_select': '3annes',
                    'service': data_service,
                    'actualite': data_actualite,
                    'departement': data_departement
                })
            elif graphe == "anne":
                annee_actuelle = datetime.now().year
                # Filtrer les contenus par année
                service_cette_annee = Service.objects.filter(date__year=annee_actuelle)
                departement_cette_annee = Departement.objects.filter(date__year=annee_actuelle)
                article_cette_annee = Article.objects.filter(date__year=annee_actuelle)
                # Compter le nombre total de contenus pour cette année
                nombre_service_cette_annee = service_cette_annee.count()
                nombre_departement_cette_annee = departement_cette_annee.count()
                nombre_article_cette_annee = article_cette_annee.count()
                # Rendre le template avec l'année et le nombre total de contenus
                return render(request, 'admin/fichier_stat/anne.html', {'annee_actuelle': annee_actuelle,
                                                                        'service': nombre_service_cette_annee,
                                                                        'departement': nombre_departement_cette_annee,
                                                                        'actualite': nombre_article_cette_annee,
                                                                        'active_page': 'stat',
                                                                        'graphe_select': 'anne'
                                                                        })


@permission_required("auth.change_permission")
def permission(request):
    if request.user.is_authenticated:
        permission = Permission.objects.all()
        users = User.objects.all()
        active_page = "permission"
        return render(request, 'admin/permission.html',
                      {'permissions': permission, 'active_page': active_page, 'users': users})
    else:
        return redirect('/administrateur')


@permission_required("auth.change_permission")
def attribuer_permission(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_id = request.POST.get('user')
            user = User.objects.get(pk=user_id)
            print(user)
            permissions_ids = request.POST.getlist('permission')
            permissions_existantes = user.user_permissions.all()
            nouvelles_permissions = Permission.objects.filter(id__in=permissions_ids)
            print(nouvelles_permissions)
            # Ajouter les nouvelles permissions
            for permission in nouvelles_permissions:
                # Vérifier si la permission existe déjà pour éviter les doublons
                if permission not in permissions_existantes:
                    user.user_permissions.add(permission)
            # Sauvegarder les modifications
            user.save()
            success_message = "Permission attribué avec succès"
            active_page = "permission"
            permissions = Permission.objects.all()
            users = User.objects.all()
            default_user = user
            user_permissions = user.user_permissions.all()
            return render(request, 'admin/permission.html',
                          {'active_page': active_page, 'success_message': success_message, 'users': users,
                           'permissions': permissions, 'default_user': default_user,
                           'user_permissions': user_permissions})
        else:
            return redirect('/permission')
    else:
        return redirect('/administrateur')


@permission_required('auth.view_permission')
def view_permissions(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_id = request.POST.get('user')
            user = User.objects.get(pk=user_id)
            user_permissions = user.user_permissions.all()
            print(user_permissions)
            active_page = "permission"
            permissions = Permission.objects.all()
            users = User.objects.all()
            return render(request, 'admin/permission.html', {
                'active_page': active_page,
                'users': users,
                'default_user': user,
                'user_permissions': user_permissions,
                'permissions': permissions
            })
        else:
            return redirect('/permission')
    else:
        return redirect('/administrateur')


@permission_required('auth.delete_permission')
def delete_permission(request, id_permission, id_user):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=id_user)
        permission = get_object_or_404(Permission, id=id_permission)
        user.user_permissions.remove(permission)
        user.save()
        users = User.objects.all()
        permissions = Permission.objects.all()
        active_page = "permission"
        error_message = "Suprréssion éfféctué avec succès"
        user_permissions = user.user_permissions.all()
        return render(request, 'admin/permission.html', {
            'active_page': active_page, 'default_user': user, 'users': users, 'permissions': permissions,
            'error_message': error_message, 'user_permissions': user_permissions
        })
    else:
        return redirect('/administrateur')


def ajout_agence(request):
    if request.user.is_authenticated:
        return render(request, "admin/ajout_agence.html", {'active_page': 'ajout_agence'})
    else:
        return redirect('/administrateur')


@permission_required('vitrine.add_agence')
def add_agence(request):
    if request.user.is_authenticated:
        active_page = "ajout_agence"
        success_message = "Agence ajouté avec succès"
        if request.method == "POST":
            nom = request.POST.get('nom')
            rue = request.POST.get('rue')
            telephone = request.POST.get('telephone')
            photo = request.FILES.get('photo')
            if photo and nom != "" and rue != "" and telephone != "":
                Agence.objects.create(nom=nom, rue=rue, telephone=telephone, photo=photo)
                return render(request, "admin/ajout_agence.html", {
                    'active_page': active_page,
                    'success_message': success_message,
                })
            else:
                return render(request, 'admin/ajout_agence.html', {
                    'active_page': active_page,
                    'error_message': "Veillez remplir tous les champs"
                })

        else:
            return redirect('/ajout_agence')
    else:
        return redirect('/administrateur')


@permission_required('vitrine.edit_autre')
def titre(request):
    if request.user.is_authenticated and request.method == "POST":
        grand_titre = request.POST.get('grand_titre')
        petit_titre = request.POST.get('petit_titre')

        if grand_titre:
            instance = Autre.objects.get(pk=1)
            instance.grand_titre = grand_titre
            instance.save()
            autre = Autre.objects.get(pk=1)
            attribute_message = "Modification éfféctué avec succès"
            return render(request, 'admin/autre.html', {'active_page': 'ajout_autre', 'autre': autre, 'attribute_message': attribute_message})

        if petit_titre:
            instance = Autre.objects.get(pk=1)
            instance.petit_titre = petit_titre
            instance.save()
            autre = Autre.objects.get(pk=1)
            attribute_message = "Modification éfféctué avec succès"
            return render(request, 'admin/autre.html', {'active_page': 'ajout_autre', 'autre': autre, 'attribute_message': attribute_message})


@permission_required('vitrine.view_equipe')
def equipe(request):
    if request.user.is_authenticated:
        return render(request, 'admin/equipe.html', {'active_page': 'equipe'})
    else:
        return redirect('/administrateur')


@permission_required('vitrine.add_equipe')
def add_equipe(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            photo = request.FILES.get('photo')
            if photo:
                equipe = Equipe.objects.create(photo=photo)
                equipe.save()
                success_message = "Photo de l'équipe ajouté avec succès"
                return render(request, 'admin/equipe.html', {'active_page': 'equipe', 'success_message': success_message})
            else:
                error_message = "L'image est obligaoire"
                return render(request, 'admin/equipe.html', {'error_message': error_message, 'active_page': 'equipe'})

        else:
            return redirect('equipe')
    return redirect('/administrateur')









