#Lab 7
3. 
```
> rules.all <- apriori(admissions)
Apriori

Parameter specification:
 confidence minval smax arem  aval originalSupport maxtime support minlen
        0.8    0.1    1 none FALSE            TRUE       5     0.1      1
 maxlen target   ext
     10  rules FALSE

Algorithmic control:
 filter tree heap memopt load sort verbose
    0.1 TRUE TRUE  FALSE TRUE    2    TRUE

Absolute minimum support count: 40 

set item appearances ...[0 item(s)] done [0.00s].
set transactions ...[164 item(s), 400 transaction(s)] done [0.00s].
sorting and recoding items ... [6 item(s)] done [0.00s].
creating transaction tree ... done [0.00s].
checking subsets of size 1 2 done [0.00s].
writing ... [1 rule(s)] done [0.00s].
creating S4 object  ... done [0.00s].
> rules.all
set of 1 rules 
> inspect(rules.all)
    lhs         rhs       support confidence lift    
[1] {rank=4} => {admit=0} 0.1375  0.8208955  1.202777
```
