CREATE TABLE `DR3_msisdn_20241230` (
  `id_msisdn` int NOT NULL DEFAULT '0' COMMENT 'identificador',
  `date_capture_datetime` datetime(3) DEFAULT NULL,
  `msisdn` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci DEFAULT NULL COMMENT 'numero',
  PRIMARY KEY (`id_msisdn`),
  KEY `idx_date_capture_datetime` (`date_capture_datetime`),
  KEY `idx_id_date_msisdn` (`id_msisdn`,`msisdn`,`date_capture_datetime`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

INSERT INTO DRYRUN_CAPTURE.DR3_msisdn_20241230 (id_msisdn, date_capture_datetime, msisdn) VALUES (29, '2025-01-31 19:19:02.630', '51933010240');
INSERT INTO DRYRUN_CAPTURE.DR3_msisdn_20241230 (id_msisdn, date_capture_datetime, msisdn) VALUES (1253, '2025-01-31 10:36:19.061', '51934698153');
