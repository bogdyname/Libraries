import csv
from datetime import datetime     
        
def create_insert_command(table: str, field: dict, csv_field: list, input_filename: str, output_filename: str) -> str:
    """
     Function to check list of args for null and data type.
    
    Parameters
    ----------
    table : str
        Table name there need to isert new data.
    field : dict
        Fields names in table. Key is name, value is type.
    csv_field : list
        List of columns names in loaded csv file for keys in field dict.
    input_filename : str
        Csv filename for parsing.
    output_filename : str
        Name for output sql file.
        
    Returns
    -------
    Full path for the generated file    
        
    Raises
    ------
    
    """
    #add current date and time to output file
    current_dt = datetime.now().strftime("%d%m%Y_%H%M%S")
    output_filename += '_' + current_dt + '.sql'
    
    print('Output: ', output_filename)
    print('Input: ', input_filename)
    
    #format for isert command
    #INSERT INTO table_name (column1, column2, column3, ...)
    #VALUES (value1, value2, value3, ...), (value1, value2, value3, ...), etc;
    
    # reading CSV file
    if input_filename:
        # open the file in read mode
        filename = open(input_filename, 'r')
        # creating dictreader object
        file = csv.DictReader(filename)

        number_from = []
        number_to = []
        owner = []
        mnc = []
        region = []
        tp = []
        
        for col in file:
            number_from.append(col['NumberFrom'])
            number_to.append(col['NumberTo'])
            owner.append(col['OwnerId'])
            mnc.append(col['MNC'])
            region.append(col['RegionCode'])
            tp.append(1)
            
        insert_com = 'INSERT INTO 7_zone (number_from, number_to, operator, mnc, region, type) \n VALUES \n'
        
        for n_from, n_to, own, m, reg, t in zip(number_from, number_to, owner, mnc, region, tp):
            insert_com += '(' + n_from + '",' + '"' + n_to + '",' + '"' + own + '",' + str(m) + ',' + str(reg) + ',' + str(t) + ',' + '),\n'
 
        text_file = open(output_filename, "w")
        text_file.write(insert_com)
        text_file.close()
    
if __name__ == "__main__":
    
    table = '7_zone'
    field = {'number_from': 'VARCHAR', 'number_to': 'VARCHAR', 'operator': 'VARCHAR', 'mnc': 'INT', 'region': 'INT', 'type': 'TINYINT'}
    csv_field = ['NumberFrom', 'NumberTo', 'OwnerId', 'MNC', 'RegionCode', 'type']
    input_filename = r'C:\\Users\\bogdy\\Downloads\\formated\\Numbering_plan_202307180000_3528.csv'
    output_filename = r'C:\\Users\\bogdy\\Downloads\\formated\\7_zone.sql'

    create_insert_command(table, field, csv_field, input_filename, output_filename)