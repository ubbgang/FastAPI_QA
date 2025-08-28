# -*- coding: utf8 -*-
import logging as file_logging
from logging.handlers import RotatingFileHandler
import os

from utils.helpers import get_now

class Logging:
    additional_info:str
    
    class Color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    
    def __init__(self, *args) -> None:
        self.additional_info = "".join(
                [f" | {item}" for item in args]) if len(args) else ""

    def log_error(self,text:str):
        now = get_now().strftime('%d.%m.%Y, %H:%M:%S')
        print(
            f"{self.Color.RED}{now}{self.additional_info} | ERROR: {text}{self.Color.END}")
        file_logging.error(f"{self.additional_info} | ERROR: {text}")
        
    def log_success(self,text:str):
        now = get_now().strftime('%d.%m.%Y, %H:%M:%S')
        print(
            f"{self.Color.GREEN}{now}{self.additional_info} | SUCCESS: {text}{self.Color.END}")
        file_logging.info(f"{self.additional_info} | SUCCESS: {text}")

    def log_attention(self,text:str):
        now = get_now().strftime('%d.%m.%Y, %H:%M:%S')
        print(
            f"{self.Color.YELLOW}{now}{self.additional_info} | ATTENTION: {text}{self.Color.END}")
        file_logging.warning(f"{self.additional_info} | ATTENTION: {text}")

    def log_function_execution(self,text:str):
        now = get_now().strftime('%d.%m.%Y, %H:%M:%S')
        print(
            f"{self.Color.DARKCYAN}{now}{self.additional_info} | FUNCTION: {text}{self.Color.END}")
        file_logging.info(f"{self.additional_info} | FUNCTION: {text}")
        
    @staticmethod
    def setup_root_logger(folder_path:str,file_path:str):
        if not (os.path.exists(folder_path)):
            os.makedirs(folder_path, exist_ok=True)
        handler = RotatingFileHandler(
            file_path,      # Имя файла логов
            maxBytes=5*1024*1024, # Максимальный размер файла (5 МБ)
            backupCount=5        # Количество резервных копий
        )
        file_logging.basicConfig(encoding='utf-8', level=file_logging.INFO, format="%(asctime)s%(message)s", datefmt="%d.%m.%Y, %H:%M:%S",handlers=[handler])

        
