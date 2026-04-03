import streamlit as st
from datetime import datetime, date

# Configurazione della pagina
st.set_page_config(page_title="MedAudit B2B - Legal", layout="wide")

# Intestazione per gli Studi Legali
st.title("⚖️ MedAudit - Tool di Pre-Valutazione Medico-Legale")
st.subheader("Valutazione strategica per Azione Diretta ex art. 12 L. 24/2017 (Foro di Milano)")
st.markdown("---")

# Sezione 1: Dati del Sinistro e Regime Temporale (Claims Made)
st.header("1. Inquadramento Temporale del Sinistro")
st.info("Verifica della retroattività decennale obbligatoria e del regime Claims Made.")

col1, col2 = st.columns(2)
with col1:
    data_evento = st.date_input("Data in cui si è verificato l'evento dannoso (presunto errore):", min_value=date(2000, 1, 1))
with col2:
    data_richiesta = st.date_input("Data della prima richiesta di risarcimento (Claim):", value=datetime.today())

# Calcolo della retroattività
anni_trascorsi = data_richiesta.year - data_evento.year
if data_richiesta < data_evento:
    st.error("La data della richiesta danni non può essere precedente all'evento.")
elif anni_trascorsi > 10:
    st.warning("⚠️ ATTENZIONE: L'evento dannoso risale a oltre 10 anni fa. Potrebbe essere superato il limite della retroattività decennale obbligatoria prevista per le polizze.")
else:
    st.success(f"✅ L'evento rientra nei {anni_trascorsi} anni precedenti alla richiesta. Copertura compatibile con la retroattività decennale obbligatoria.")

# Sezione 2: Tipologia di Struttura e Massimali Minimi (D.M. 232/2023)
st.header("2. Inquadramento della Struttura e Copertura")
tipo_struttura = st.selectbox(
    "Seleziona la tipologia di Struttura Sanitaria coinvolta:",
    [
        "Struttura ambulatoriale (no ambulatori protetti/laboratori analisi)",
        "Struttura SENZA attività chirurgica, ortopedica, anestesiologica e parto",
        "Struttura CON attività chirurgica, ortopedica, anestesiologica e parto"
    ]
)

# Determinazione del massimale minimo di legge
massimale = ""
if "ambulatoriale" in tipo_struttura:
    massimale = "1.000.000 €"
elif "SENZA" in tipo_struttura:
    massimale = "2.000.000 €"
else:
    massimale = "5.000.000 €"

st.info(f"💡 In base al D.M. 232/2023, questa struttura deve avere un massimale minimo garantito per sinistro di **{massimale}**.")

# Compagnia Assicurativa e Foro
st.subheader("Individuazione Compagnia Assicuratrice")
compagnia = st.selectbox("La struttura risulta assicurata con:", ["Sconosciuta / In autoritenzione (Misure Analoghe)", "AM Trust (Sede: Milano)", "Relyens (Sede: Milano)", "Altra Compagnia"])

# Sezione 3: Generazione Report Strategico
st.markdown("---")
if st.button("Genera Dossier di Fattibilità Azione Diretta", type="primary"):
    st.header("📑 Dossier Strategico Preliminare")
    
    if compagnia in ["AM Trust (Sede: Milano)", "Relyens (Sede: Milano)"]:
        st.success("**Esito Strategico:** ALTA FATTIBILITÀ per radicare l'Accertamento Tecnico Preventivo (ATP) presso il **Tribunale di Milano**.")
        st.write("L'Azione Diretta contro l'assicuratore (Art. 12 Legge 24/2017) è pienamente operativa. È consigliabile notificare il ricorso ex art. 696-bis c.p.c. presso la sede legale della compagnia a Milano per favorire una gestione transattiva più rapida.")
    elif compagnia == "Sconosciuta / In autoritenzione (Misure Analoghe)":
        st.warning("**Esito Strategico:** AZIONE DIRETTA NON ESPERIBILE O A RISCHIO.")
        st.write("Se la struttura opera in regime di auto-ritenzione del rischio (Misure Analoghe) e ha costituito un Fondo Rischi/Fondo Riserva Sinistri, l'azione diretta contro l'assicurazione non è possibile. Si dovrà procedere direttamente contro la Struttura e valutare la capienza dei loro fondi di bilancio.")
    else:
        st.info("**Esito Strategico:** AZIONE DIRETTA ESPERIBILE.")
        st.write("Verificare la sede legale dell'assicurazione per determinare il Foro competente più vantaggioso in cui incardinare l'ATP.")