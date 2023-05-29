from openpyxl import load_workbook

book = load_workbook('OLX_MOTO_29_05_23.xlsx')
ws_name = 'ws2'
if ws_name not in book.wsnames:
    book.create_ws(ws_name)

ws = book[ws_name]
ws['A1'] = 'Top 3 anunturi'
ws.merge_cells('A1:C1')

ws['A2'] = 'Locul 1'
ws['A3'] = 'Locul 2'
ws['A4'] = 'Locul 3'

ws['A1'] = df_surpl['Key'].iloc[0]
ws['A2'] = df_surpl['Key'].iloc[1]
ws['A3'] = df_surpl['Key'].iloc[2]
ws['B1'] = df_surpl['Value'].iloc[0]
ws['B2'] = df_surpl['Value'].iloc[1]
ws['B3'] = df_surpl['Value'].iloc[2]

book.save('test.xlsx')

