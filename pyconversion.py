import json, csv

class Convert(object):
    @staticmethod
    def csv_to_json(csv_file, json_file):
        """ Converts CSV file to JSON.
            CSV needs headers, for now. """
        try:
            f = open(csv_file, 'r')
            r = csv.DictReader(f)
            out = json.dumps( [row for row in r] )
            with open(json_file, 'w') as j:
                j.write(out)
            return json_file
        except Exception, e:
            print "Error converting CSV to JSON: {}".format(e)
            return None
