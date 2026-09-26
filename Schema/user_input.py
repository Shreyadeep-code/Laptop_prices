from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal

class UserInput(BaseModel):

    company: Annotated[str,Field(...,description='enter the Laptop company')]
    TypeName: Annotated[str,Field(...,description='Laptop type')]
    Ram:Annotated[int,Field(...,gt=0,description='Ram in GB')]
    TouchScreen:Annotated[Literal['YES','NO'],Field(...,description='Touchscreen or not')]
    IPS:Annotated[Literal['YES','NO'],Field(...,description='IPS or not')]
    weight:Annotated[float,Field(...,gt=0,description='Weight of laptop in grams')]
    Screenresolution:Annotated[str,Field(...,description='screen resolution')]
    Screensize:Annotated[float,Field(...,description='Screen size')]
    Hard_drive:Annotated[int,Field(...,ge=0,description='Enter hard drive size in GB')]
    ssd:Annotated[int,Field(...,ge=0,description='enter SSD size in GB')]
    opsys:Annotated[str,Field(...,description='Enter the opreating system')]
    cpu_name: Annotated[str,Field(...,description='enter cpu-name')]
    gpu_name:Annotated[str,Field(...,description='enter gpu_name')]

    @computed_field
    @property
    def x_res(self)->int:
        return int(self.Screenresolution.split('x')[0])

    @computed_field
    @property
    def y_res(self)->int:
        return int(self.Screenresolution.split('x')[1])

    @computed_field
    @property
    def ppi(self)->float:
        return float(((self.x_res**2+self.y_res**2)**0.5)/self.Screensize)
    @computed_field
    @property
    def ts(self)-> int:
        return 1 if self.TouchScreen=='YES' else 0

    @computed_field
    @property
    def ips(self)->int:
        return 1 if self.IPS=='YES' else 0
    

