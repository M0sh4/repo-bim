CREATE TABLE `Plantilla_json_type` (
  `id_json_type` int NOT NULL AUTO_INCREMENT COMMENT 'identificador',
  `type_name` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL COMMENT 'tipo de variable',
  PRIMARY KEY (`id_json_type`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci


INSERT INTO DRYRUN_CAPTURE.Plantilla_json_type (id_json_type, type_name) VALUES (1, 'string');
INSERT INTO DRYRUN_CAPTURE.Plantilla_json_type (id_json_type, type_name) VALUES (2, 'number');
INSERT INTO DRYRUN_CAPTURE.Plantilla_json_type (id_json_type, type_name) VALUES (3, 'object');
INSERT INTO DRYRUN_CAPTURE.Plantilla_json_type (id_json_type, type_name) VALUES (4, 'array');
INSERT INTO DRYRUN_CAPTURE.Plantilla_json_type (id_json_type, type_name) VALUES (6, 'float');
INSERT INTO DRYRUN_CAPTURE.Plantilla_json_type (id_json_type, type_name) VALUES (7, 'bool');
