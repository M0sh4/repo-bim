CREATE TABLE `findtransaccion_match` (
  `financial_transaction_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `transaction_type` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `transaction_reference` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `transaction_date` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `fromfri` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `tofri` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `context` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

INSERT INTO DRYRUN_CAPTURE.findtransaccion_match (financial_transaction_id, transaction_type, transaction_reference, transaction_date, fromfri, tofri, context) VALUES ('396193577', 'CASH_IN', '121420241115115940', '2024-11-15 12:02:00.239000', 'FRI:51989294475/MSISDN', 'FRI:51970007041/MSISDN', 'http-ci_kasnet_partner');
INSERT INTO DRYRUN_CAPTURE.findtransaccion_match (financial_transaction_id, transaction_type, transaction_reference, transaction_date, fromfri, tofri, context) VALUES ('396193493', 'CASH_IN', '727920241115115928', '2024-11-15 12:01:48.226000', 'FRI:51989294475/MSISDN', 'FRI:51912760622/MSISDN', 'http-ci_kasnet_partner');
