import sys 
sys.path.insert(1, 'libs')
import json as json
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base  
from marshmallow import Schema, fields

Base = declarative_base()

class JsonNode(Base):
    __tablename__ = 'Plantilla_json_node'

    id_json_node = Column(Integer, primary_key=True, autoincrement=True)
    id_json_api = Column(Integer, ForeignKey('Plantilla_json_api.id_json_api'))
    node_key = Column(String(255), nullable=False)
    node_value = Column(Text)
    parent_node_id = Column(Integer, ForeignKey('Plantilla_json_node.id_json_node'))
    node_level = Column(Integer, nullable=False)
    id_json_type = Column(Integer, ForeignKey('Plantilla_json_type.id_json_type'))

    parent_node = relationship('JsonNode', remote_side=[id_json_node], back_populates='children', foreign_keys=[parent_node_id])
    children = relationship('JsonNode', back_populates='parent_node')
    document = relationship('JsonDocument', back_populates='nodes', foreign_keys=[id_json_api])
    type = relationship('JsonType', back_populates='nodes', foreign_keys=[id_json_type])

class JsonDocument(Base):
    __tablename__ = 'Plantilla_json_api'

    id_json_api = Column(Integer, primary_key=True, autoincrement=True)
    api_name = Column(String(255), nullable=False)
    date_created = Column(DateTime, default=None)
    version_json = Column(String(20), nullable=False)
    status_json = Column(Integer, nullable=False)
    nodes = relationship('JsonNode', back_populates='document', foreign_keys=[JsonNode.id_json_api])

class JsonType(Base):
    __tablename__ = 'Plantilla_json_type'
    
    id_json_type = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(50), nullable=False)
    nodes = relationship('JsonNode', back_populates='type', foreign_keys=[JsonNode.id_json_type])

class JsonTypeSchema(Schema):
    id_json_type = fields.Int()
    type_name = fields.Str()

class JsonDocumentSchema(Schema):
    id_json_api = fields.Int()
    api_name = fields.Str()
    date_created = fields.DateTime()
    version_json = fields.Str()
    status_json = fields.Int()

class JsonNodeSchema(Schema):
    id_json_node = fields.Int()
    id_json_api = fields.Int()
    node_key = fields.Str()
    node_value = fields.Str()
    parent_node_id = fields.Int()
    node_level = fields.Int()
    id_json_type = fields.Int()