import itertools

def findInputs(ex):
    inputs=[]
    for c in ex:
        if c!='+' and c!='*' and c!='-' and c!='(' and c!=')' and c!=' ' and c not in inputs:
            inputs.append(c)
    return inputs

def evaluate(ex,row):
    input_no=0
    replaced=[]
    for c in ex:
        if c!='+' and c!='*' and c!='-' and c!='(' and c!=')' and c!=' ' and c not in replaced :
            ex=ex.replace(c,str(row[input_no]))
            input_no+=1
            replaced.append(c)

            
    ex=ex.replace('+','&')
    ex=ex.replace('*','|')
    ex=ex.replace('-','~')
    result=eval(ex)
    return result

def compute_results(truthtable,ex):
    outputs=[]
    for row in truthtable:
        outputs.append(evaluate(ex,row))
    return outputs


n=int(input('ENTER NUMBER OF INPUTS: '))
print('Rules: ')
print('1) TO ENTER "AND" USE "+"')
print('2) TO ENTER "OR" USE "*"')
print('3) TO ENTER "NOT" USE "-"')
logical_expression=input('ENTER THE LOGICAL EXPRESSION: ')
truth_table = list(itertools.product([0,1],repeat=n))
table_outputs=compute_results(truth_table,logical_expression)


print('')
print('Truth Table:')
print('')
for c in findInputs(logical_expression):
    print(c,end=' ')
print('Output')
for i in range(len(truth_table)):
    for val in truth_table[i]:
        print(val,end=' ')
    print(' ',table_outputs[i])
print('')

if table_outputs.count(1)>=1:
    print('The entered propositional logic expression is SATISFIABLE')
else:
    print('The entered propositional logic expression is NOT SATISFIABLE')