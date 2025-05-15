from sqlalchemy import Column, Integer, String, Date, ForeignKey, CLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Clientes(Base):
    __tablename__ = 'Clientes'
    ClienteID = Column(Integer, primary_key=True)
    Nombre = Column(String(100), nullable=False)
    Apellido = Column(String(100), nullable=False)

class Asuntos(Base):
    __tablename__ = 'Asuntos'
    NumeroExpediente = Column(Integer, primary_key=True)
    ClienteID = Column(Integer, ForeignKey('Clientes.ClienteID'), nullable=False)
    FechaInicio = Column(Date, nullable=False)
    FechaArchivo = Column(Date)  # Alternativamente FechaFinalizacion
    Estado = Column(String(50), nullable=False)

class Gabinetes(Base):
    __tablename__ = 'Gabinetes'
    GabineteID = Column(Integer, primary_key=True)
    Nombre = Column(String(100), nullable=False)
    Pais = Column(String(50), nullable=False)

class Abogados(Base):
    __tablename__ = 'Abogados'
    Pasaporte = Column(String(20), primary_key=True)
    Nombre = Column(String(100), nullable=False)
    Especialidad = Column(String(100), nullable=False)

class Audiencias(Base):
    __tablename__ = 'Audiencias'
    AudienciaID = Column(Integer, primary_key=True)
    NumeroExpediente = Column(Integer, ForeignKey('Asuntos.NumeroExpediente'), nullable=False)
    FechaAudiencia = Column(Date, nullable=False)
    AbogadoPasaporte = Column(String(20), ForeignKey('Abogados.Pasaporte'), nullable=False)
    Incidencias = Column(CLOB, nullable=True)
