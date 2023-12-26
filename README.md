# spuds

## Linux Install
1. Clone the Repo

2. Set up VENV
```
python3 -m venv .venv
```

3. Activate VENV
```
source .venv/bin/activate
```

4. Install requirements
```
pip install -r requirements.txt
```

5. Make copy of config
```
cp example.config.yml config.yml
```

6. Update config with your settings
```
nano config.yml
```

7. Make sure to choose a free port for Prometheus. 

8. Add the job to Prometheus.yml. If you are running Prometheus in docker make sure to choose the gateway IP like you would for node exporter

9. Restart Prometheus

10. Create a new Import Dashboard and copy/paste the grafana.json contents into your dashboard

11. Update the UID for the data source with your UID

12. The dashboard should populate.

