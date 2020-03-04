#--volume=$HOME/neo4j/data:/data
#docker run --rm --publish=7474:7474 --publish=7687:7687 --env=NEO4J_AUTH=neo4j/test --env=dbms.security.auth_enabled=false --env=dbms.connector.bolt.listen_address=0.0.0.0:7687 --env=dbms.connector.bolt.tls_level=OPTIONAL --env=dbms.connector.http.listen_address=0.0.0.0:7474 neo4j        
#docker run --rm --publish=7474:7474 --publish=7687:7687 --env=NEO4J_AUTH=neo4j/test --env=dbms.connectors.default_listen_address=0.0.0.0 neo4j        


docker run --rm --publish=7474:7474 --publish=7687:7687 --volume=$HOME/neo4j/data:/data --volume=$HOME/neo4j/logs:/logs --volume=$HOME/neo4j/conf:/conf neo4j 
#dump-config