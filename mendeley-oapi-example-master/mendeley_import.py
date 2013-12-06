from pprint import pprint
from mendeley_client import *


if __name__ == "__main__":
    # Collect the required data
    mendeley = create_client()
    # Top 20 Tags from Computer and Information Science (cat 6)
    top20tags = mendeley.tagged('test',items=20, cat=6)
    # All publications by the author Wolfgang G Stock (exact match)
    pub_stock = mendeley.authored('\"Wolfgang G Stock\"', items=100)
