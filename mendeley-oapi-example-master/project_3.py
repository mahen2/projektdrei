from pprint import pprint
from mendeley_client import *



def save_as_pickle(p_object, filename):
    with open("%s.pk" % filename, "w") as p_output:
        pickle.dump(p_object, p_output, pickle.HIGHEST_PROTOCOL)


def open_from_pickle(filename):
    with open("%s.pk" % filename, "r") as p_input:
        r_object = pickle.load(p_input)
    return r_object


if __name__ == "__main__":

    # Collect the required data
    mendeley = create_client()

    # # Top 20 Tags from Computer and Information Science (cat 6)
    # top20tags = mendeley.tag_stats(6)
    # # All publications by the author Wolfgang G Stock (exact match)
    # pub_stock = mendeley.authored('\"Wolfgang G Stock\"', items=100)
    # All Publications with the tag "ontology"
    # onto_tagged = mendeley.tagged("ontology", items=200)
    
    # save_as_pickle(top20tags, "top20tags")
    # save_as_pickle(pub_stock, "pub_stock")
    # save_as_pickle(onto_tagged, "onto_tagged")
    
    print open_from_pickle("top20tags")
    # open_from_pickle("pub_stock")
