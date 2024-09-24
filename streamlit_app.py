import streamlit_app as st
from streamlit_agraph import agraph, Node, Edge, Config

st.set_page_config(layout='wide')

st.title('Knowledge Graph 🧐')

m_1,m_2,m_3 = st.columns((2,6,2))

if 'node' not in st.session_state:
    st.session_state.node = []
if 'edge' not in st.session_state:
    st.session_state.edge = []

with m_2:
    c1, c2, c3 = st.columns((3, 4, 3))
    with st.form('None', border=False):
        with c1:
            from_node = st.text_input('from', key="from_node")

        with c2:
            label_edge = st.text_input('label', key="label_edge")

        with c3:
            to_node = st.text_input('to', key="to_node")

        submitted = st.form_submit_button('submit')

        if submitted:
            from_node_id = from_node.replace(' ', '_')
            to_node_id = to_node.replace(' ', '_')

            if from_node_id not in [node.id for node in st.session_state.node]:
                st.session_state.node.append(Node(id=from_node_id, 
                                                label=from_node, 
                                                size=25))

            if to_node_id not in [node.id for node in st.session_state.node]:
                st.session_state.node.append(Node(id=to_node_id, 
                                                label=to_node, 
                                                size=25))

            edge_exists = False
            for edge in st.session_state.edge:
                if edge.source == from_node_id and edge.to == to_node_id:
                    edge.label = label_edge
                    edge_exists = True
                    break

            if not edge_exists:
                st.session_state.edge.append(Edge(source=from_node_id, 
                                                label=label_edge, 
                                                target=to_node_id))

    config = Config(
        width=750,
        height=500,
        directed=True, 
        physics=True, 
        hierarchical=False
    )

    return_value = agraph(
        nodes=st.session_state.node, 
        edges=st.session_state.edge, 
        config=config
    )
