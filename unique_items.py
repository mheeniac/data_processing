import csv
import operator

class UniqueItems():
    def __init__(self, filename, key):
        self.filename = filename
        self.key = key

    def unique_items(self):
        with open(self.filename, 'rb') as file:
            reader = csv.reader(file, dialect='excel')
            row_names = next(reader)  # gets the first line
            country_names = []
            index = row_names.index(self.key)
            for rows in reader:
                if rows[index] not in country_names:
                    country_names.append(rows[index])
        return country_names, index

    def unique_count(self):
        country_names = self.unique_items()[0]
        index = self.unique_items()[1]
        dict = {}
        for items in country_names:
            dict[items] = 0

        with open(self.filename, 'rb') as file:
            reader = csv.reader(file, dialect='excel')
            for rows in reader:
                if rows[index] in country_names:
                    var_name = rows[index]
                    dict[var_name] = dict[var_name] + 1


        dict_perc = {}
        for key,value in dict.iteritems():
            sub_dict = {}
            perc = float(value)/float(sum(dict.values()))*100
            sub_dict["Percentage"] = round(perc,1)
            sub_dict["Occurrence"] = value
            dict_perc[key] = sub_dict

        sorted_dict = sorted(dict_perc.items(), key=operator.itemgetter(1),reverse=True)
        return sorted_dict


countries = UniqueItems("customers.csv","country")
states = UniqueItems("customers.csv", "state")
cities = UniqueItems("customers.csv", "city")

for items in countries.unique_count():
    print items


