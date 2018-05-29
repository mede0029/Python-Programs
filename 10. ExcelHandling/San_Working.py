#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8
import xlrd  # importando a biblioteca
import xlsxwriter
import xlwt

####################
# Read in original xls file, and rearrange data
####################

workbook = xlrd.open_workbook('origem.xls', 'r')  # escolhe o arquivo a ser lido
worksheet = workbook.sheet_by_index(0)  # escolher a aba a ser lida

# criando uma array para cada coluna do novo arquivo:
outputID = []
outputVulnerability = []
outputCheckID = []
outputStatus = []
outputRisk = []
outputCriticality = []
outputProbability = []
outputDescription = []
outputThreat = []
outputSolution = []

numColumns = worksheet.ncols # ncols is a function - getting the number of columns in the worksheet
recordCount = 0 # Track the current record number to be used in loop
newRecord = True # Indica o começo de um novo registro

# looping em cada linha, criando uma variável pra cada coluna:
for rows in range(0, worksheet.nrows):
    col1 = worksheet.cell(rows, 0)
    colString1 = col1.__str__()
    colString1 = colString1.replace("text:'", "")  # removing "text:'" from the value
    colString1 = colString1.replace("empty:''","")  # removing "empty:''" from the value
    colString1 = colString1.replace("'","")  # removing the final ' from  the value

    col2 = worksheet.cell(rows, 1)
    colString2 = col2.__str__()
    colString2 = colString2.replace("text:'", "")  # removing "text:'" from the value
    colString2 = colString2.replace("empty:''", "")  # removing "empty:''" from the value
    colString2 = colString2.replace("'", "")  # removing the final ' from  the value

    col3 = worksheet.cell(rows, 2)
    colString3 = col3.__str__()
    colString3 = colString3.replace("text:'", "")  # removing "text:'" from the value
    colString3 = colString3.replace("empty:''", "")  # removing "empty:''" from the value
    colString3 = colString3.replace("'", "")  # removing the final ' from  the value

    # Read in the first row of each new record, and split it into ID  and Vulnerability fields
    # Tratamos a primeira linha de maneira diferente, porque ela á e unica que não tem um valor
    # a ser procurado na primeira coluna e outro a ser lido na terceira coluna
    if newRecord is True and colString1 != "": # a principio o newRecord é sempre True. Se não for uma linha vazia
        out = colString1.split('.')
        # split the string on the 4th . to get the ID and Vulnerability
        # 4.1.1.3. Vulnerability text is here
        #        ^ splitting the text here and placing into the two variables below
        outputID.append('.'.join(out[:4]))
        outputVulnerability.append('.'.join(out[4:]))
        newRecord = False  # Agora ja sabemos que nõa é mais a primeira linha, podemos partir para os
                            # próximos registros que vão funcionar de maneira diferente.

    elif "Check ID" in colString1:  # se "Check ID" na primeira coluna
        outputCheckID.append(colString3) # adicione a terceira coluna à array outputCheckID

    elif "Status" in colString1:
        outputStatus.append(colString3)

    elif "Risk" in colString1:
        outputRisk.append(colString3)

    elif "Criticality" in colString1:
        outputCriticality.append(colString3)

    elif "Probability" in colString1:
        outputProbability.append(colString3)

    elif "Description" in colString1:
        outputDescription.append(colString3)

    elif "Threat" in  colString1:
        outputThreat.append(colString3)

    elif "Solution" in colString1:
        outputSolution.append(colString3)

    # This is the last row of each record, reset the newRecord boolean to true, and increment the record counter
    # meaning is new record, therefore, new line
    elif "Return to the results table" in colString1:
        recordCount = recordCount + 1  # Reached the end of the record, increment counter by 1
        newRecord = True # start all over again (next row in nex file)

####################
# Write rearranged data to new xls file
####################

workbookOut = xlwt.Workbook()  # abre uma planilha em branco
worksheetOut = workbookOut.add_sheet('WPmodelo')  # nomeia uma sheet

worksheetOut.write(0, 0, 'ID')  # criando as colunas com nome
worksheetOut.write(0, 1, 'VULNERABILITY')
worksheetOut.write(0, 2, 'CHECK ID')
worksheetOut.write(0, 3, 'STATUS')
worksheetOut.write(0, 4, 'RISK')
worksheetOut.write(0, 5, 'CRITICALITY')
worksheetOut.write(0, 6, 'PROBABILITY')
worksheetOut.write(0, 7, 'DESCRIPTION')
worksheetOut.write(0, 8, 'THREAT')
worksheetOut.write(0, 9, 'SOLUTION')

# loop through each record and write to the excel file, one row at a time
# use outCells + 1 because outCells starts at 0 and we've already written the headers to row 0
for outCells in range(recordCount):
    worksheetOut.write(outCells + 1, 0, outputID[outCells])
    worksheetOut.write(outCells + 1, 1, outputVulnerability[outCells])
    worksheetOut.write(outCells + 1, 2, outputCheckID[outCells])
    worksheetOut.write(outCells + 1, 3, outputStatus[outCells])
    worksheetOut.write(outCells + 1, 4, outputRisk[outCells])
    worksheetOut.write(outCells + 1, 5, outputCriticality[outCells])
    worksheetOut.write(outCells + 1, 6, outputProbability[outCells])
    worksheetOut.write(outCells + 1, 7, outputDescription[outCells])
    worksheetOut.write(outCells + 1, 8, outputThreat[outCells])
    worksheetOut.write(outCells + 1, 9, outputSolution[outCells])

workbookOut.save('MODELO.xls')  # salva a planilha