import sys
import csv

__author__ = '5Fingers'
__license__ = 'GPLv3'
__version__ = "1.0.0"

class CSVConverter:
    """This class convert a CSV file with comma separator into XML file"""

    def __init__(self, sys_args):
        self.csvFileName = sys_args[1]
        self.xmlFileName = sys_args[2]

    def convert_file(self):
        try:
            csv_content = csv.reader(open(self.csvFileName))
            with open(self.xmlFileName, 'w') as xml_content:
                xml_content.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n')
                # Create the root tag
                xml_content.write('<CsvData>\n')

                first_row = 0
                for row in csv_content:
                    if first_row == 0:
                        tags = row
                        # replace spaces with underscores in tag names
                        for i in range(len(tags)):
                            tags[i] = tags[i].replace(' ', '_')
                    else:
                        xml_content.write('<RowTag>' + '\n')
                        for i in range(len(tags)):
                            xml_content.write('    <{0}>{1}</{2}>\n'.format(tags[i], row[i], tags[i]))
                        xml_content.write('</RowTag>\n')

                    first_row += 1

                xml_content.write('</CsvData>\n')
            print('The csv file was successfully converted! :) ')
        except Exception as e:
            sys.stderr.write(u'{0:s} {1:s}\n'.format('PythonCall#execute', e))


if __name__ == "__main__":
    CSVConverter(sys.argv).convert_file()