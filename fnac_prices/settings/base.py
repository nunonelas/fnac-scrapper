# Author
__author__ = "Nuno Nelas"
__license__ = "GPL"
__version__ = "1.1.3"
__maintainer__ = "Nuno Nelas"
__email__ = "nuno.nelas(at)icloud(dot)com"
__status__ = "Production"

# Versions
BASE_VERSION = __version__
BASE_CODENAME = "beta"

# FNAC Settings
STORE = "skyhe"
MAX_OFFER = 100000000.0
PRODUCTS = 10   # how many products does a page have?
DECREASE_BY = 0.01

# URLs
HOMEPAGE = "https://www.fnac.pt/"
LOGIN_URL = "https://secure.fnac.pt/identity/gateway/signin"
INVENTORY_URL = "https://mp.fnac.pt/compte/vendeur/inventaire/num_desc/{id}/{num}/1"

# Files
DEFAULT_ENCODING = "utf-8"