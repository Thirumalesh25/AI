likes(ram,mango).
girl(seema).
red(rose).
owns(john,gold).
likes(bill,cindy).

method 1
swipl -s a.pl

method 2
swipl
[a].

Prolog online compiler link to execute:
https://swish.swi-prolog.org/

?- likes(ram,What).
What=mango
?- likes(Who,cindy).
Who = bill
?- red(What).
What = rose
?-owns(Who,What).
What = gold,
Who = john