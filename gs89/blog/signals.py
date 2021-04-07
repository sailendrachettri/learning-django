from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_delete, post_init, post_save, pre_migrate, post_migrate
from django.core.signals import request_finished, request_started, got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('------------------------------------------')
    print('Logged-in Signal......Run Intro')
    print('Sender: ', sender)
    print('Request: ', request)
    print('User: ', user)
    print('User Password: ', user.password)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print('------------------------------------------')
    print('Logged-out Signal......Run Outro.....')
    print('Sender: ', sender)
    print('Request: ', request)
    print('User: ', user)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# user_logged_out.connect(log_out, sender=User)

@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print('------------------------------------------')
    print('Login-failed Signal......Run Failed.....')
    print('Sender: ', sender)
    print('Request: ', request)
    print('Credentials: ', credentials)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# user_logged_failed.connect(login_failed, sender=User)


#------------------------------------------------------------------------------------------
@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print('------------------------------------------')
    print('Pre save Signal....')
    print('Sender: ', sender)
    print('Instance: ', instance)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# pre_save.connect(at_beginning_save, sender=User)

@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print('------------------------------------------')
        print('Post save Signal.... New Record created')
        print('Sender: ', sender)
        print('Created: ', created)
        print('Instance: ', instance)
        print(f'Kwargs: {kwargs}')
        print('------------------------------------------')
    else:
        print('------------------------------------------')
        print('Post save Signal.... Update Old Record')
        print('Sender: ', sender)
        print('Instance: ', instance)
        print('Created: ', created)
        print(f'Kwargs: {kwargs}')
        print('------------------------------------------')
# post_save.connect(at_ending_save, sender=User)
    

@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print('------------------------------------------')
    print('Pre Delete Signal....')
    print('Sender: ', sender)
    print('Instance: ', instance)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# pre_delete.connect(at_beginning_delete, sender=User)

@receiver(post_delete, sender=User)
def at_ending_delete(sender, *args, **kwargs):
    print('------------------------------------------')
    print('Post Delete Signal....')
    print('Sender: ', sender)
    print(f'Args: ', {args})
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# post_delete.connect(at_Ending_delete, sender=User)

@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print('------------------------------------------')
    print('Pre Init Signal....')
    print('Sender: ', sender)
    print(f'Args:  {args}')
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# pre_init.connect(at_beginning_init, sender=User)

@receiver(post_init, sender=User)
def at_ending_init(sender, instance, **kwargs):
    print('------------------------------------------')
    print('Post Init Signal....')
    print('Sender: ', sender)
    print('Instance: ', instance)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# post_init.connect(at_Ending_init, sender=User)

#------------------------------------------------------------------------------------------
@receiver(request_started)
def at_begining_request(sender, environ, **kwargs):
    print('------------------------------------------')
    print('At Begining Request....')
    print('Sender: ', sender)
    print('Environ: ', environ)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# request_started.connect(at_begininging_request)

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print('------------------------------------------')
    print('At ending Request....')
    print('Sender: ', sender)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# request_finished.connect(at_ending_request)

@receiver(got_request_exception)
def at_ending_request(sender, request, **kwargs):
    print('------------------------------------------')
    print('At Request Exception....')
    print('Sender: ', sender)
    print('Request: ', request)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# got_request_exception.connect(at_request_exception)



@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('------------------------------------------')
    print('befor_install_app....')
    print('Sender: ', sender)
    print('App_config: ', app_config)
    print('Verbosity: ', verbosity)
    print('Interactive: ', interactive)
    print('Using: ', using)
    print('Plan: ', plan)
    print('Apps: ', apps)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# pre_migrate.connect(before_install_app)


@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('------------------------------------------')
    print('befor_install_app....')
    print('Sender: ', sender)
    print('App_config: ', app_config)
    print('Verbosity: ', verbosity)
    print('Interactive: ', interactive)
    print('Using: ', using)
    print('Plan: ', plan)
    print('Apps: ', apps)
    print(f'Kwargs: {kwargs}')
    print('------------------------------------------')
# post_migrate.connect(at_end_migrate_flush)


@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print('------------------------------------------')
    print("Initial connection to the database.....")
    print("Sender: ", sender)
    print("Connection: ", connection)
    print(f"Kwargs: {kwargs}")
    print('------------------------------------------')
    # connection_created.connect(conn_db)