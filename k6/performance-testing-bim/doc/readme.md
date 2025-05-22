### Inicializar proyecto node
npm init -y

### Descargar libreria de K6
npm install --save-dev @types/k6

### Ejecucion
k6 run --env ENV=QA main.js

## Omitir setup y teardown
k6 run --no-setup --no-teardown ...

## Genera output JSON
--out json=results/test.json

## Genera output en influxdb
 <!-- --out influxdb=https://us-east-1-1.aws.cloud2.influxdata.com?bucket=k6_bim --out influxdb-auth=Jx7QttCAkyt4QiFrj1fBOaJmimqisbyc9EPM1Ad_4DwAyBp8YyMIBcTh2bc0oTeXBCn_MlU6McNkK_y9nWxpdQ==


--out influxdbv2=https://us-east-1-1.aws.cloud2.influxdata.com?bucket=k6_bim --out influxdbv2-token=Jx7QttCAkyt4QiFrj1fBOaJmimqisbyc9EPM1Ad_4DwAyBp8YyMIBcTh2bc0oTeXBCn_MlU6McNkK_y9nWxpdQ== -->

## Tipos de Prueba de Performance
Smoke Test . Verifique el funcionamiento del sistema con carga mínima.
Average Load Test . Descubra cómo funciona el sistema con tráfico típico.
Stress Test . Descubra cómo funciona el sistema con la carga de tráfico pico.
Spike Test . Descubra cómo funciona el sistema ante aumentos repentinos y masivos de tráfico.
Breakpoint Test . Aumente progresivamente el tráfico para descubrir puntos de interrupción del sistema.
Soak Test . Detecta si el sistema se degrada bajo cargas de mayor duración.