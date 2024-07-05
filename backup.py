import os
import subprocess
import datetime
import logging


logging.basicConfig(filename='/backup/backup.log', level=logging.INFO, format='%(asctime)s %(message)s')


def backup(source, destination):
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    dest_path = os.path.join(destination, f'backup_{timestamp}')
    
    try:
        
        os.makedirs(dest_path)
        
        
        subprocess.run(['rsync', '-avz', source, dest_path], check=True)
        
        logging.info(f'Successfully backed up {source} to {dest_path}')
    except Exception as e:
        logging.error(f'Failed to backup {source} to {dest_path}: {str(e)}')

if __name__ == "__main__":
    
    source_dir = "/path/to/source"
    destination_dir = "/backup"

    
    backup(source_dir, destination_dir)

