from pprint import pprint
from mendeley_client import *
import operator
import numpy as np
from matplotlib import pyplot as p
from datetime import datetime



def save_as_pickle(p_object, filename):
    with open("%s.pk" % filename, "wb") as p_output:
        pickle.dump(p_object, p_output, pickle.HIGHEST_PROTOCOL)


def open_from_pickle(filename):
    with open("%s.pk" % filename, "rb") as p_input:
        r_object = pickle.load(p_input)
    return r_object


if __name__ == "__main__":

    # Collect the required data
    # mendeley = create_client()
    # categories = mendeley.categories()
    
    # Overall publications publications of all time
    # overall_pub = mendeley.paper_stats()
    
    # # Top 20 Tags from Computer and Information Science (cat 6)
    # top20tags = mendeley.tag_stats(6)
    
    # # All publications by the author Wolfgang G Stock
    # pub_stock = []
    # page_count = mendeley.authored('Wolfgang G. Stock', items=500)["total_pages"]
    # for page_num in range(1, page_count):
    #     pub_stock.append(mendeley.authored('Wolfgang G. Stock', items=500, page=page_num))
    # TODO: only exact match
    
    # All Publications with the tag "ontology"
    # onto_tagged = []
    # for category in categories:
    #     page_count = mendeley.tagged("ontology", cat=category["id"],items=500)["total_pages"]
    #     for page_num in range(1, page_count):
    #         tags = mendeley.tagged("ontology", cat=category["id"], items=500, page_count)
    #         onto_tagged.append(tags)
    
	# Plotting
	
	# Top20 Tags
	# tags = open_from_pickle("top20tags")
	# tags_value = []
	# tags_name = []
	# for element in tags:
	# 	tags_value.append(element["count"])
	# 	tags_name.append(element["name"].encode("utf-8"))
	# ind=range(len(tags_value))
	# fig = p.figure()
	# ax = fig.add_subplot(1,1,1)
	# ax.bar(ind, tags_value, align='center')
	# ax.set_ylabel('Anzahl')
	# ax.set_title("Top20 Tags der Kategorie 'Computer and Informationscience'")
	# ax.set_xticks(ind)
	# ax.set_xticklabels(tags_name)
	# fig.autofmt_xdate()
	# p.show()
	
	"""
	# Overall Publications
	publications = open_from_pickle("overall_pub")
	pub_years = {}
	pub_syears = []
	pub_scount = []
	for element in publications:
		if element["year"] in pub_years:
			pub_years[element["year"]] += 1
		else:
			pub_years[element["year"]] = 1
	sorted_years = sorted(pub_years.iteritems(), key=operator.itemgetter(0))
	for element in sorted_years:
		pub_syears.append(datetime.strptime(str(element[0]) , '%Y'))
		pub_scount.append(element[1])
	p.plot_date(x=pub_syears, y=pub_scount, fmt="r-")
	p.ylabel("Publications")
	p.title("Overall number of Publications/year")
	p.grid=True
	p.show()
	# TODO: y-Achse auf 0 setzen und mehr Werte
	"""
	
    # Save the collected data in pickle files
    # save_as_pickle(overall_pub, "overall_pub")
    # save_as_pickle(top20tags, "top20tags")
    # save_as_pickle(pub_stock, "pub_stock")
    # save_as_pickle(onto_tagged, "onto_tagged")
    

    # Read the pickle files
    # pprint(open_from_pickle("overall_pub"))
    # print open_from_pickle("top20tags")
    # print open_from_pickle("pub_stock")
    # onto = open_from_pickle("onto_tagged")
