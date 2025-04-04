CREATE TABLE `DR4_REVERSA_COMPARTAMOS_AHORROS_20251014` (
  `id_log_rever` int NOT NULL,
  `date_capture_datetime` datetime DEFAULT NULL,
  `sendingfri_req` varchar(255) DEFAULT NULL,
  `receivingfri_req` varchar(255) DEFAULT NULL,
  `FROMFRI` varchar(255) DEFAULT NULL,
  `TOFRI` varchar(255) DEFAULT NULL,
  `FINANCIALTRANSACTIONID_HIST` varchar(255) DEFAULT NULL,
  `FITYPE` varchar(50) DEFAULT NULL,
  `amount_rever` decimal(10,2) DEFAULT NULL,
  `amount_hist` decimal(10,2) DEFAULT NULL,
  `status_rever` varchar(10) DEFAULT NULL,
  `sendernote_hist` text,
  `row_refund` int DEFAULT NULL,
  `row_hist` int DEFAULT NULL,
  PRIMARY KEY (`id_log_rever`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

INSERT INTO DRYRUN_CAPTURE.DR4_REVERSA_COMPARTAMOS_AHORROS_20251014 (id_log_rever, date_capture_datetime, sendingfri_req, receivingfri_req, FROMFRI, TOFRI, FINANCIALTRANSACTIONID_HIST, FITYPE, amount_rever, amount_hist, status_rever, sendernote_hist, row_refund, row_hist) VALUES (339878, '2025-01-04 05:43:19', 'FRI:51985020019/MSISDN', 'FRI:51917737228/MSISDN', 'FRI:51917737228/MSISDN', 'FRI:51985020019/MSISDN', '414135387', 'PAYMENT_SEND', 25.00, 25.00, '', 'c1c6e176-ca5e-11ef-a2af-af454ec06eb0', 1, 1);
INSERT INTO DRYRUN_CAPTURE.DR4_REVERSA_COMPARTAMOS_AHORROS_20251014 (id_log_rever, date_capture_datetime, sendingfri_req, receivingfri_req, FROMFRI, TOFRI, FINANCIALTRANSACTIONID_HIST, FITYPE, amount_rever, amount_hist, status_rever, sendernote_hist, row_refund, row_hist) VALUES (339904, '2025-01-04 05:08:51', 'FRI:51985020019/MSISDN', 'FRI:51933577113/MSISDN', 'FRI:51933577113/MSISDN', 'FRI:51985020019/MSISDN', '414133938', 'PAYMENT_SEND', 100.00, 100.00, '', 'f7df1f55-ca59-11ef-97fb-6b2b264a6103', 2, 2);
