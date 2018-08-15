import os,sys
virtenv = os.path.expanduser('~') + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
   if sys.version.split(' ')[0].split('.')[0] == '3':
       exec(compile(open(virtualenv, "rb").read(), virtualenv, 'exec'), dict(__file__=virtualenv))
   else:
       execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
   pass

sys.path.append(os.path.expanduser('~'))
sys.path.append(os.path.expanduser('~') + '/ROOT/')
sys.path.append(os.path.expanduser('~') + '/ROOT/ROOT/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'ROOT.ROOT.settings'

from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

application = get_wsgi_application()
