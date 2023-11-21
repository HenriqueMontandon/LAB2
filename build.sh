set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate

cat <<EOF | python manage.py shell
import os
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

if not User.objects.filter(username=os.environ["DJANGO_SUPERUSER_USERNAME"]).exists():
    User.objects.create_superuser(os.environ["DJANGO_SUPERUSER_USERNAME"], os.environ["DJANGO_SUPERUSER_EMAIL"], os.environ["DJANGO_SUPERUSER_PASSWORD"])

basic_users_group, _ = Group.objects.get_or_create(name="Basic users")

permissions = ["add_user", "view_user", "add_list", "view_list", "add_comentario", "view_investment"]
permissions_objs = [Permission.objects.get(codename=c) for c in permissions]

for perm in permissions_objs:
    basic_users_group.permissions.add(perm)

basic_users_group.save()
EOF