import os
import pandas as pd
import xml.etree.ElementTree as ET
import streamlit as st
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def process_xml_file(xml_file):
    ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Extract the NF-e info first to get chaveNFe
    nfe_info = extract_nfe_info(root, ns)
    chave_nfe = nfe_info['chaveNFe']  # Ensure this key matches what extract_nfe_info() returns

    # Pass chave_nfe to the other extraction functions
    items_list = extract_items_info(root, ns, chave_nfe)
    total_dict = extract_total_info(root, ns, chave_nfe)
    transp_dict = extract_transport_info(root, ns, chave_nfe)
    cobr_dict = extract_billing_info(root, ns, chave_nfe)
    pag_list = extract_payment_info(root, ns, chave_nfe)

    # Create DataFrames for each extracted part
    df_nfe_dict = pd.DataFrame([nfe_info])
    df_items = pd.DataFrame(items_list)
    df_total = pd.DataFrame([total_dict])
    df_transp = pd.DataFrame([transp_dict])
    df_cobr = pd.DataFrame([cobr_dict])
    df_pag = pd.DataFrame(pag_list)

    # Merging DataFrames on 'chaveNFe'
    df_merged = df_nfe_dict.merge(df_items, on='chaveNFe', how='left')
    df_merged = df_merged.merge(df_total, on='chaveNFe', how='left')
    df_merged = df_merged.merge(df_transp, on='chaveNFe', how='left')
    df_merged = df_merged.merge(df_cobr, on='chaveNFe', how='left')
    df_merged = df_merged.merge(df_pag, on='chaveNFe', how='left')

    return df_merged


def show_home():
    st.title("Query Your XML Data")
    uploaded_files = st.file_uploader("Choose XML files", type='xml', accept_multiple_files=True)
    
    if uploaded_files:
        all_dfs = []  # List to hold all DataFrames from each file
        for uploaded_file in uploaded_files:
            df_current = process_xml_file(uploaded_file)
            all_dfs.append(df_current)

        if all_dfs:
            # Concatenate all DataFrames into a single DataFrame
            combined_df = pd.concat(all_dfs, ignore_index=True)
            st.write(combined_df)  # Display the combined DataFrame only once

            # Initialize and use agent for conversational AI interactions
            groq_api_key = os.getenv('GROQ_API_KEY')
            if groq_api_key is None:
                st.error("GROQ_API_KEY is not set. Please check your environment variables.")
            else:
                agent = create_pandas_dataframe_agent(
                    ChatGroq(model_name="llama3-8b-8192", temperature=0, groq_api_key=groq_api_key),
                    combined_df,
                    verbose=True
                )
                prompt = st.text_input("Enter your question about the data:")
                if st.button("Generate") and prompt:
                    with st.spinner("Generating response..."):
                        response = agent.invoke(prompt)
                        st.write(response["output"])


def process_nfe_files(folder_path):
    xml_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.xml')]
    df_all = pd.DataFrame()
    
    for file_path in xml_files:
        df_merged_current = process_xml_file(file_path)
        df_all = pd.concat([df_all, df_merged_current], ignore_index=True)

    return df_all

# Helper functions to extract information from XML
def extract_nfe_info(root, ns):
    nfe_infNFe = root.find('./nfe:NFe/nfe:infNFe', ns)
    chave_nfe = nfe_infNFe.attrib.get('Id', 'ID Not Found')[3:] if nfe_infNFe else 'Element Not Found'
    
    nfe_dict = {'chaveNFe': chave_nfe}
    
    # Extração direta de dados específicos
    ide = nfe_infNFe.find('.//nfe:ide', ns) if nfe_infNFe is not None else None
    emit = nfe_infNFe.find('.//nfe:emit', ns) if nfe_infNFe is not None else None
    dest = nfe_infNFe.find('.//nfe:dest', ns) if nfe_infNFe is not None else None

    if ide is not None:
        nfe_dict['nNF'] = ide.find('.//nfe:nNF', ns).text if ide.find('.//nfe:nNF', ns) is not None else 'Elemento nNF Não Encontrado'
        nfe_dict['dhEmi'] = ide.find('.//nfe:dhEmi', ns).text if ide.find('.//nfe:dhEmi', ns) is not None else 'Elemento dhEmi Não Encontrado'

    if emit is not None:
        nfe_dict['xNome_emit'] = emit.find('.//nfe:xNome', ns).text if emit.find('.//nfe:xNome', ns) is not None else 'Elemento xNome_emit Não Encontrado'
        nfe_dict['CNPJ_emit'] = emit.find('.//nfe:CNPJ', ns).text if emit.find('.//nfe:CNPJ', ns) is not None else 'Elemento CNPJ_emit Não Encontrado'
    
    if dest is not None:
        nfe_dict['xNome_dest'] = dest.find('.//nfe:xNome', ns).text if dest.find('.//nfe:xNome', ns) is not None else 'Elemento xNome_dest Não Encontrado'
        nfe_dict['CNPJ_dest'] = dest.find('.//nfe:CNPJ', ns).text if dest.find('.//nfe:CNPJ', ns) is not None else 'Elemento CNPJ_dest Não Encontrado'
        enderDest = dest.find('.//nfe:enderDest', ns)
        nfe_dict['xMun_dest'] = enderDest.find('.//nfe:xMun', ns).text if enderDest is not None and enderDest.find('.//nfe:xMun', ns) is not None else 'Elemento xMun_dest Não Encontrado'

    return nfe_dict


def extract_items_info(root, ns, chave_nfe):
    items = []
    for det in root.findall('./nfe:NFe/nfe:infNFe/nfe:det', ns):
        item_dict = {'nItem': det.attrib['nItem']}

        # Extract product information
        prod = det.find('./nfe:prod', ns)
        if prod is not None:
            item_dict['cProd'] = prod.find('nfe:cProd', ns).text if prod.find('nfe:cProd', ns) is not None else 'Produto Sem Código'
            item_dict['xProd'] = prod.find('nfe:xProd', ns).text if prod.find('nfe:xProd', ns) is not None else 'Produto Sem Descrição'
            item_dict['qCom'] = float(prod.find('nfe:qCom', ns).text) if prod.find('nfe:qCom', ns) is not None else 0.0
            item_dict['vUnCom'] = float(prod.find('nfe:vUnCom', ns).text) if prod.find('nfe:vUnCom', ns) is not None else 0.0
            item_dict['vUnTrib'] = float(prod.find('nfe:vUnTrib', ns).text) if prod.find('nfe:vUnTrib', ns) is not None else 0.0

        # Extract ICMS information
        for tipo in ['ICMS00', 'ICMS10', 'ICMS20', 'ICMS30', 'ICMS40', 'ICMS41', 'ICMS50', 'ICMS51', 'ICMS60', 'ICMS70', 'ICMS90']:
            icms = det.find(f'.//nfe:ICMS/nfe:{tipo}', ns)
            if icms is not None:
                item_dict['vBC_ICMS'] = float(icms.find('.//nfe:vBC', ns).text if icms.find('.//nfe:vBC', ns) is not None else 0.0)
                item_dict['pICMS'] = float(icms.find('.//nfe:pICMS', ns).text if icms.find('.//nfe:pICMS', ns) is not None else 0.0)
                item_dict['vICMS'] = float(icms.find('.//nfe:vICMS', ns).text if icms.find('.//nfe:vICMS', ns) is not None else 0.0)
                break  # Stop looking for other ICMS types if one is found

        # Extract PIS information
        pis = det.find('.//nfe:PIS/nfe:PISAliq', ns)
        if pis is not None:
            item_dict['vBC_PIS'] = float(pis.find('.//nfe:vBC', ns).text if pis.find('.//nfe:vBC', ns) is not None else 0.0)
            item_dict['pPIS'] = float(pis.find('.//nfe:pPIS', ns).text if pis.find('.//nfe:pPIS', ns) is not None else 0.0)
            item_dict['vPIS'] = float(pis.find('.//nfe:vPIS', ns).text if pis.find('.//nfe:vPIS', ns) is not None else 0.0)

        # Extract COFINS information
        cofins = det.find('.//nfe:COFINS/nfe:COFINSAliq', ns)
        if cofins is not None:
            item_dict['vBC_COFINS'] = float(cofins.find('.//nfe:vBC', ns).text if cofins.find('.//nfe:vBC', ns) is not None else 0.0)
            item_dict['pCOFINS'] = float(cofins.find('.//nfe:pCOFINS', ns).text if cofins.find('.//nfe:pCOFINS', ns) is not None else 0.0)
            item_dict['vCOFINS'] = float(cofins.find('.//nfe:vCOFINS', ns).text if cofins.find('.//nfe:vCOFINS', ns) is not None else 0.0)

        # Assume 'chaveNFe' is defined earlier in the context where this function is called
        item_dict['chaveNFe'] = chave_nfe  # Add this line if chaveNFe is defined globally or passed in some way

        items.append(item_dict)
    return items


# Implement other extraction functions similarly
def extract_total_info(root, ns, chave_nfe):
    total_dict = {}

    # Extracting total invoice values
    total = root.find('./nfe:NFe/nfe:infNFe/nfe:total/nfe:ICMSTot', ns)
    if total is not None:
        total_dict['vBC'] = float(total.find('nfe:vBC', ns).text if total.find('nfe:vBC', ns) is not None else 0.0)
        total_dict['vICMS'] = float(total.find('nfe:vICMS', ns).text if total.find('nfe:vICMS', ns) is not None else 0.0)
        total_dict['vProd'] = float(total.find('nfe:vProd', ns).text if total.find('nfe:vProd', ns) is not None else 0.0)
        total_dict['vIPI'] = float(total.find('nfe:vIPI', ns).text if total.find('nfe:vIPI', ns) is not None else 0.0)
        total_dict['vPIS'] = float(total.find('nfe:vPIS', ns).text if total.find('nfe:vPIS', ns) is not None else 0.0)
        total_dict['vCOFINS'] = float(total.find('nfe:vCOFINS', ns).text if total.find('nfe:vCOFINS', ns) is not None else 0.0)
        total_dict['vNF'] = float(total.find('nfe:vNF', ns).text if total.find('nfe:vNF', ns) is not None else 0.0)

    # Extracting retained tax values
    retTrib = root.find('./nfe:NFe/nfe:infNFe/nfe:total/nfe:retTrib', ns)
    if retTrib is not None:
        total_dict['vRetPIS'] = float(retTrib.find('nfe:vRetPIS', ns).text if retTrib.find('nfe:vRetPIS', ns) is not None else 0.0)
        total_dict['vRetCOFINS'] = float(retTrib.find('nfe:vRetCOFINS', ns).text if retTrib.find('nfe:vRetCOFINS', ns) is not None else 0.0)

    # Associating the 'chaveNFe' with the totals for identifying the related invoice
    total_dict['chaveNFe'] = chave_nfe

    return total_dict

def extract_transport_info(root, ns, chave_nfe):
    transp_dict = {}
    
    # Finding the transport information in the XML
    transp = root.find('./nfe:NFe/nfe:infNFe/nfe:transp/nfe:transporta', ns)
    if transp is not None:
        transp_dict['CNPJ_transp'] = transp.find('nfe:CNPJ', ns).text if transp.find('nfe:CNPJ', ns) is not None else 'N/A'

    # Include the 'chaveNFe' in the transport dictionary to link this information with the respective invoice
    transp_dict['chaveNFe'] = chave_nfe

    return transp_dict


def extract_billing_info(root, ns, chave_nfe):
    cobr_dict = {}

    # Finding the billing information in the XML
    cobr = root.find('./nfe:NFe/nfe:infNFe/nfe:cobr/nfe:fat', ns)
    if cobr is not None:
        cobr_dict['nFat'] = cobr.find('nfe:nFat', ns).text if cobr.find('nfe:nFat', ns) is not None else 'N/A'
        cobr_dict['vOrig'] = float(cobr.find('nfe:vOrig', ns).text) if cobr.find('nfe:vOrig', ns) is not None else 0.0
        cobr_dict['vLiq'] = float(cobr.find('nfe:vLiq', ns).text) if cobr.find('nfe:vLiq', ns) is not None else 0.0

    # Include the 'chaveNFe' to link the billing information with the respective invoice
    cobr_dict['chaveNFe'] = chave_nfe

    return cobr_dict

def extract_payment_info(root, ns, chave_nfe):
    pag_list = []
    
    # Finding payment details in the XML
    pag = root.findall('./nfe:NFe/nfe:infNFe/nfe:pag/nfe:detPag', ns)
    for detPag in pag:
        vPag = float(detPag.find('nfe:vPag', ns).text) if detPag.find('nfe:vPag', ns) is not None else 0.0
        payment_info = {'vPag': vPag, 'chaveNFe': chave_nfe}
        pag_list.append(payment_info)
    
    return pag_list


if __name__ == "__main__":
    show_home()
