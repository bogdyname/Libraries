import sys
from datetime import datetime

def check_emptiness(args=[]) -> bool:
    """
    Function to check list of args for null and data type.
    
    Parameters
    ----------
    args : list
        List of args to check
        
    Returns
    -------
    true on success otherwise false
    
    Raises
    ------
    ValueError
        If args is empty.
        If any item in args is empty.
        If any item in args is not a string.
    """
    if not args:
        raise ValueError('args list is empty')
    
    #check data type
    if any(not isinstance(item, str) for item in args):
        raise ValueError('some value is not a string')
    #check data in args
    if any(not item for item in args):
        raise ValueError('some value is empty')
    
    return True
        
def create_insert_command(table: str, field: dict, filename='insert') -> str:
    """
     Function to check list of args for null and data type.
    
    Parameters
    ----------
    filename : str, optional
        File name there to save created sql command to isert.
    table : str
        Table name there need to isert new data.
    
    field : dict
        (key-str, value-list)
        
    Returns
    -------
    Full path for the generated file    
        
    Raises
    ------
    
    """
    #add current date and time to output file
    current_dt = datetime.now().strftime("%d%m%Y_%H%M%S")
    filename += '_' + current_dt + '.sql'
    
    args = [table, field]
    check_emptiness(args)
    
def read_column_csv(filename='', column=''):
    pass
    
if __name__ == "__main__":
    filename = ''
    if len (sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print('Error: add path to filename!')
        quit()