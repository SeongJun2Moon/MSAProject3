# 코드
### user_email = Column(String(20), primary_key=True) # django의 model 역할 
### password = Column(String(20), nullable=False) # nullable:필수작성 공란안됨

# 오류
### fastapi.exceptions.FastAPIError: Invalid args for response field! Hint: check that <class 'app.models.user.User'> is a valid pydantic field type
```python
# model 구성하는 class 안에 밑에 추가 
class Config:
    BaseConfig.arbitrary_types_allowed = True
    allow_population_by_field_name = True
```
### sqlalchemy.exc.InvalidRequestError: Table 'posts' is already defined for this MetaData instance. 
```python
# model 구성하는 class 안에 밑에 추가 
__abstract__ = True
```