from ..utils.database import Session, engine
from .user_matrix_model import MatrixDao


class MatrixService():
    def add_matrix( user_id, matrix_data):
       return MatrixDao.add_matrix( user_id, matrix_data)

    def get_all_matrix( user_id):
       return MatrixDao.get_all_matrix( user_id)