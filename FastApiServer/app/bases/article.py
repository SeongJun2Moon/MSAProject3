from abc import abstractmethod, ABCMeta
from typing import List
from app.models.article import Article
from app.schemas.article import ArticleDTO


class ArticleBase(metaclass=ABCMeta):

    @abstractmethod
    def add_user(self, request_user: ArticleDTO) -> str: pass

    @abstractmethod
    def login(self, request_user: ArticleDTO) -> Article: pass

    @abstractmethod
    def update_user(self, request_user: ArticleDTO) -> str: pass

    @abstractmethod
    def delete_user(self, request_user: ArticleDTO) -> str: pass

    @abstractmethod
    def find_all_users(self, page: int) -> List[Article]: pass

    @abstractmethod
    def find_user_by_id(self, request_user: ArticleDTO) -> ArticleDTO: pass

    @abstractmethod
    def find_userid_by_email(self, request_user: ArticleDTO) -> str: pass