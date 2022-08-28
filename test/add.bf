,  c0 = get user input for first number
subtract 48 to convert ASCII value to integer
> ++++++++  c1 = 8 loop counter
[
< ------  subtract 6 from c0
> -       subtract 1 from c1
]  loop ends when c1 = 0

,  c1 = get user input for second number
> ++++++++  c2 = 8 loop counter
[
< ------  subtract 6 to c1
> -       subtract 1 from c2
]  loop ends when c2 = 0

<  move to the previous cell (c1)

[    start loop on loop counter cell (c1)
< +  add 1 to c0
> -  subtract 1 from c1
]    end loop on loop counter cell (c1)

copy c0 to c1
<[->+>+<<]>>[-<<+>>]<


add 48 to convert integer to ASCII value
++++++++  c1 = 8 loop counter
[
< ++++++  add 6 to c0
> -       subtract 1 from c1
]
< .       print out c0
