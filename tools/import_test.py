import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

try:
    import home.templatetags.custom_filters as cf
    print('import ok, attrs:', [a for a in dir(cf) if not a.startswith('__')])
except Exception as e:
    print('import failed:', e)
