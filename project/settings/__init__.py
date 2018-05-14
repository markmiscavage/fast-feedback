import os.path
import sys

from base import *

# Load settings overides
_path = os.path.join(PROJECT_ROOT, 'settings', 'hosts')
sys.path.insert(0, _path)

from socket import gethostname
_hostname = gethostname().split('.')[0]

ENV_VAR = 'SBK_FEEDBACK_OVERRIDE'

if os.environ.get(ENV_VAR):
    sys.modules['host'] = __import__(os.environ.get(ENV_VAR))
    from host import *
    del sys.modules['host']
elif os.path.isfile(os.path.join(_path,'local_settings.py')):
    from local_settings import *
elif os.path.isfile(os.path.join(_path, '%s.py' % _hostname)):
    sys.modules['host'] = __import__(_hostname)
    from host import *
    del sys.modules['host']

sys.path.remove(_path)
