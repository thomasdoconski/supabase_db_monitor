import os
import pickle
import logging

def load_from_pickle(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            logging.error(f"Erro ao carregar o arquivo pickle: {e}")
    return None

def save_to_pickle(file_path, data):
    try:
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
    except Exception as e:
        logging.error(f"Erro ao salvar o arquivo pickle: {e}")
