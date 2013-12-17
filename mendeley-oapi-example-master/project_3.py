from pprint import pprint
from mendeley_client import *
import operator
import numpy as np
from matplotlib import pyplot as p
from datetime import datetime
import json


def save_as_pickle(p_object, filename):
    with open("%s.pk" % filename, "wb") as p_output:
        pickle.dump(p_object, p_output, pickle.HIGHEST_PROTOCOL)


def open_from_pickle(filename):
    with open("%s.pk" % filename, "rb") as p_input:
        r_object = pickle.load(p_input)
    return r_object

# Draws a barchart with the matplotlib-library using the given values.
def draw_barchart(names, values, ylabel, title):
    ind=range(len(values))
    fig = p.figure()
    ax = fig.add_subplot(1,1,1)
    ax.bar(ind, values)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(ind)
    ax.set_xticklabels(names)
    fig.autofmt_xdate()
    p.show()

# Draws a piechart with the matplotlib-library using the given values.
def draw_piechart(names, values):
    t= 0
    sizes=[]
    # Convert the given values to percentages/100
    for element in values:
        t = t+element
    for element in values:
        x = (float(element)/t)*100
        sizes.append(x)
    p.pie(sizes, labels=names, autopct='%1.1f%%', startangle=90)
    p.axis('equal')
    p.show()

# Draws a timeline with the matplotlib-library using the given values and dates.
def draw_timeline(names, values, ylabel, title):
    p.plot_date(x=names, y=values, fmt="-")
    p.ylabel(ylabel)
    p.title(title)
    p.ylim(ymin=0)
    p.grid=True
    p.show()

if __name__ == "__main__":


    # ### Collect the required data ###

    mendeley = create_client()
    # categories = mendeley.categories()

    # Export all categories for later usage
    # with open("categories.json", "wb") as json_output:
    #     json.dump(categories, json_output, indent=4)

    # Overall publications publications of all time
    # overall_pub = {}
    # for i in range(2003, 2013):
    #     overall_pub[i]=mendeley.search("year:%s"%i)["total_results"]
    # save_as_pickle(overall_pub, "overall_pub")

    # # Top 20 Tags from Computer and Information Science (cat 6)
    # top20tags = mendeley.tag_stats(6)
    # save_as_pickle(top20tags, "top20tags")

    # All publications by the author Wolfgang G Stock
    # pub_stock = mendeley.search("author:\"Wolfgang G Stock\"", items=500)
    # save_as_pickle(pub_stock, "pub_stock")

    # Top 10 publications published in "Nature"
    # search_nature = mendeley.search("published_in:\"Nature\"", items=10)
    # top10_nature = {}
    # for elem in search_nature["documents"]:
    #     top10_nature[elem["title"]] = mendeley.details(elem["uuid"])\
    #                                    ["stats"]["readers"]
    # save_as_pickle(top10_nature, "top10_nature")

    # All Publications with the tag "ontology"
    # onto_tagged = {}
    # for category in categories:
    #     cat_id = category["id"]
    #     onto_tagged[cat_id] = 0
    #     # If the item value is too high (not max 500 as with .search)
    #     # no documents are returned
    #     # (maybe the item value must be less than the number of results)
    #     page_count = mendeley.tagged("ontology", cat=cat_id, items=100)\
    #                  ["total_pages"]
    #     for page_num in range(1, page_count+1):
    #         tagged = mendeley.tagged("ontology", cat=cat_id, items=100,
    #                                  page=page_num)
    #         for document in tagged["documents"]:
    #             if document["year"]==2011:
    #                 onto_tagged[cat_id] += 1
    # save_as_pickle(onto_tagged, "onto_tagged")


    # ### Plotting ###

    # Reads the file with the extracted tags and makes two ordered lists (tags and frequency) out of it. Then visualizes the results with a barchart.
    """
    # Top20 Tags
    tags = open_from_pickle("top20tags")
    tags_value = []
    tags_name = []
    # Split the tag/frequency pairs in two lists
    for element in tags:
        tags_value.append(element["count"])
        tags_name.append(element["name"].encode("utf-8"))
    draw_barchart(tags_name, tags_value, "Haeufigkeit des vergebenen Tags", "Top20 Tags der Kategorie 'Computer and Informationscience'")
    """

    # Draws a piechart giving the percentage distribution of the overall publications of the last 10 years.

    # Overall Publications
    # publications = open_from_pickle("overall_pub")
    # pub_years = {}
    # pub_syears = []
    # pub_scount = []
    # # Check if the publication year is in the last 10 years. If yes, add it to the dictionary or increase its frequency
    # for element in publications:
    #     if element["year"] >=2003:
    #         if element["year"] in pub_years:
    #             pub_years[element["year"]] += 1
    #         else:
    #             pub_years[element["year"]] = 1
    # # Make a list of tuples sorted by the frequency ot of the dictionary
    # sorted_years = sorted(pub_years.iteritems(), key=operator.itemgetter(0))
    # for element in sorted_years:
    #     pub_syears.append(element[0])
    #     pub_scount.append(element[1])
    # draw_piechart(pub_syears, pub_scount)


    # Draws a timeline for the publications of "Wolfgang G. Stock".
    """
    # Stock Publications/Year
    publications = open_from_pickle("pub_stock")
    pub_years = []
    pub_dic = {}
    all_years = []
    pub_syears = []
    pub_scount = []
    # Get all of the years, an article was published and sort them.
    for element in publications["documents"]:
        pub_years.append(element["year"])
    pub_years=sorted(pub_years)
    # Make a List with all years in his publication-time.
    for i in range(pub_years[0], pub_years[-1]):
        all_years.append(i)
    # Check if he published something in a year and cycle the publications. If yes, add it to the dictionary or increase the frequency, else add with 0 frequency to the dictionary
    for year in all_years:
        if year in pub_years:
            for element in publications["documents"]:
                if year==element["year"]:
                    if element["year"] in pub_dic:
                        pub_dic[element["year"]] += 1
                    else:
                        pub_dic[element["year"]] = 1
        else:
            pub_dic[year] = 0
    # Sort by year, not by frequency this time
    sorted_years = sorted(pub_dic.iteritems(), key=operator.itemgetter(0))
    for element in sorted_years:
        # Convert the integer years to the datetime-format, so we can use the dateplot-function of matplotlib
        pub_syears.append(datetime.strptime(str(element[0]) , '%Y'))
        pub_scount.append(element[1])
    draw_timeline(pub_syears, pub_scount, "Anzahl der Publikationen", "Anzahl der Publikationen/Jahr von Wolfgang G. Stock")
    """

    # Draws a barchart of all of the authors, who co-authored Wolfgang G. Stock and sorts them by the number of co-published papers
    """
    # Stock Co-Authors
    # Save the data for all publications of Stock in a list
    publications = open_from_pickle("pub_stock")["documents"]
    authors = {}
    authors_value = []
    authors_name = []
    # For each article: get all of the names of the authors and if it is not "Wolfgang G. Stock" then save them with their frequency of co-authorhood in a dictionary.
    for article in publications:
        for author in article["authors"]:
            if (author["surname"] != "Stock" and author["forename"] != "Wolfgang G.") and (author["surname"] != "G. Stock" and author["forename"] != "Wolfgang"):
                name = author["forename"]+" "+author["surname"]
                if name in authors:
                    authors[name] += 1
                else:
                    authors[name] = 1
    sorted_authors = sorted(authors.iteritems(), key=operator.itemgetter(1), reverse = True)
    for element in sorted_authors:
        authors_name.append(element[0])
        authors_value.append(element[1])
    draw_barchart(authors_name, authors_value, "Anzahl gem. publizierter Artikel", "Co-Autoren von Wolfgang G. Stock")
    """

    # Draws a piechart given the frequencys a category on mendeley was tagged with "ontology".

    # # Ontology
    # ontology = open_from_pickle("onto_tagged")
    # categories = []
    # values = []
    # for element in ontology:
    #     categories.append(element)
    #     values.append(ontology[element])
    # draw_barchart(categories, values, "Haeufigkeit der Vergabe", "Mit 'ontology' getaggte Kategorien")

    # Draws a barchart for the ranked top 10 publications of the journal "Nature and Science"
    # Top 10 Nature and Science
    ns = open_from_pickle("top10_nature")
    articles = []
    readers = []
    for element in ns:
        articles.append(element)
        readers.append(ns[element])
    draw_barchart(articles, readers, "Leser", "Top 10 populaerste Publikationen in 'Nature and Science'")
