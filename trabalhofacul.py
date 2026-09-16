import pandas as pd
import numpy as np

# Configuração de semente para reprodutibilidade
np.random.seed(42)

n_records = 500

bairros = ['Centro', 'Alto da Boa Vista', 'Croatá', 'Pedras', 'Tucunduba', 'Buriti']
faixas_etarias = ['0-12 anos', '13-17 anos', '18-59 anos', '60+ anos']
sexos = ['Feminino', 'Masculino']
agravos = ['Hipertensão', 'Diabetes', 'Dengue/Arboviroses', 'Atendimento Pré-Natal', 'Saúde Mental', 'Rotina/Preventivo']
ubs_list = ['UBS Centro', 'UBS Alto da Boa Vista', 'UBS Croatá', 'UBS Pedras']
status_list = ['Em Acompanhamento', 'Alta/Resolvido', 'Encaminhado Especialista', 'Falta/Absenteísmo']

data = {
    'ID_Atendimento': [f'ATD-{1000+i}' for i in range(n_records)],
    'Data_Atendimento': pd.date_range(start='2026-06-01', periods=n_records, freq='h').strftime('%d/%m/%Y'),
    'Bairro_Residencia': np.random.choice(bairros, size=n_records, p=[0.25, 0.20, 0.18, 0.15, 0.12, 0.10]),
    'Faixa_Etaria': np.random.choice(faixas_etarias, size=n_records, p=[0.15, 0.10, 0.45, 0.30]),
    'Sexo': np.random.choice(sexos, size=n_records),
    'Agravo_Saude': np.random.choice(agravos, size=n_records, p=[0.30, 0.25, 0.15, 0.10, 0.10, 0.10]),
    'UBS_Atendimento': np.random.choice(ubs_list, size=n_records),
    'Status_Acompanhamento': np.random.choice(status_list, size=n_records, p=[0.50, 0.25, 0.15, 0.10])
}

df = pd.DataFrame(data)
df.to_excel('dados_saude_preventiva.xlsx', index=False)