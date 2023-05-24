import zipfile

zip = zipfile.ZipFile ('arquivoszipados.zip', 'w', zipfile.ZIP_DEFLATED)
zip.write('arquivos/Anexo_I_Rol.pdf', 'Anexo_I_Rol.pdf')
zip.write('arquivos/Anexo_I_Rol_excel.xlsx', 'Anexo_I_Rol_excel.xlsx')
zip.write('arquivos/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN540_RN541_RN542_RN544_546_550_553_571v2_575_576_577.pdf', 'Anexo_II_DUT_2021.pdf')
zip.write('arquivos/Anexo_III_DC_2021_RN_465.2021.v2.pdf', 'Anexo_III_DC_2021_RN_465.2021.v2.pdf')
zip.write('arquivos/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf', 'Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf')
zip.close
