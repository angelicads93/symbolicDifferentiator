
####################################################################################################
####################################################################################################

def parsePolynomial(polyString):
    ###--- Remove spaces:
    polyList = []
    for i in polyString:
        if i!=' ':
            polyList.append(i)
    ###--- Identify terms (returns a list of list of elements):
    termsList = []
    signPosition = 0
    for i in range(len(polyList)):    
        tmp_i = polyList[i]
        if tmp_i=='+' or tmp_i=='-' and i>0:
            termsList.append(polyList[signPosition:i])
            signPosition = i
    termsList.append(polyList[signPosition:])
    ###--- Rewrite every element as a string (returns a list of strings):
    for i in range(len(termsList)):
        tmp_string = ''
        for j in range(len(termsList[i])):
            tmp_string += termsList[i][j]
        termsList[i] = tmp_string
    ###--- Identify prefactors and powers:
    powerList, prefactorList = [],[]
    for i in range(len(termsList)):
        #-- Powers larger or equal than 2:
        if 'x**' in termsList[i]:
            tmp_power     = int(termsList[i].split('x**')[1].split('*')[0])
            if '*x**' in termsList[i]:
                tmp_prefactor = termsList[i].split('*x**')[0] 
            else:
                tmp_prefactor = termsList[i].split('x**')[1].split('*')[1]
                if '-' in termsList[i].split('x**')[0]:
                    tmp_prefactor = '-'+tmp_prefactor
        #-- Linear terms:
        elif 'x' in termsList[i] and '**' not in termsList[i]:
            tmp_power = 1
            if '*x' in termsList[i]:
                tmp_prefactor = termsList[i].split('*x')[0]
            else:
                tmp_prefactor = termsList[i].split('x*')[1] 
                if '-' in termsList[i].split('x*')[0]:
                    tmp_prefactor = '-'+tmp_prefactor
       #-- Constant term:
        elif 'x' not in termsList[i]:
            tmp_prefactor = termsList[i]
            tmp_power = 0
        prefactorList.append(int(tmp_prefactor))
        powerList.append(tmp_power)
    return  prefactorList, powerList


def computeDerivative(prefactorList, powerList):
    derivativeList_prefactor = []
    derivativeList_power = []
    for i in range(len(prefactorList)):
        tmp_prefactor = prefactorList[i]*powerList[i]
        tmp_power = powerList[i]-1
        derivativeList_prefactor.append(tmp_prefactor)
        derivativeList_power.append(tmp_power)
    return derivativeList_prefactor, derivativeList_power


def builSymbolicExpression(derivativeList_prefactor, derivativeList_power):
    derivativeString = ''
    for i in range(len(derivativeList_prefactor)):
        #-- Constant term:
        if derivativeList_power[i] == 0:
            derivativeString += ' '+str(derivativeList_prefactor[i])
        #-- Linear term:
        if derivativeList_power[i]==1:
            if derivativeList_prefactor[i]>0:
                derivativeString += ' + '+str(derivativeList_prefactor[i])+'*x'
            elif derivativeList_prefactor[i]<0:
                derivativeString += ' - '+str(abs(derivativeList_prefactor[i]))+'*x'
        #-- Quadratic or larger:
        elif derivativeList_power[i]>1:
            if derivativeList_prefactor[i]>0:
                derivativeString += ' + '+str(derivativeList_prefactor[i])+'*x**'+str(int(derivativeList_power[i]))
            elif derivativeList_prefactor[i]<0:
                derivativeString += ' - '+str(abs(derivativeList_prefactor[i]))+'*x**'+str(int(derivativeList_power[i]))
    return derivativeString


####################################################################################################
####################################################################################################

inFunction = input('Polynomial = ')

prefactorList, powerList = parsePolynomial(inFunction)

derivativeList_prefactor, derivativeList_power = computeDerivative(prefactorList, powerList)

derivativeString = builSymbolicExpression(derivativeList_prefactor, derivativeList_power) 
print('Derivative = ', derivativeString)



