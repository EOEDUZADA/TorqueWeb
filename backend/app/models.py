from sqlalchemy import Boolean, String, ForeignKey, Numeric, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from decimal import Decimal

class Base(DeclarativeBase):
    pass

#Funcionário
class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    active: Mapped[bool] = mapped_column(Boolean, default=True)


#Cliente
class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))

#Veículos
class Vehicle(Base):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id")) #Chave estrangeira que vai ligar o veículo com seu dono
    plate: Mapped[str] = mapped_column(String(10))
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column()
    mileage: Mapped[int] = mapped_column()


# Peças
    
class Part(Base):
    __tablename__ = "parts"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(String(50))
    category: Mapped[str] = mapped_column(String(50))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2)) #Numeric para evitar problemas típicos do float
    quantity_available: Mapped[int] = mapped_column()
    active: Mapped[bool] = mapped_column(Boolean, default=True)


#Ordems de serviço

class WorkOrder(Base):
    __tablename__ = "work_orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(
        ForeignKey("vehicles.id")
    )
    initial_analysis: Mapped[str] = mapped_column(Text)
    services_performed: Mapped[str] = mapped_column(Text)
    labor_cost: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    status: Mapped[str] = mapped_column(
        String(30),
        default="Em andamento",
    )
    created_by: Mapped[int] = mapped_column(
        ForeignKey("employees.id")
    )


#Peças da ordem de serviço
class WorkOrderPart(Base):
    __tablename__ = "work_order_parts"

    id: Mapped[int] = mapped_column(primary_key=True)
    work_order_id: Mapped[int] = mapped_column(
        ForeignKey("work_orders.id")
    )
    part_id: Mapped[int] = mapped_column(
        ForeignKey("parts.id")
    )
    quantity: Mapped[int] = mapped_column()
    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2) #Mantém o preço da peça relacionado à ordem e não com o preço da tabela 'part'
    )

#Mapped -> Tipagem e definir o tipo de dado
#mapped_column -> Detalhes da coluna no banco
    
