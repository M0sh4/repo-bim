@echo off
REM Iniciar los servicios de InfluxDB y Grafana en segundo plano
docker-compose up -d influxdb grafana

REM Separador visual
echo --------------------------------------------------------------------------------------
echo Load testing with Grafana dashboard http://localhost:3000/d/k6/k6-load-testing-results
echo --------------------------------------------------------------------------------------

REM Ejecutar el script de estrés con k6
docker-compose run --rm k6 run --env ENV=QA /scripts/main.js > logs.txt 2>&1