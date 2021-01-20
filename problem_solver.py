
import copy
import io
import os
class qn:
    "this is the class which is can be used to represent the question object"
    def __init__(self,label="",values={}):
        
        self.label= label
        self.values=values
        self.operation=""
        self.ans=None
        
    def solve(self):
        exec(self.operation)
    def displayval(self):
        print("\n\n")
        for i in self.values:
            print(i,"=",self.values[i])
    def printq(self):
        print(self.label)
        
    def inpu(self,edit):
        print("\n\nenter the values\n")
        for i,j in zip(self.values,range(len(self.values))):
            
            if self.values[i]!=None and j in edit:
                
                print(i,":",end='')
                self.values[i]=float(input())







#gets the data from the file and parses it 

def getqns():
    f = open("questions.txt",'r')
    #the following 3 variables wil hold the label of the question the values and the operations
    qns=[]
    val=[]
    operations=['']

    a = {}#stores the values of a single question
    label='' #stores the label of a single question
    oper='' #store the equations of a single question

    mode=-1 #determines which type of data is being read
    first = True #this indicates where the current question is the first one or not


    for i in f:
        m = i.strip()

        if m == 'q:':   #sets the mode ie question, equation or values mode
            mode = 0
            if first:
                first = False
            else:       #saves the data of previous question
                val.append(a)
                qns.append(label)
                operations.append('')
                label = ''
                a = {}
            continue
        elif m == 'v:':
            mode = 1
            continue
        elif m == 'e:':
            mode = 2
            continue
    
        if mode == 0:   #collects the label
        
                label+=i
            
        if '=' in i:    #seperates the question from the values and equations
            
            if mode == 1:    
                l=i.find('=')
                a [i[:l].strip()]=float(i[l+1:].strip())    #find the given values and saves them in the dictionary
            
            elif mode == 2:                 #in the equation mode it parses the equation
                l=i.find('=')
                a [i[:l].strip()]=None
                #get the equation 
                oper = i.strip()
                #cleanse the equation
                starting_label=0
                for s in oper :
                    if not s .isalpha()and not s.isnumeric():
                        if s !='_' and s != '.': 
                            oper=oper.replace(s," "+s+" ") #adds spaces between operand and operator eg : 2/4 becomes 2 / 4
                            
    
                            continue
            
                
                oper =  oper.split() # splits operators to add the self keyword so that execution can take place 
        
                for i in oper:
                    if i.isalpha() or '_' in i:
                        operations [-1] += 'self.values[\''+i+'\']' #changes all names to self.values['<name>']
                        continue
                    operations [-1] += i
                operations[-1]+='\n' #seperates different operations within a single question with \n
    
    #appends the values and label of the final question : no need to do this for equations
    val.append(a)
    qns.append(label)
    f.close()                
    return qns,val,operations


#clears the screen
def cls(lines=0):
    n=os.get_terminal_size()
    n=n[1]
    n=10
    for i in range(n-lines):
        print('')


#makes the set of question into a list of objects
def makeset():
    l=[]
    temp=qn()

    
      
    qns,val,operations = getqns()

    

    for i,j,k in zip(qns,val,operations):

        temp.label = i
        temp.values = j
        temp.operation = k

        l.append(copy.deepcopy(temp))   #make a copy of the objects

    
    return l


#main program


def main():
    ls=makeset()
    

    print("---question list--- \n\n")
    no=0
    for i in ls:
        print("question number :",no)
        i.printq()
        no+=1

    print("\n\nenter the question number:",end='')
    no=int(input())

    a = ls[no]

    print("\n\n---answer---\n\n")
    cls()
    a.printq()
    a.displayval()
    print("\n----------------------------------------------")
    print("do you wish to edit the data (y/n):",end='')
    choice=input()
    if choice == 'y' or choice == 'Y':
        print("enter the no of the data you wish to edit:",end='')
        edit=list(map(int,input().strip().split()))
        a.inpu(edit)
    a.solve()
    a.displayval()


main()
c=input()
