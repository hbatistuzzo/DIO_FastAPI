from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime

# Por algum motivo há uma distinção entre os schemas.py criados nas pastas atleta/categorias/etc e o criado
# no contrib (por que?). Originalmente foi importado

# from sqlalchemy.orm import DeclarativeBase, mas isso foi modificado posteriormente. Que confusão..

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True


class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de criação')] 


# # feito na aula e aparentemente abandonado posteriormente.
# class BaseModel(DeclarativeBase):
#     id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),default = uuid4, nullable=False)