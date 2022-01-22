import joblib
import streamlit as st
import networkx as nx
from streamlit_agraph import agraph, Node, Edge, Config

st.markdown("# Graph Vis")

with st.spinner("Loading graph dataset"):
    G = joblib.load('graph.joblib')

# controls
unique_node_type = list(set([n[1]['ent_typ'] for n in G.nodes(data=True)]))
node_type = st.sidebar.multiselect('Node types',unique_node_type,default=unique_node_type)    
unique_edge_type=list(set([n[2]['relation'] for n in G.edges(data=True)]))                               
edge_type = st.sidebar.multiselect('Edge types',unique_edge_type,unique_edge_type)                                   

layout = st.sidebar.selectbox('Layout',['dot','neato','circo','fdp','sfdp'])
edge_style = st.sidebar.selectbox('Edge style',['STRAIGHT','CURVE_SMOOTH','CURVE_FULL',])                                   

with st.spinner("Subset graph"):
        subset = [n[0] for n in G.nodes(data=True) if n[1]['ent_typ'] in node_type]
        subgraph = nx.subgraph(G,subset)

        node_and_degree = subgraph.degree()
        nx.set_node_attributes(subgraph, values = dict(subgraph.degree), name='degree')
        most_connected_node = sorted(subgraph.degree, key=lambda x: x[1], reverse=True)[0][0]
        subgraph = nx.ego_graph(subgraph, most_connected_node)

# Now create the equivalent Node and Edge lists
nodes = [Node(id=n[0], label=str(n[1]['name']), size=(10+n[1]['degree'])**2) for n in subgraph.nodes(data=True)]
edges = [Edge(
                source=e[0],
                target=e[1],
                labelProperty="",
                label=e[2]['relation'],
                type=edge_style) 
                for e in subgraph.edges(data=True) if e[0] in subgraph.nodes and e[1] in subgraph.nodes]

config = Config(width=500, 
                height=500,
                #graphviz_layout=layout,
                directed=True,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6", # or "blue"
                collapsible=False,
                node={'labelProperty':'label'},
                link={'labelProperty': 'label', 'renderLabel': True},
                # **kwargs e.g. node_size=1000 or node_color="blue"
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)