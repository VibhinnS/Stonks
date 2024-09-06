
# Stonks - A New Way To Visualize Stock Data

- Steps to run :- 
    - 
    - Have Kafka on your local setup
    - Run Zookeeper service -
     `.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties`

    - Run the server props service 
     `.\bin\windows\kafka-server-start.bat .\config\server.properties`
    
    - Create a venv in your development dir and install the dependencies (NOTE : Do NOT install latest versions of Elasticsearch or Kafka. Python 3.12 is not stable in prod yet. Please use the mentioned versions only)
    - Run command `pip install -r requirements.txt` after activating venv
    - Once installed, navigate to `<venv-name>/Lib/elasticsearch/compat.py` and fix this code line

    From This - 
    ```python 
    try:
        from collections.abs import Mapping
    except ImportError:
        from collections import Mapping
    ```
    To This - 
    ```python
    try:
        from collections.abs import Mapping
    except ImportError:
        from collections.abc import Mapping
    ```
    - Run `docker-compose up` from terminal and pull the Elasticsearch and Kibana images
    - In 2 separate terminals, run `python producer.py` and `python consumer.py`
    - Head to `http://localhost:9200/_cat/indices?v` and see if `stock_data` is in the indexed list
    - Move to `http://localhost:5601/` to check Kibana
    - Add index pattern `stock_data*` in index pattern and create dashboard of your taste




