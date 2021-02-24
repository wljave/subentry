import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'new title'
sheet['A1'] = '漫威宇宙'
rows = [['美国队长', '钢铁侠', '蜘蛛侠'], ['是', '漫威', '宇宙', '经典', '人物']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('Marvel.xlsx')
