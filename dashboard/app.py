import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
import random

st.set_page_config(page_title="Sales Dashboard RT", layout="wide")
st.title("📊 Sales Dashboard — Real-Time")
st.caption(f"Atualizado em: {datetime.now().strftime('%H:%M:%S')}")

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Receita Hoje", "R$ 42.318", "+12%")
col2.metric("🛒 Pedidos", "318", "+8")
col3.metric("🎯 Ticket Médio", "R$ 133,07", "-2%")
col4.metric("📦 Em Aberto", "42", "+5")

hours = [f"{h:02d}:00" for h in range(8, 20)]
sales = [random.randint(1000, 8000) for _ in hours]
df = pd.DataFrame({"Hora": hours, "Receita": sales})
st.plotly_chart(px.bar(df, x="Hora", y="Receita", title="Receita por Hora"), use_container_width=True)
