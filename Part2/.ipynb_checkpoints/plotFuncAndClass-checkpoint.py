class nameAndUnit: #only contains the name and the unit, not the value 
    def __init__(self, keyIn, nameVarIn, varDescr='', unitVarIn = '', latIn = '' ):
        self.keyDF=keyIn; #key of the variable in the data Frame
        if unitVarIn=='': # if no parameters for unit, might result in problems if nameVarIn is not in the shape mdot(kg/s)
            interm=nameVarIn.split('(')
            self.nameVar=interm[0]
            self.unitVar=interm[1].split(')')[0]
        else:
            self.nameVar=nameVarIn; #Name of the variable
            self.unitVar= unitVarIn; #Unit of the variable 
        if varDescr=='':
            self.varDescription=nameVarIn; #description of the variable, default : name of the variable
        else:
            self.varDescription = varDescr;
        if latIn=='':
            self.lat=self.nameVar; #Latex representation of variable without dollars
        else:
            self.lat=latIn;
            
            
def fromNumDayToDate(numDay): #gives the date from the number of the day in the year, strating with 0 -> 01/01
    listMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
    choiceMonth=0;
    sumDayMonth=0;
    while(sumDayMonth<numDay):
        sumDayMonth+=listMonth[choiceMonth]
        choiceMonth+=1
    if(sumDayMonth==numDay):
        if choiceMonth < 9:
            interm = ('0'+str(choiceMonth+1));
        else:
            interm = str(choiceMonth+1)
        rez='01/'+interm;
    else:
        choiceMonth-=1;
        sumDayMonth-=listMonth[choiceMonth];
        numDayMonth=numDay-sumDayMonth+1;
        if choiceMonth < 9:
            interm = ('0'+str(choiceMonth+1));
        else:
            interm = str(choiceMonth+1)
        if numDayMonth<=9:
            interm2 = '0'+str(numDayMonth)
        else:
            interm2=str(numDayMonth)
        rez = interm2+'/'+interm;
    return rez