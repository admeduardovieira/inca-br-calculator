import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Título do app
st.set_page_config(page_title="Calculadora de Risco de Câncer - INCA Brasil", page_icon="🩺")

# Data files path
male_cancer_data_path = "man.csv"
female_cancer_data_path = "woman.csv"

# File existence check
if not os.path.exists(male_cancer_data_path) and not os.path.exists(female_cancer_data_path):
    st.error("Arquivos de dados não encontrados.")
    st.stop()

# Age group identification (Brazilian age groups)
def get_age_group(age):
    age_groups = [(0, 4), (5, 9), (10, 14), (15, 19), (20, 24), (25, 29), (30, 34),
                  (35, 39), (40, 44), (45, 49), (50, 54), (55, 59), (60, 64),
                  (65, 69), (70, 74), (75, 79), (80, 84), (85, 999)]
    for group in age_groups:
        if group[0] <= age <= group[1]:
            return f"{group[0]}-{group[1]}"
    return "Sem dados"

# Cumulative incidence calculation
def calculate_cumulative_risk(df, start_age_group, years):
    if start_age_group not in df.columns:
        return np.nan
    
    age_group_index = df.columns.get_loc(start_age_group)
    max_index = min(age_group_index + (years // 5), len(df.columns) - 1)
    risk_values = df.iloc[:, age_group_index:max_index].values
    cumulative_risk = 1 - np.prod(1 - risk_values / 100000, axis=1)
    return cumulative_risk * 100

# App Title
st.title("🩺 Calculadora de Risco de Câncer - INCA Brasil")
st.markdown("**Baseado nos dados do Instituto Nacional do Câncer (INCA) - Brasil**")

# Age and Gender Input
age = st.number_input("Digite sua idade", min_value=0, max_value=100, value=0, step=1)
gender = st.selectbox("Selecione seu gênero", ["Selecione", "Masculino", "Feminino"])

# Age group
age_group = get_age_group(age)

# Load and process data
selected_data = None
if gender == "Masculino":
    if os.path.exists(male_cancer_data_path):
        male_df = pd.read_csv(male_cancer_data_path, encoding="utf-8", index_col=0)
        if age_group in male_df.columns:
            selected_data = male_df[[age_group]].copy()
            selected_data["5_anos_risco_acumulado (%)"] = calculate_cumulative_risk(male_df, age_group, 5)
            selected_data["10_anos_risco_acumulado (%)"] = calculate_cumulative_risk(male_df, age_group, 10)
elif gender == "Feminino":
    if os.path.exists(female_cancer_data_path):
        female_df = pd.read_csv(female_cancer_data_path, encoding="utf-8", index_col=0)
        if age_group in female_df.columns:
            selected_data = female_df[[age_group]].copy()
            selected_data["5_anos_risco_acumulado (%)"] = calculate_cumulative_risk(female_df, age_group, 5)
            selected_data["10_anos_risco_acumulado (%)"] = calculate_cumulative_risk(female_df, age_group, 10)

# Display results
if selected_data is not None:
    st.subheader(f"Risco de Câncer para {age_group} anos - {gender}")
    st.dataframe(selected_data.style.format("{:.2f}"))
    
    # Graph
    fig, ax = plt.subplots(figsize=(10, 6))
    plot_data = selected_data[["5_anos_risco_acumulado (%)", "10_anos_risco_acumulado (%)"]]
    plot_data.plot(kind="bar", ax=ax, color=["#ff6b6b", "#4ecdc4"])
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Risco (%)")
    plt.title(f"Risco de Câncer acumulado - {gender}, {age_group} anos")
    plt.legend(["5 anos", "10 anos"])
    
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f'{height:.2f}%', (p.get_x() * 1.005, height * 1.005), fontsize=8)
    
    st.pyplot(fig, use_container_width=True)
elif gender != "Selecione":
    st.write("⚠️ Dados não disponíveis para esta faixa etária ou gênero.")

st.markdown("---")
st.caption("💡 Esta calculadora é educacional. Para avaliação médica, consulte um profissional.")