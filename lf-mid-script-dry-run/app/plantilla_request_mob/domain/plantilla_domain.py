'''Plantilla Domain'''
from app.shared.utils import Utils
class PlantillaDomain:
    ''' Class Plantilla Domain'''

    def build_json_structure(self,nodes) -> dict:
        '''Método para estructurar de table a json'''
        try:
            print(repr("Estructurando plantilla request de Comviva. \n plantilla_domain/build_json_structure"))
            utils = Utils()
            if(not isinstance(nodes, list)):
                raise ValueError("Error DR: La plantillas Mobiquity no tiene tipo de dato list \n plantilla_domain/build_json_structure")
            
            node_dict = {node.id_json_node: node for node in nodes}
            json_structure = {
            }

            for node in nodes:
                document_name = node.document.api_name
                id_json_api = str(node.id_json_api)

                if id_json_api not in json_structure:
                    json_structure[id_json_api] = {
                        document_name: {}
                    }
                if document_name not in json_structure[id_json_api]:
                    json_structure[id_json_api][document_name] = {}

                if node.parent_node_id is None:
                    json_structure[id_json_api][document_name][node.node_key] = self.get_node_value(node, node_dict)

            combined_json = utils.deserializacion_json(json_structure)

            if not combined_json:
                raise ValueError("Error DR: No existe plantillas Mobiquity para la petición \n plantilla_domain/build_json_structure")
            
            print(repr(f"Consulta exitosa plantilla request de Comviva. \n plantilla_domain/build_json_structure {combined_json}"))
            return combined_json
        except ValueError:
            raise
        except IndexError:
            raise
        except KeyError:
            raise
        except TypeError:
            raise
        except AttributeError:
            raise
        except Exception as e:
            print(repr(f"Error DR: json_structure: {e} \n plantilla_domain/build_json_structure"))

    def get_node_value(self, node, node_dict):
        try:
            # Buscar los hijos de este nodo
            children = [child for child in node_dict.values() if child.parent_node_id == node.id_json_node]

            # Si el nodo es de tipo 'object', retornamos un diccionario con sus hijos.
            if node.type.id_json_type == 3:  # object
                result = {}
                for child in children:
                    child_value = self.get_node_value(child, node_dict)
                    result[child.node_key] = child_value
                return result
            
            # Si el nodo es de tipo 'array', manejamos la lógica según los requisitos especificados.
            if node.type.id_json_type == 4:  # array
                result = []
                seen_values = set()  # Para almacenar valores únicos si hay hermanos con el mismo node_key

                # Detectar si los hijos deben ser objetos (cuando tienen el mismo parent_node_id)
                grouped_children = {}
                for child in children:
                    # Validar si el valor no es nulo o vacío antes de procesar
                    child_value = self.get_node_value(child, node_dict)
                    if child_value not in (None, "", "None"):
                        if child.parent_node_id not in grouped_children:
                            grouped_children[child.parent_node_id] = {}
                        grouped_children[child.parent_node_id][child.node_key] = child_value

                # Si se encuentran hijos agrupados, añádelo al array como objetos
                for obj in grouped_children.values():
                    result.append(obj)

                # Si no hay hijos agrupados (es decir, es un array simple), aplicamos validaciones
                if not grouped_children:
                    for child in children:
                        child_value = self.get_node_value(child, node_dict)
                        if child_value not in (None, "", "None"):
                            seen_values.add(child_value)  # Almacena valores únicos

                    # Convertir el conjunto a una lista y ordenar (opcional)
                    result = list(seen_values)

                # Si no hay hijos pero el nodo tiene un valor
                if node.node_value not in (None, "", "None"):
                    seen_values.add(node.node_value)

                # Devolver la lista de valores únicos o un array vacío si no hay valores
                return list(seen_values) if seen_values else result

            if node.type.id_json_type == 2:  # number
                return int(node.node_value) if node.node_value not in (None, "", "None") else 0
            elif node.type.id_json_type == 1:  # string
                return str(node.node_value) if node.node_value not in (None, "", "None") else ""
            elif node.type.id_json_type == 6:  # float
                return float(node.node_value) if node.node_value not in (None, "", "None") else 0.0
            elif node.type.id_json_type == 7:  # boolean
                # Convertir el valor de texto "True" o "False" a un valor booleano
                if node.node_value == "True":
                    return True
                elif node.node_value == "False":
                    return False
                else:
                    return False
    
            return node.node_value if node.node_value not in (None, "", "None") else None
        except ValueError:
            raise
        except IndexError:
            raise
        except KeyError:
            raise
        except TypeError:
            raise
        except AttributeError:
            raise
        except Exception as e:
            print(repr(f"Error DR: Error general json_structure: {e}"))