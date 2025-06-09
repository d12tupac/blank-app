import streamlit as st
import pandas as pd

st.title("Facture Utilisateur Summary")

# Check if openpyxl is installed
try:
    import openpyxl
except ImportError:
    st.error("The 'openpyxl' package is required but not installed. Please run: pip install openpyxl")
    st.stop()

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, engine='openpyxl')
        
        st.write("### Raw Data Preview")
        st.write(df.head())
        
        # Check if required columns exist
        required_columns = ['Utilisateur', 'NOM_D_UTILISATEUR', 'Nombre_de_Factures', 
                          'Factures_du_montant_total', 'Nombre_de_ANNULER', 'Montant_total_ANNULER']
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            st.error(f"Missing required columns in Excel file: {', '.join(missing_columns)}")
            st.stop()
        
        # Generate summary
        summary = df.groupby(['Utilisateur', 'NOM_D_UTILISATEUR']).agg({
            'Nombre_de_Factures': 'sum',
            'Factures_du_montant_total': 'sum',
            'Nombre_de_ANNULER': 'sum',
            'Montant_total_ANNULER': 'sum'
        }).reset_index()
        
        # Rename columns for better display
        summary = summary.rename(columns={
            'Nombre_de_Factures': 'Total Factures',
            'Factures_du_montant_total': 'Montant Total',
            'Nombre_de_ANNULER': 'Factures Annulées',
            'Montant_total_ANNULER': 'Montant Annulé'
        })
        
        st.write("### User Facture Summary")
        st.dataframe(summary)
        
        # Download button
        st.download_button(
            label="Download Summary as Excel",
            data=summary.to_csv(index=False, sep=';').encode('utf-8'),
            file_name='user_facture_summary.csv',
            mime='text/csv'
        )
        
    except Exception as e:
        st.error(f"An error occurred while processing the file: {str(e)}")
