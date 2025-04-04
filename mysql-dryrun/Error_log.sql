CREATE TABLE `Error_log` (
  `id_error_log` int NOT NULL AUTO_INCREMENT COMMENT 'identificador',
  `id_log` int DEFAULT NULL COMMENT 'identificador de la tabla Log',
  `timestamp_error` datetime NOT NULL COMMENT 'fecha y hora del error',
  `error_type` varchar(225) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci NOT NULL COMMENT 'tipo de error',
  `error_message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci COMMENT 'mensaje del error',
  `stack_trace` text CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci COMMENT 'componente donde ocurrió el error',
  `id_mapping` int DEFAULT NULL COMMENT 'identificador de la tabla Mapping',
  `clave_ewp` varchar(225) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL COMMENT 'clave de la comparación',
  `is_resolved` tinyint(1) NOT NULL COMMENT '0: error sin reproceso / 1: procesado',
  `timestamp_resolved` datetime DEFAULT NULL COMMENT 'fecha y hora que se resuelve',
  PRIMARY KEY (`id_error_log`),
  KEY `Error_log_Log_FK` (`id_log`),
  KEY `Error_log_Mapping_FK` (`id_mapping`),
  CONSTRAINT `Error_log_Mapping_FK` FOREIGN KEY (`id_mapping`) REFERENCES `Mapping` (`id_mapping`)
) ENGINE=InnoDB AUTO_INCREMENT=376683 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci

