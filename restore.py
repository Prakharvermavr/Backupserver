import os
import subprocess
import logging


logging.basicConfig(filename='/backup/restore.log', level=logging.INFO, format='%(asctime)s %(message)s')


def restore(backup_dir, restore_dir):
    try:
        
        subprocess.run(['rsync', '-avz', backup_dir, restore_dir], check=True)
        
        logging.info(f'Successfully restored {backup_dir} to {restore_dir}')
    except Exception as e:
        logging.error(f'Failed to restore {backup_dir} to {restore_dir}: {str(e)}')

if __name__ == "__main__":
    
    backup_dir = "/path/to/backup_dir"
    restore_dir = "/path/to/restore_dir"

    
    restore(backup_dir, restore_dir)

