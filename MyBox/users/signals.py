from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Sinal para criar automaticamente um perfil associado ao usuário
    quando um novo usuário é criado.
    """
    if created:
        if not hasattr(instance, 'profile'):  # Cria apenas se o perfil não existir
            Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Sinal para salvar automaticamente o perfil associado
    quando o usuário é salvo.
    """
    if hasattr(instance, 'profile'):  # Salva o perfil apenas se ele existir
        instance.profile.save()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Sinal para criar automaticamente um perfil associado ao usuário
    quando um novo usuário é criado.
    """
    if created:
        if not hasattr(instance, 'profile'):  # Cria apenas se o perfil não existir
            Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Sinal para salvar automaticamente o perfil associado
    quando o usuário é salvo.
    """
    if hasattr(instance, 'profile'):  # Salva o perfil apenas se ele existir
        instance.profile.save()

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Profile


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created and not hasattr(instance, 'profile'):  # Only create if no profile exists
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     if hasattr(instance, 'profile'):  # Save profile only if it exists
#         instance.profile.save()
# # @receiver(post_save, sender=User)
# # def create_profile(sender, instance, created, **kwargs):
# #     if created:  # Para novos usuários
# #         Profile.objects.create(user=instance)
# #     else:  # Para usuários existentes sem Profile
# #         if not hasattr(instance, 'profile'):
# #             Profile.objects.create(user=instance)

# # @receiver(post_save, sender=User)
# # def save_profile(sender, instance, **kwargs):
# #     instance.profile.save()
