# **Facture Utilisateur Summary App**  

🚀 **A Streamlit web app** that analyzes Excel files containing hospital billing data and generates a summary of invoices (factures) per user.  

## **📌 Features**  
✔ **Upload Excel files** (.xlsx or .xls)  
✔ **Preview raw data** before processing  
✔ **Generate summary reports** showing:  
   - Total invoices generated per user  
   - Total invoice amounts  
   - Total canceled invoices  
   - Total canceled amounts  
✔ **Download results** as a CSV file  

## **🛠 Installation & Setup**  

### **Prerequisites**  
- Python 3.7+  
- `pip` (Python package manager)  

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### **2. Install Dependencies**  
```bash
pip install streamlit pandas openpyxl
```

### **3. Run the App**  
```bash
streamlit run facture_app.py
```

The app will open in your default browser at `http://localhost:8501`.  

## **📂 Expected Excel File Format**  
The app processes Excel files with the following columns:  

| Column Name                 | Description                          |
|-----------------------------|--------------------------------------|
| `Hôpital`                   | Hospital name                        |
| `Utilisateur`               | User's full name                     |
| `NOM_D_UTILISATEUR`         | Username                            |
| `Date`                      | Invoice date (YYYYMMDD format)       |
| `Type_de_Facture`           | Invoice type (e.g., Consultation)    |
| `Nombre_de_Factures`        | Number of invoices generated         |
| `Factures_du_montant_total` | Total invoice amount                 |
| `Nombre_de_ANNULER`         | Number of canceled invoices          |
| `Montant_total_ANNULER`     | Total canceled amount                |

## **📸 Screenshots**  
*(Optional: Add screenshots of the app in action)*  

## **📝 How to Use**  
1. **Upload** your Excel file.  
2. **Preview** the raw data.  
3. **View** the summary report.  
4. **Download** the results as CSV.  

## **⚙ Deployment (Optional)**  
You can deploy this app on:  
- **Streamlit Cloud**  
- **Heroku**  
- **AWS/GCP**  

## **📜 License**  
This project is open-source under the **MIT License**.  



### **🔗 Links**  
- [GitHub Repository](https://github.com/your-username/your-repo-name)  
- [Streamlit Documentation](https://docs.streamlit.io/)  



🎉 **Enjoy using the app!** If you encounter issues, feel free to open an **Issue** or submit a **Pull Request**.  
